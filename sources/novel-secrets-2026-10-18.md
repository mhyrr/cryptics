# Novel secrets: private enciphered or shorthand texts that nobody has read (2026-10-18)

*Agent survey, 2026-10-18. Inputs: `CLAUDE.md`, the two earlier 18 Oct surveys (`screenshot-opportunities-2026-10-18.md`,
`untouched-data/10-decryptable-resweep-2026-10-18.md`), `catalog/entries/` and `catalog/EXCLUDED.md`, and a fresh
`git clone` of Bourdeau's `dbourdeau/cyphersolver` (last commit 14 Oct 2026; 392 target folders, grepped for every
candidate). About 60 web searches. **Every archive host was blocked again.** WebFetch returned DNS `ENOTFOUND` for
scienceblogs.de, loc.gov, exhibits.lib.lehigh.edu, manuscripts.nls.uk, brusselsmorning.com and
pre1600ms.beinecke.library.yale.edu, and `curl` got `000` from wellcomecollection.org, iiif.wellcomecollection.org,
collections.library.yale.edu, e-manuscripta.ch and archive.org. So every catalogue fact below rests on **search-result
snippets** of the catalogue record (marked "snippet"). The one exception is what is quoted from Bourdeau's repository,
which was read directly. No readings were attempted (rule 9).*

## Summary

1. The novelty test was applied before readability. It removes almost everything diplomatic, and most famous private
   ciphers too: Pepys, Byrd, Lister, Wesley, Lichtenberg, Wittgenstein, Constant, Treby, Dickens, Rinzi and Prestwood are all read or being read.
2. **Best find: Miles Rock's Pitman-shorthand "Keep Shut" book (Lehigh, SC MS 0400.29.03, 1861–65).** The writer was a private soldier
   and signalman who rode on a Kilpatrick raid in 1864. The pages are digitized and his own shorthand textbook is in the same collection.
   No transcription was found.
3. **Montgomery Meigs's Pitman journals after 1861** (LOC, MSS32540, digitized) are the largest prize: the private daily record of the Union's
   Quartermaster General. Only 1853–59 and 1861 are published. Whether later years were transcribed privately is the open check.
4. Two Scottish **private cipher account books with their keys in the same volumes** are a key lookup, not cryptanalysis: Lord Milton
   1738–39 (NLS MS.16962, with keys in MS.17605) and Dundas of Dundas 1688–1701 (NLS Adv.MSS.80.3.48–50). They need an NLS scan order.
5. Rows 5–10 are weaker, and the reason is stated for each. The wall common to all ten is images: only rows 1, 2, 6 and 8 are online.

## Novelty test as applied

- **(a) Not read today.** Grep Bourdeau's repo and this repo, search for an edition or transcription, and search Cipherbrain, DECODE/HCPortal and Tomokiyo by snippet.
- **(b) No plaintext can exist by construction.** The text is a private diary, private account or private note whose only intended reader was the writer.
  No chancery, no recipient decipherment.
- **(c) Images reachable.** "Online" means a free viewer, per the snippet. "Order" means a reprographics request.
- **(d) Solvable by code.** A published shorthand system, or a key filed with the text, or simple substitution.

## Ranked table

