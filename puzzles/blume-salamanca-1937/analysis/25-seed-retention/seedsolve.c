/* Experiment 25: complete seed ranking and wider retention over experiment-21 engine.
 * Build: cc -O3 -march=native -o out/seedsolve seedsolve.c -lm
 * Run with cwd ../21-dc-method, where out/lm_es_{2,4}.bin live.
 * No true key/plaintext inputs. Random-key z is a ranking heuristic, not a p-value.
 */
#define main experiment21_main
#include "../21-dc-method/dcm.c"
#undef main
#include <sys/resource.h>

typedef struct { int id, w, key[MAXW]; double v, z; } Seed;
static void keycheck(const int *k, int w) {
    int seen[MAXW] = {0};
    if (w < 2 || w >= MAXW) { fprintf(stderr, "invalid width\n"); exit(2); }
    for (int i=0; i<w; i++) if (k[i]<0 || k[i]>=w || seen[k[i]]++) {
        fprintf(stderr, "invalid permutation\n"); exit(2);
    }
}
static void emit_seed(const Seed *s, int w1, int at) {
    printf("{\"w1\":%d,\"id\":%d,\"rank\":%d,\"w2\":%d,\"idp\":%.8f,\"z\":%.6f,\"k2\":\"",w1,s->id,at,s->w,s->v,s->z);
    print_key(stdout,s->key,s->w); printf("\"}\n");
}
static void setup(const char *ct, unsigned long long seed) {
    memset(&P,0,sizeof P); P.n=read_text(ct,P.ct); strcpy(P.conv,"CC");
    IDPMODE=1; ORACLE=0; PMI=0; SPACE=0;
    rs=88172645463325252ULL ^ seed; for(int i=0;i<10;i++) rnd64();
    load_lm("es"); t0w=now(); t0c=cpu();
}
static int compare_seed(const void *va,const void *vb) {
    const Seed *a=va,*b=vb;
    if(a->z>b->z) return -1;
    if(a->z<b->z) return 1;
    return (a->id>b->id)-(a->id<b->id);
}
/* Stream a deterministic one-swap expansion. One declared first-width hypothesis per call.
 * The same scan work is used for controls at that width and every target grid cell.
 */
