+++
title = "Coded telegrams of John A. Macdonald, 1873–1891 (solved 2021) — calibration case"
slug = "macdonald-canadian-pm-telegrams"
kind = "cipher"
era = "1873, 1879, 1881–1891"
origin = "Canada (Prime Minister John A. Macdonald and his circle)"
language = "English"
status = "solved"
confidence = "high"
digitized = "https://docs.google.com/spreadsheets/d/11pTqYziadc-C-Qvfzzqve-0Ho_ifUOAdGVIhZy5-lFo/edit#gid=0"
tags = ["calibration", "solved", "telegram", "codebook", "Slater-code", "additive", "brute-force", "19th-century", "Library-and-Archives-Canada", "Cipherbrain"]

[scores]
mystery = 1
material = 5
solvable = 5
compute = 5
verifiable = 5
crowding = 5
+++

# Coded telegrams of John A. Macdonald, 1873–1891 (solved 2021) — calibration case

## What it is
More than a hundred coded messages, mostly telegrams, sent by or around John A. Macdonald, Canada's first prime minister (1867–73, 1878–91). They date from 1873, 1879 and 1881–1891 and are held at Library and Archives Canada (LAC). The Canadian government used Robert Slater's *Telegraphic Code, to Ensure Secresy in the Transmission of Telegrams* (1870), a public codebook of about 25,000 numbered English words. The telegrams consist of real English words in senseless order ("damnation", "pray", "fever"…). The sender looked up each plaintext word's number, added a secret key, and sent the word at the new number.

## What is unsolved
Nothing material. The entry is here as a calibration case: a known public codebook, a secret additive, and a corpus nobody had looked at. A handful of short messages were left over; George Lasry proposed readings for several of them, and Brown judged those readings correct.

## What survives
The originals at LAC (MIKAN record links in Brown's list), scanned online. Matthew Brown compiled a public spreadsheet listing every cryptogram with transcription, archive link and, where known, plaintext. Slater's codebook is on Google Books and the Internet Archive.

## Prior attempts and current consensus
Matthew Brown (England) read in Slater's preface that the Canadian government had used the code, then searched LAC and found the telegrams. Klaus Schmeh published his solution on Cipherbrain on 30 June 2021. Brown assumed a simple additive and tried all ~24,999 keys on each telegram, ranking candidate plaintexts by the frequency rank of their words. In his words, it needs "about 10 or more words to arrive at the correct solution." The keys turned out to be 250, 50 or 500 in 1873. In 1881–84 they were mostly multiples of 100 (a page of Slater holds 100 words); one message to Tupper used 365. From about 1885–88 a base plus the day of the month was used (e.g. 1234 + date, December 1887). At least one subtractive key was used (−200, 15 June 1886, to J. W. Trutch). Example decode (key 250): "PRIVATE CRITICAL POINT CHANCES AGAINST SUCCESS BUT IF NEGOTIATION INTERRUPTED…". Lasry used word-bigram scoring to propose readings for four leftovers (e.g. "cant do any more", "tell boyd to run"), and Brown confirmed them as the only grammatical candidates in his top 100. No formal paper was found; the solve is documented on Cipherbrain, in Brown's spreadsheet, and in Tomokiyo's Cryptiana.

## What a solution would have to do
Met: a single short key per telegram, from a key space of ~25,000, turns each telegram into grammatical English that fits Macdonald's correspondence. The keys follow a pattern across years (round hundreds, then base + date). That pattern is independent confirmation, because a key schedule that makes administrative sense is very unlikely to be an artefact of the scoring.

## Why the scores
Scored as they would have stood before 2021, except mystery.
- mystery 1 today. Before 2021 it would have been 2: unread political telegrams of a national founder, with some historical interest (the 1873 Pacific Scandal year, the 1885 rebellion era), but not a known open question.
- material 5: over a hundred telegrams, digitized at LAC, codebook public.
- solvable 5: a government using a published commercial code, the code named in the codebook's own preface.
- compute 5: the textbook case. It is a large codebook, but the codebook is known and the secret is a one-parameter additive; exhaustive search with a word-frequency score is all it takes. This is why "codebook" alone should not lower compute: what matters is whether the codebook is in hand.
- verifiable 5: grammatical English from a 1-in-25,000 key, with keys forming a sensible schedule.
- crowding 5: untouched before Brown found it.
- compute mode (retrospective): ENUMERATE (24,999 additive keys × codebook lookup) · verifier MECHANICAL · space ENUMERABLE · signal YES · fit HIGH.
- Calibration point: as with Mary Stuart, the binding step was finding the corpus. Here the lead came from a codebook's preface naming its users. Prefaces and advertisements of 19th-century commercial codebooks are a cheap way to locate government users whose archived traffic may be unread.

## Sources
- PRIMARY — Library and Archives Canada, Macdonald telegrams, e.g. record 510721 (no. 10 on Brown's list). https://www.bac-lac.gc.ca/eng/CollectionSearch/Pages/record.aspx?app=fonandcol&IdNumber=510721
- PRIMARY — Robert Slater, *Telegraphic Code, to Ensure Secresy in the Transmission of Telegrams* (1870), Google Books. https://books.google.com/books/about/Telegraphic_Code_to_Ensure_Secresy_in_th.html?id=MJYBAAAAQAAJ
- CLAIMANT — Matthew Brown, list of all cryptograms with transcription, archive link and plaintext (Google Sheets). https://docs.google.com/spreadsheets/d/11pTqYziadc-C-Qvfzzqve-0Ho_ifUOAdGVIhZy5-lFo/edit#gid=0
- POPULAR — Klaus Schmeh, "Wie Matthew Brown die verschlüsselten Telegramme des ersten kanadischen Premierministers löste," Cipherbrain, 30 June 2021 (method, examples, keys; comments by Brown and Lasry). https://scienceblogs.de/klausis-krypto-kolumne/2021/06/30/wie-matthew-brown-die-verschluesselten-telegramme-des-ersten-kanadischen-premierministers-loeste/
- SECONDARY — Satoshi Tomokiyo, Cryptiana, codebreaking article, section "Slater's Code" (key schedule by year, subtractive key, Lasry's follow-up). https://cryptiana.web.fc2.com/code/codebreaking.htm
- SECONDARY — Satoshi Tomokiyo, Cryptiana, "Unsolved Historical Ciphers," "Telegrams of First Canadian Prime Minister, John A. Macdonald" (marked Solved). https://cryptiana.web.fc2.com/code/unsolved.htm

## Unverified claims
- The exact number of telegrams found and the number left unread; sources say "more than a hundred" and "most."
- Whether Brown or Lasry published the work formally (journal or HistoCrypt). A search found nothing.
- Whether the spreadsheet is still publicly accessible; its URL is taken from Cipherbrain and was not opened.
- The shorthand words over some code words in one unsolved telegram, mentioned by Schmeh; their reading is unknown.