| # | Document | Writer, date | (a) not read: evidence | (b) private | (c) images | ~Pages | System / solvability | Score note |
|---|---|---|---|---|---|---|---|---|
| 1 | **Lehigh Univ. Special Collections SC MS 0400.29.03 "Keep Shut Correspondence Book, 1861–1865"**, with SC MS 0400.03 "Shorthand Notebook" | Miles Rock (Lehigh alumnus, Union signalman, later astronomer and surveyor) | Omeka record has "only metadata and page scans, with no transcription" (snippet). Not in Bourdeau, Schmeh or the repo | Personal log and diary of a private soldier | **Online** (exhibits.lib.lehigh.edu items 8433/40705, 8421/40696) | est. 50–150 (unverified) | Benn Pitman, *Reporter's Companion* (Cincinnati 1861), and **his own copy is SC MS 0400.34** | Best ratio of novelty, access and solvability |
| 2 | **LOC Manuscript Division, Montgomery C. Meigs Papers, MSS32540, journals 1862–1892** | M. C. Meigs, Quartermaster General of the Union Army 1861–82 | Published edition covers only 1853–59 and 1861 (Wolff, *Capitol Builder*, S. Doc. 106-20, 2001). Martin K. Mohr worked "three volumes" (snippet, years unknown). No later edition found | Private daily journal | **Online** (LOC digitized from 51 reels, 42,508 images; the journals are believed to be included) | thousands | "Sloppy" mid-century Pitman (snippet). Readable but hard. A shorthand-reader problem, not a cipher | Highest value. Novelty for 1862+ not proven |
| 3 | **NLS MS.16962** (account book 1738–39, "inverted folios hold an account in cypher and two keys to cyphers"), plus MS.16980 (1754, with key), MS.17605 (keys 1737–55) and the 1746 volume with keys at ff. 12v–14v | Andrew Fletcher, Lord Milton, Lord Justice Clerk, manager of Scottish patronage for Islay | Nothing found in print on the cipher accounts. Not in Bourdeau | **Private accounts** in his own hand | Order (NLS reprographics). Not digitized as far as found | ~10–40 for the cipher account | Key in the same volume, so a lookup | Real "secret money" potential |
| 4 | **Atlantikwall Raversyde (Ostend), 1943 diary in Groote shorthand** (no inventory number found) | Unknown Ostend-region writer under occupation; the key lists "burgemeester", "gemeenteraadslid", "ontvangsten" | Museum's public appeal of 2 Sept 2025 says it "could read only a few words". No later result found (searched Oct 2026) | Private diary | Ask the museum (images not public) | unknown | Groote stenography (published Dutch system) plus a partial key **filed with the diary** | High interest, **crowding risk**: public call |
| 5 | **NLS Acc.6123/1–7, "shorthand diary probably of James Bonar", 1775–1821, 7 vols** | James Bonar (1757–1821), Solicitor of Excise; disturbed Deacon Brodie's gang in the Excise Office raid, March 1788; treasurer of the RSE | No edition found. **But** his son's c.1830 biography (NLS) "mostly draws on extracts from his diary", so some plaintext exists | Private diary | Order (7 vols; costly) | ~1,000+ | Unknown 18th-c. shorthand (Byrom, Gurney, Taylor are likely) | Rich, but (a) is partial and (c) is expensive |
| 6 | **PAN Biblioteka Kórnicka BK 02411, "Tekst pisany szyfrem", Paris 23 Jan 1855** | Leonard Niedźwiecki (1810–92), secretary of the Polish emigration (Hôtel Lambert circle); addressed to "Newton Hanson Esq. M.D., Viaduct House, Brighton" | Catalogue title only (Bourdeau `hard_targets.md` #2, never attempted; grep of all 392 target folders: none) | Private cipher held in the writer's papers | **Online, free** (WBC Poznań, publication 218680) | 1 | ~25–30 signs, ~350–450 tokens. Possibly English shorthand. Otherwise simple substitution | Short, so it may fall below unicity |
| 7 | **NLS Adv.MSS.80.3.48–50**, Dundas of Dundas accounts of legal expenses 1688–1701; 80.3.48 (18 ff.) "mainly written in cipher" | Dundas of Dundas family, through the Revolution of 1688 | Nothing in print found | Private accounts | Order | ~18 ff. cipher + scattered | Unknown. Probably a family substitution; accounts give numeric cribs | Small, cheap, plausible |
| 8 | **UCL Galton Papers GALTON/1/1/7/2/3** (diary notes c. Oct 1827 "partially written in cipher", **"no transcription"**) and **/2/2** (two notes in his cipher: "Anecdote of Bolivar", 16th-c. history) | Samuel Tertius Galton (1783–1844), Birmingham Quaker banker, father of Francis | Catalogue says no transcription for /2/3. The 1838–44 diaries (/2/5) **are** transcribed (/2/7) | Private | **Online** (Wellcome *Codebreakers* digitization. Rights flagged "in copyright") | ~5–10 | **Key survives: GALTON/1/1/7/2/1 (1829)**. A lookup, and the /2/7 typescript is a full-scale verifier | Low stakes, near-certain read. Best as a calibration case |
| 9 | **BL Add MS 4956**, William Courten (alias Charleton) diary 1698 in an interleaved *Apollo Anglicanus*, much of it in cipher; key on f. 66 (Madden), another key Sloane 4019 f. 79 | William Courten (1642–1702), collector whose cabinet went to Sloane and so to the BM | Digital Ark/Bargrave project describes the cipher as covering "business and personal exchanges" (snippet). No transcription found | Private diary | Order (BL imaging, post-2023 outage) | ~65 ff. | Key in volume | (a) weakened: Madden evidently read it |
| 10 | **Bodleian MS. Eng. misc. e. 675** (113 ff.) and e. 676, "Diary of Mifanwy Rhys, 1893, written partly in code" | Mifanwy Rhys, daughter of Sir John Rhŷs | No edition found | Private diary | Order (Weston Library) | ~20–50 coded passages? | Unknown; probably a schoolgirl substitution | Low stakes |

Not a new row: **MHS Ms. Sbd-133** (anonymous cipher diary, 1776–c.1799) already passes this test and is in the catalog as
`anonymous-cipher-diary-mhs`.

## Top 5

### 1. Miles Rock, "Keep Shut" book and shorthand notebook (Lehigh SC MS 0400.29.03, 0400.03)
- **Why it could matter.** Rock was "the only Lehigh student to serve in the Civil War". He was a signalman "temporarily attached to
  Judson Kilpatrick", "participated in one of Kilpatrick's famous raids in 1864", and later published a memoir of it in a Lancaster
  paper (Lehigh exhibit, SECONDARY, snippet). If that raid is the Kilpatrick–Dahlgren raid on Richmond (Feb–Mar 1864), the
  private shorthand of a participant bears on the Dahlgren papers controversy, the charge that the raid's orders were to burn Richmond
  and kill Jefferson Davis. **Which raid is unverified.** Kilpatrick also raided in Georgia in August 1864. A "Keep Shut" title on a
  private correspondence log suggests that matter was hidden from comrades.
- **(a)** The Omeka record is "metadata and page scans, with no transcription or description of content" (snippet). Not in
  Bourdeau's 392 targets, the catalog, or Cipherbrain results.
- **(b)** A private soldier's own book. There is no chancery and no recipient.
- **(c)** Page scans are on exhibits.lib.lehigh.edu (blocked here). Greg's browser should work.
- **(d)** Benn Pitman phonography. The writer's own 1861 *Reporter's Companion* is SC MS 0400.34, so the dialect of the system is pinned.
  Pitman-family shorthand is published and has living readers.
- **What would kill it.** The book is mostly longhand with little shorthand. The shorthand covers trivia, such as signal-practice drills. Or Lehigh holds a
  typescript transcription not mentioned on the exhibit. First step: open item 8433, count shorthand pages, and find the
  Feb–Mar 1864 leaves.

### 2. Montgomery C. Meigs's shorthand journals after 1861 (LOC MSS32540)
- **Why it could matter.** Meigs ran Union supply for the whole war and was a party to cabinet-level quarrels (Stanton, Lincoln, the
  Fort Pickens expedition). He founded Arlington National Cemetery and lost his son John Rodgers Meigs in October 1864. His journals were private, kept in
  shorthand, and run to 1892 (LOC "About this collection", PRIMARY catalogue, snippet).
- **(a)** The only edition is Wolff, *Capitol Builder: The Shorthand Journals of M. C. Meigs, 1853–1859, 1861* (2001), and its last chapter is an
  1861 epilogue (UW catalogue, SECONDARY). A review says Martin K. Mohr "worked through three volumes", years unknown
  (snippet). No transcription of 1862+ was found, and O'Harrow's 2016 biography has no notes, which makes its use of them unclear.
- **(b)** A private journal.
- **(c)** LOC digitized the collection (42,508 images). The journals are believed to be among them, not verified.
- **(d)** Pitman, but "sloppy". This needs a human Pitman reader or a trained HTR model. It is not a code problem.
- **What would kill it.** The journals stop or thin out after 1861 (the LOC description stresses aqueduct, Capitol and Pension Building). Or the
  Architect of the Capitol or the Senate Historical Office holds an unpublished full transcription (the likeliest kill; ask them). First step:
  find the journal volumes for 1862–65 in the LOC finding aid (ms006021).

### 3. Lord Milton's cipher account, 1738–39 (NLS MS.16962, keys MS.17605)
- **Why it could matter.** Andrew Fletcher, Lord Milton (1692–1766), was the Duke of Argyll's (Islay's) manager of Scottish
  patronage and Lord Justice Clerk through the 1745 rising. An account he kept in cipher, inverted at the back of an ordinary book,
  is very probably money he did not want his clerks to read: political payments, pensions or private debts.