static void scanbin(const char *file,int width,int keep,int samples) {
    if(width<2 || width>=MAXW || P.n/width<2 || keep<1 || keep>64 || samples<2) exit(2);
    P.w1=width;
    double mu[MAXW]={0},sd[MAXW]={0};
    for(int w=18;w<=28;w++) {
        P.w2=w; double m=0,m2=0;
        for(int i=0;i<samples;i++) { int k[MAXW]; random_key(k,w); double v=k2_idp(k);
            double d=v-m; m+=d/(i+1); m2+=d*(v-m); }
        mu[w]=m; sd[w]=sqrt(m2/(samples-1)); if(sd[w]<1e-8) sd[w]=1e-8;
    }
    FILE *f=fopen(file,"rb"); if(!f) { perror(file); exit(2); }
    Seed top[64]; for(int i=0;i<keep;i++) top[i].z=-1e100;
    int count=0,w;
    while((w=fgetc(f))!=EOF) {
        unsigned char bytes[MAXW];
        if(w<18 || w>28 || fread(bytes,1,(size_t)w,f)!=(size_t)w) exit(2);
        Seed s; s.id=count++; s.w=w;
        for(int j=0;j<w;j++) s.key[j]=bytes[j];
        keycheck(s.key,w); P.w2=w;
        s.v=k2_idp(s.key); s.z=(s.v-mu[w])/sd[w];
        int worst=0; for(int j=1;j<keep;j++) if(top[j].z<top[worst].z) worst=j;
        if(s.z>top[worst].z) top[worst]=s;
    }
    fclose(f); if(count<keep) exit(2);
    qsort(top,(size_t)keep,sizeof(Seed),compare_seed);
    for(int i=0;i<keep;i++) emit_seed(&top[i],width,i);
    fprintf(stderr,"{\"phase\":\"scanbin\",\"keys\":%d,\"n_idp\":%lld,\"cpu\":%.3f}\n",count,n_idp,cpu()-t0c);
}
static void scan(const char *file,int wmin,int wmax,int keep,int samples) {
    if(wmin<2 || wmax>=MAXW || wmax<wmin || keep<0 || keep>100000 || samples<2) exit(2);
    FILE *f=fopen(file,"r"); if(!f) { perror(file); exit(2); }
    Seed *keys=NULL; int count=0,cap=0, have[MAXW]={0}; char *line=NULL; size_t len=0;
    while(getline(&line,&len,f)>0) {
        char *tab=strchr(line,'\t'); if(!tab) exit(2); *tab=0;
        if(count==cap) { cap=cap?cap*2:1024; keys=realloc(keys,sizeof(Seed)*cap); if(!keys) exit(2); }
        Seed *s=&keys[count++]; s->id=atoi(line); s->w=parse_key(tab+1,s->key);
        keycheck(s->key,s->w); have[s->w]=1;
    }
    fclose(f); free(line); if(!count) exit(2);
    for(P.w1=wmin;P.w1<=wmax;P.w1++) {
        if(P.n/P.w1<2) { fprintf(stderr,"too few rows\n"); exit(2); }
        double mu[MAXW]={0},sd[MAXW]={0};
        for(int w=2;w<MAXW;w++) if(have[w]) {
            P.w2=w; double m=0,m2=0;
            for(int i=0;i<samples;i++) { int k[MAXW]; random_key(k,w); double v=k2_idp(k);
                double d=v-m; m+=d/(i+1); m2+=d*(v-m); }
            mu[w]=m; sd[w]=sqrt(m2/(samples-1)); if(sd[w]<1e-8) sd[w]=1e-8;
        }
        Seed *top=malloc(sizeof(Seed)*(size_t)count); if(!top) exit(2);
        for(int i=0;i<count;i++) {
            top[i]=keys[i]; P.w2=top[i].w;
            top[i].v=k2_idp(top[i].key); top[i].z=(top[i].v-mu[top[i].w])/sd[top[i].w];
        }
        qsort(top,(size_t)count,sizeof(Seed),compare_seed);
        int take=keep ? (keep<count ? keep : count) : count;
        for(int i=0;i<take;i++) emit_seed(&top[i],P.w1,i);
        free(top);
        fflush(stdout);
    }
    fprintf(stderr,"{\"phase\":\"scan\",\"keys\":%d,\"n_idp\":%lld,\"cpu\":%.3f}\n",count,n_idp,cpu()-t0c);
    free(keys);
}
static void seeded(const char *keystr,int w1,int climb,int budget,int restarts) {
    int k2[MAXW], k1[MAXW], best1[MAXW],best2[MAXW];
    P.w1=w1; P.w2=parse_key(keystr,k2); keycheck(k2,P.w2);
    if(w1<2 || w1>=MAXW || P.n/w1<2 || restarts<1 || budget<1) exit(2);
    CLIMB1=0; CLIMB2=1; BUDGET=budget;
    // Always try the exact seed first. A fallible IDP climb must not erase an exact key.
    double before=k2_idp(k2), best=k1_stage(k1,k2,restarts,1);
    memcpy(best1,k1,sizeof(int)*w1); memcpy(best2,k2,sizeof(int)*P.w2);
    if(climb) {
        // Start the IDP climb from the original phrase key, not a quadgram-altered key.
        parse_key(keystr,k2); nb_build(&NB2,P.w2); BUDGET=n_idp+budget;
        double v=climb_k2(k2); (void)v;
        double sc=k1_stage(k1,k2,restarts,1);
        if(sc>best) { best=sc; memcpy(best1,k1,sizeof(int)*w1); memcpy(best2,k2,sizeof(int)*P.w2); }
    }
    report("seed",0,before,best,best1,best2,-1);
}
int main(int argc,char **argv) {
    // Per-process CPU cap; wall-clock load does not weaken the evaluation budget.
    struct rlimit limit;
    limit.rlim_cur=(argc>1 && !strcmp(argv[1],"scanbin")) ? 180 : 60;
    limit.rlim_max=limit.rlim_cur+1;
    if(setrlimit(RLIMIT_CPU,&limit)!=0) { perror("CPU limit"); return 2; }
    if(argc>=2 && !strcmp(argv[1],"decrypt")) return experiment21_main(argc,argv);
    if(argc!=9) { fprintf(stderr,"scan CT KEYS WMIN WMAX KEEP SAMPLES SEED\nseed CT KEY W1 CLIMB BUDGET RESTARTS SEED\n"); return 2; }
    setup(argv[2],strtoull(argv[8],NULL,10));
    if(!strcmp(argv[1],"scan")) scan(argv[3],atoi(argv[4]),atoi(argv[5]),atoi(argv[6]),atoi(argv[7]));
    else if(!strcmp(argv[1],"scanbin")) scanbin(argv[3],atoi(argv[4]),atoi(argv[6]),atoi(argv[7]));
    else if(!strcmp(argv[1],"seed")) seeded(argv[3],atoi(argv[4]),atoi(argv[5]),atoi(argv[6]),atoi(argv[7]));
    else return 2;
    return 0;
}
