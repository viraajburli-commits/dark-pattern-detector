# Data sheets

One sheet for each dataset the project uses. We follow a short version of the "Datasheets for Datasets" format (Gebru et al., 2021): where the data comes from, what is in it, how it was made, how we use it and what to watch out for.

---

## 1. Training data: Yada et al. (2022), from the 2019 crawl

| | |
|---|---|
| **Source** | [yamanalab/ec-darkpattern](https://github.com/yamanalab/ec-darkpattern), file `dataset/dataset.tsv` |
| **Paper** | Y. Yada et al., *Dark patterns in e-commerce: a dataset and its baseline evaluations*, IEEE BigData 2022 ([arXiv](https://arxiv.org/abs/2211.06543)) |
| **Built from** | Mathur et al., *Dark Patterns at Scale*, CSCW 2019: a 2019 crawl of about 11,000 popular English-language shopping sites |
| **Licence** | Apache-2.0 |
| **Size** | 2,356 rows. After we remove empty rows, duplicates and texts given both labels: 2,349 (1,178 dark patterns, 1,171 normal) |
| **Columns** | `page_id` (web page the text came from), `text`, `label` (1 = dark pattern), `Pattern Category` |
| **Trick types** | Scarcity 418, Social Proof 312, Urgency 210, Misdirection 195, Obstruction 27, Sneaking 12, Forced Action 4 |
| **How we use it** | 80/20 train/test split **by web page**. The 20% (470 texts from 250 pages) is the 2019 test set |
| **Watch out for** | Dark patterns here are short and full of numbers, so a model can partly learn the format instead of the meaning. Our surface-feature check gets F1 0.80 without reading a single word. Very few Obstruction, Sneaking and Forced Action examples |

---

## 2. Second test set: CogniGuard (2024)

| | |
|---|---|
| **Source** | [4darsh-Dev/CogniGaurd](https://github.com/4darsh-Dev/CogniGaurd), file `django-mlapi-backend/datasets/dp_final_dataset_may_4k.csv`, pinned to commit `09de733` |
| **Made by** | Adarsh Maurya and team, 2024, for India's *Dark Patterns Buster* hackathon |
| **Licence** | MIT |
| **Size** | 4,491 rows. 1,927 also appear in the 2019 data, so we remove them, plus duplicates and conflicts. **2,195 new rows** (1,761 dark patterns, 434 normal) in 1,393 near-copy groups |
| **Columns** | `Title` (the text), `Category` (trick type, or "Not Dark Pattern") |
| **Trick types (new rows)** | Urgency 562, Social Proof 361, Scarcity 309, Forced Action 231, Misdirection 196, Sneaking 74, Obstruction 28 |
| **Settings** | Mostly Indian shopping, travel, food-delivery, subscription and app text, plus cookie and privacy prompts |
| **How we use it** | (a) A test of the 2019 model on a completely separate dataset. (b) Half of it is added to training and the model is tested on the other half, over 5 random splits by near-copy group. (c) All of it is added to training for the live-site test and the demo |
| **Watch out for** | Many rows look hand-written or generated, not copied from live sites, and many are templated near-copies ("Your subscription is about to expire Renew now to continue" / "... to keep accessing"). We group texts with the same first four words so near-copies never sit on both sides of a split. 80% of rows are tricks, so F1 is misleading and we use balanced accuracy |

---

## 3. Live-site test set (ours): `live_sites_2026.csv`

| | |
|---|---|
| **What it is** | Short text snippets copied from real, public web pages on **15 November 2026** |
| **Sites (15)** | Booking.com, Agoda, Expedia, Hotels.com, Priceline, Walmart, Macy's, Temu, eBay, Fashion Nova, Steam, StubHub, Ticketmaster, GetYourGuide, Viator |
| **Pages** | Search results (72), hotel pages (23), product pages (21), home pages (12), and city, event, activity and game pages |
| **Size** | 176 snippets: 37 dark patterns, 139 normal. Batch 1: 146 (29 tricks). Batch 2: 30 (8 tricks). 2 snippets also appear in the training data and are removed before testing, leaving 174 |
| **Trick types** | Scarcity 15, Social Proof 11, Urgency 10, Misdirection 1 |
| **Columns** | `text`, `label` (1 = dark pattern), `category`, `source_site`, `page_type`, `date_collected`, `batch` |
| **Labelling** | Each snippet labelled with the 2019 dataset's categories (Mathur et al.'s taxonomy). One labeller; no second person has checked the labels |
| **Collection** | Collected with AI assistance through a normal browser, reading public pages only. Amazon was skipped because its terms forbid automated agents. Pages behind a login or bot check (Shein, Etsy, Best Buy, most of Temu) were not used. No reviews, names, accounts or other personal information were copied |
| **Licence** | Short excerpts quoted for non-commercial research and education. The text belongs to the original websites |
| **How we use it** | Held-out test only. It is never used for training or for choosing settings or the threshold |
| **Watch out for** | Small (35 tricks after removing overlaps), so 95% confidence intervals are about ±0.09 in balanced accuracy. Hotel and travel sites are over-represented because that is where we found the most tricks. Some templates repeat across sites ("We have 3 left at this price"). Text only: visual tricks such as countdown timers drawn as images are not captured |
