# Provenance — 05-documentary-onset

All files fetched 2026-10-20. Downloads are untrusted data; scripts only read them.

## sillok.history.go.kr (National Institute of Korean History)

Every response `fetch.py` saved is listed, one line each, in `data/manifest.tsv`:
path, method, URL, POST form, UTC time, sha256 and size of the uncompressed bytes.
The raw pages sit gzip-compressed in `data/raw/` (cache; not for commit, see README).

| Kind | Files | URL pattern | Tier |
|---|---|---|---|
| Reign month lists | `data/raw/months/*.html.gz` (32) | `https://sillok.history.go.kr/search/inspectionMonthList.do?id=<reign>` | PRIMARY (index) |
| Month article lists | `data/raw/days/*.html.gz` | `https://sillok.history.go.kr/search/inspectionDayList.do?id=<reign>_<month id>` | PRIMARY (index) |
| Joseon Sillok search, original text | `data/raw/search/w_<term hex>_pNNNN.html.gz` | POST `https://sillok.history.go.kr/search/searchResultList.do` with `type=w` | PRIMARY |
| Ming Shilu search | `data/raw/search/m_<term hex>_pNNNN.html.gz` | same, `type=m`, `sillokType=SMC` | PRIMARY |
| Sillok articles (text + Korean translation) | `data/raw/articles/*.html.gz` (11) | `https://sillok.history.go.kr/id/<article id>` | PRIMARY |

## Other files (`data/raw/papers/`)

| File | URL | sha256 | Tier |
|---|---|---|---|
| therrell2004.pdf | https://bpb-us-e1.wpmucdn.com/wordpressua.uark.edu/dist/1/224/files/2017/09/2004_Therrell_Stahle_Aztec-drought-and-the-curse-of-One-Rabbit.pdf?bid=224 | e65390903b7456087351d66357859d2ca0bc76737dfbff148f315b4ec194a4ac | SCHOLARLY (Therrell, Stahle & Acuña-Soto 2004, BAMS 85:1263) |
| olinski2016.pdf (scan, no text layer; read as images) | https://repozytorium.umk.pl/bitstreams/61abd483-7224-4e31-992c-bf65eda63e04/download | 97868f9141f86ad41e54c684d97ee691f56988887abdbfca14c50df0a355153f | SCHOLARLY (Oliński 2016, in *Jan Długosz (1415–1480): życie i dzieła*, pp. 199–208) |
| mingshi_25.wiki … mingshi_30.wiki | https://zh.wikisource.org/w/index.php?title=明史/卷25&action=raw (and 26–30) | 25: 451609c1…; 26: 85a4f1b8…; 27: ac0fd1a9…; 28: 902f7e10…; 29: c7697abb…; 30: 11eb556a… | SECONDARY (Mingshi, compiled 1739; Wikisource transcription) |
| chikyu_wp13.pdf | https://chikyu.repo.nii.ac.jp/record/2117/files/workingpapers13_1.pdf | 530a5f3d865ee29650bee036b87b039bd40724ae60ad7f4d37307139de7db170 | SCHOLARLY (Itō Keisuke, RIHN working paper; uses Fujiki 2007) |

Full sha256 for the Mingshi files: 25 `451609c13143324577c6a113f1aa844b24ae75d264ab2871377c836cede71d0a`,
26 `85a4f1b8e352f1b4fb7d67f61d8a5d7d68f859e87fd4480b369654fcc6d9ce8f`,
27 `ac0fd1a931d080cfcf81f06e6e5861556d4757ed2fcdb9e0342af0821881eab5`,
28 `902f7e10c2ab1d171264ff0fc9e36318274ae65977867237e11eca1d32fa9037`,
29 `c7697abbf6cab0c182ece82dde5558cb28ffe47ce65e668404c68fe42ea46898`,
30 `11eb556a8b25400d1842711f984286bc6c8bd8ffcd0d19df1902d02107b731a2`.

## Reached but not usable (walls)

| Source | URL | What happened |
|---|---|---|
| Euro-Climhist | https://www.echdb.unibe.ch/selection/welcome/en | Needs a registered account (free; scientific tier vetted by hand). Not registered: that is Greg's call. |
| Fujiki Hisashi, 日本中世災害史年表稿 (2007) | — | Book only; no open online version found. |
| tambora.org, REACHES | — | Not tried in this run. |