- **(a)** NLS catalogue: "an account in cypher and two keys to cyphers" (snippet). No study of the cipher account was found, and the Roger Emerson
  search returned nothing on it. Not in Bourdeau (grep: none).
- **(b)** His own accounts. Most are "in his own hand" per the NLS series note.
  The correspondence ciphers in MS.17605 fail (b), because Islay's letters would have been deciphered by Milton, so they are excluded.
- **(c)** Not digitized as far as found. An NLS copy order of a few dozen pages is cheap relative to the others.
- **(d)** The keys are bound into the same volume, so this is a key lookup. The 1746 volume with keys at ff. 12v–14v and MS.16980 (1754) may
  carry more cipher entries. Ask NLS for a page count of cipher entries in each.
- **What would kill it.** The "account" is a few lines, or the cipher hides only domestic items such as wine and tailors.

### 4. Raversyde 1943 shorthand diary (Atlantikwall Raversyde, Ostend)
- **Why it could matter.** A diary from the Ostend area under German occupation, whose writer anticipated writing "burgemeester",
  "gemeenteraadslid" and "ontvangsten" often enough to list shorthand forms for them. That points to a council insider. Such a diary could
  record collaboration or resistance at municipal level (VRT NWS 2 Sept 2025, POPULAR, snippet).
- **(a)** As of Sept 2025, staff could "read only a few words". No later report was found in an October 2026 search.
- **(b)** A private diary.
- **(c)** Not online. Contact the provincial domain (Provincie West-Vlaanderen) and offer a transcription in exchange for scans.
- **(d)** Groote shorthand, a published Dutch system, with the writer's own partial key.
- **What would kill it.** A volunteer has already read it, since the appeal invited the public and AI tools. This is the main risk, so ask the museum first.

### 5. James Bonar's shorthand diary, 1775–1821 (NLS Acc.6123/1–7)
- **Why it could matter.** Forty-six years of private diary by a senior Excise lawyer in Enlightenment Edinburgh. He walked in on
  the Deacon Brodie gang robbing the Excise Office in March 1788 (Wikipedia, SECONDARY, snippet). He was RSE treasurer and a co-founder of the
  Edinburgh Subscription Library.
- **(a)** Weakened: the NLS catalogue's attribution is only "probably" Bonar. A c.1830 biography by his son (NLS, 1975 accession)
  "mostly draws on extracts from his diary", so the son could read it and some plaintext exists. Most of the diary was probably never extracted.
- **(b)** A private diary, apart from the son's extracts.
- **(c)** Order only. Seven volumes is the most expensive item here.
- **(d)** Unknown 18th-century shorthand. Identification against Byrom, Gurney, Mavor or Taylor is the first step, using the son's extracts as cribs.
- **What would kill it.** The son's biography quotes the substance of it. Or a personal system too abbreviated to verify.

## Rows 6–10 in one line each
- **6, Niedźwiecki 1855.** Free images, but only one page. First rule out Pitman or Taylor English shorthand (the English address).
  Rests on Bourdeau's note (SECONDARY).
- **7, Dundas accounts.** The cheapest key-less substitution target with numeric cribs (sums, dates). It has the merits of row 3 but no key.
- **8, S. T. Galton /2/2, /2/3.** Certain to read, because the key survives. The content is minor, so it is a calibration case for the cipher-diary method,
  and /2/5 against /2/7 gives a full verifier.
- **9, Courten 1698.** A key exists in the volume (Frederic Madden's), so someone has probably read it, and no edition was found. Only weakly novel.
- **10, Mifanwy Rhys 1893.** Novel and private, but probably a young woman's private code with low stakes.

## Checked and rejected

| Candidate | Why rejected |
|---|---|
| Yard → Manchester, 12 and 16 Oct 1699 (Beinecke, "undeciphered") | Fails (a) and (b): Bourdeau read both on 18 Sept 2026 (`targets/yard1699`). Also a chancery letter. |
| Esterházy box 636, Malsburg 1636–37, Waldeck 1744, Ilten, SP 87/24 del Puerto, SP 95/136 | Fail (b): ministerial or diplomatic. Ilten is interlined; Waldeck was attempted by Bourdeau. |
| Lord Milton's correspondence keys MS.17605 (letters 1737–55) | Fails (b): the recipient deciphered them. Only his private account (row 3) qualifies. |
| Jung-Stilling cipher diaries (UB Basel) | Fails (a): family transcripts exist (Schwinge); Benrath printed 1803 (Bourdeau note). |
| Ernest Rinzi journal (UIUC) | Fails (a): Gaffney broke it in 2017; only Italian gaps remain (Cipherbrain, snippet). |
| Erich Pieper diary; Emil Klein notebook; Siegfried Schwabl diary | Pieper and Klein solved by blog readers. Schwabl: Schmeh says the solution is known but unpublished. Crowded. |
| W. T. Prestwood diaries (NCSU) | Fails (a): Browder deciphered them. |
| Mary Crespigny 1791 (Bodleian MS. Eng. e. 3767) | Fails (a): deciphered; Clover's notes deposited 2024. |
| "Diary in cipher" 1734, Methodist Archives, Manchester | Almost certainly Wesley's Oxford diary, transcribed by Heitzenrater. Charles Wesley's is read (Newport). |
| Anne Lister | Crowd-transcribed by West Yorkshire Archive "Code Breakers". |
| Pepys, Byrd (all three), Shaw (Weintraub), Wittgenstein, Lichtenberg, Constant (2002 edition), Carnap, Treby (McKenzie 2021), Dickens (Dickens Code) | Published or deciphered. |
| Gödel Gabelsberger notebooks; Husserl | Professional transcription projects under way. |
| Rossette Davie interview 1951 (Weber State) | Crowded: "hundreds of offers", seven transcriptions accepted (2020). |
| York Castle Museum WWI shorthand diaries (1917–18) | Public appeal in 2014; crowd-exposed. Status not checked. |
| Great Lakes sailor's journal, 1867 | Fails (c): one page from Reddit; holder unknown. |
| "Encrypted diary by an unknown woman" (Schmeh 2018); Kansas library message | Single pages, crowd-exposed on Cipherbrain. |
| Dresden police-history Kassiber panels (museum-digital Sachsen) | Teaching panels, several made for training. Schmeh covered them in 2020. Panel 14-20 has its key shown. |
| Lady Gwendolen Cecil diary passage | Short and crowd-exposed (GCHQ, Schmeh 2019). |
| John Rodgers Meigs letters | Fails (a): Giunta transcribed about 40 shorthand letters. |
| Meigs journals 1853–59, 1861 | Fails (a): Wolff 2001. |
| Brougham family encrypted letter (UCL) | Fails (a): deciphered 2023. |
| Colonial clergy "short-writing" (Powers: "hundreds ... untranscribed") | A real class, but mostly sermon notes, and Bidwell's are solved. No specific high-value item identified. |
| AAS "Dayly Obseruation" shorthand diary | Fails (a): printed in AAS *Proceedings*. |
| Nelson war diaries (MSU) | Fails (a): transcriptions are in the collection. |
| Miles Franklin pocket diaries (SL NSW) | Fails (a): a volunteer reports translating the shorthand for 1926–36. |
| Wellcome MS.259/4 (1649 alchemical notes, "lines of an unresolved cypher") | Too short to verify a reading; private, but only a few lines. Kept as a lead, not a row. |
| Prize Papers (TNA HCA 30/32; c. 160,000 undelivered letters) | Ideal for (b), but no specific enciphered letter could be identified by search. Worth a dedicated catalogue sweep (search "cipher", "chiffre", "cijfer" in the Prize Papers portal) from an unblocked browser. |
| Commercial code telegrams in private papers | No specific undecoded holding with an identified codebook found in this pass. |
| Tolkien diaries | Fails (c): private estate. |

## Unverified claims

- Lehigh SC MS 0400.29.03: that the "Keep Shut" book is the item the exhibit calls the "Diary and Correspondence Log with Shorthand Entries",
  its page count, and which 1864 raid Rock rode on. All rest on exhibit snippets. The pages were not seen.
- Meigs: that the post-1861 journal volumes are in the digitized LOC set, and that no unpublished transcription exists (AOC or Senate Historical
  Office). Mohr's "three volumes" are unidentified.
- NLS MS.16962: the extent of the cipher account, and the 1746 volume's shelfmark. The NLS catalogue was seen only as snippets.
- Raversyde diary: that it remains unread after Sept 2025. No inventory number or page count was found.
- Bonar: the attribution ("probably") and the extent of the son's extracts.
- Niedźwiecki BK 02411: every detail comes from Bourdeau's `research/oldest/scan_2026-09-23/hard_targets.md` (SECONDARY). The Kórnik catalogue was not reached.
- Dundas Adv.MS.80.3.48: the snippets disagree ("mainly written in cipher, 1688–1699, 18 ff." against "some entries in cipher" at group level).
- Galton GALTON/1/1/7/2/2 is dated "mid 18th century" in one snippet, which cannot be right for S. T. Galton's cipher. Whether the Wellcome images are
  viewable online despite the "in copyright" flag is also unverified.
- Courten: whether Madden or the Digital Ark project produced a transcription that was not found.

## Sources (as reached, all via search snippets unless noted)

- Lehigh exhibit "Rediscovering Miles Rock": https://exhibits.lib.lehigh.edu/exhibits/show/miles-rock/civil-war ; items https://exhibits.lib.lehigh.edu/items/show/8433 , /40705 , /8421 , /8325 (SECONDARY / PRIMARY images)
- LOC Meigs Papers: https://www.loc.gov/collections/montgomery-c-meigs-papers/about-this-collection/ ; finding aid https://tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/ms006021/ms006021.pdf (PRIMARY catalogue); *Capitol Builder* https://search.library.wisc.edu/catalog/999920251502121 (SCHOLARLY)
- NLS Lord Milton: https://manuscripts.nls.uk/subjects/324 ; https://manuscripts.nls.uk/repositories/2/resources/18514 (PRIMARY catalogue)
- Raversyde: https://www.vrt.be/vrtnws/nl/2025/09/02/atlantikwall-raversyde-steno-schrift-dagboek-ontcijferen-oproep/ (POPULAR); https://brusselsmorning.com/ostends-raversyde-seeks-experts-for-1943-groote-diary/78378/ (POPULAR)
- Bonar: https://manuscripts.nls.uk/repositories/2/resources/9326 ; https://discovery.nationalarchives.gov.uk/details/r/N13767173 (PRIMARY catalogue); https://en.wikipedia.org/wiki/James_Bonar_(scholar) (SECONDARY)
- Niedźwiecki: https://www.wbc.poznan.pl/dlibra/publication/edition/218680/content (PRIMARY images, not reached); Bourdeau repo `research/oldest/scan_2026-09-23/hard_targets.md` (SECONDARY, read directly)
- Dundas: https://manuscripts.nls.uk/repositories/2/archival_objects/17151 (PRIMARY catalogue)
- Galton: https://content.www.wellcomecollection.org/works/wgcfp6nw ; https://preview.wellcomecollection.org/works/wx7j4pb4 ; https://content.www.wellcomecollection.org/works/eg7qr9py (PRIMARY catalogue)
- Courten: https://drc.usask.ca/projects/bargrave/public_msitem.php?id=27 (SCHOLARLY)
- Mifanwy Rhys: https://archives.bodleian.ox.ac.uk/repositories/2/archival_objects/190257 (PRIMARY catalogue)
- Rejections: https://scienceblogs.de/klausis-krypto-kolumne/2017/10/10/another-crypto-mystery-solved-tony-gaffney-has-broken-ernest-rinzis-encryption-code ; https://scienceblogs.de/klausis-krypto-kolumne/2018/11/16/an-encrypted-diary-written-by-an-austrian-servant-and-soldier/ ; https://www.historynewsnetwork.org/article/historians-struggle-to-understand-oral-history-wri ; https://mds.marshall.edu/sermonstudies/vol5/iss1/1 ; https://www.nationalarchives.gov.uk/professional-guidance-and-services/our-research-and-academic-collaboration/our-research-projects/collections-and-archives-research/the-prize-papers/ ; Bourdeau `targets/yard1699/NOTES.md` (read directly).
