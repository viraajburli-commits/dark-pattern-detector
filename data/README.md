# Data

The two public datasets are downloaded automatically by the notebook and are not stored in this repo. The live-site test set is stored here.

| Dataset | Used for | Rows we use | Licence |
|---|---|---|---|
| **Yada et al. (2022)**, [yamanalab/ec-darkpattern](https://github.com/yamanalab/ec-darkpattern), built from Mathur et al.'s 2019 crawl of 11K shopping sites | Training and the main test set (split by web page) | 2,349 (1,178 dark patterns, 1,171 normal) | Apache-2.0 |
| **CogniGuard dataset (2024)**, [4darsh-Dev/CogniGaurd](https://github.com/4darsh-Dev/CogniGaurd), file `django-mlapi-backend/datasets/dp_final_dataset_may_4k.csv` at commit `09de733` | Second, independent test set ("does it still work?") and the improvement experiment | 2,195 after removing the 1,927 rows copied from the 2019 data and duplicates (1,761 dark patterns, 434 normal) | MIT |
| **Live-site test set (ours)**, `live_sites_2026.csv` | Third test set: real text from current websites | 176 snippets (37 tricks, 139 normal) from 15 sites in two batches; 174 used after removing 2 that appear in the training data | Short excerpts for research |

**Caveat on the CogniGuard data:** many of its new rows look written by hand or generated, not copied from live sites, and many are templated near-copies of each other. We group near-copies (same first four words) so they never appear on both sides of a train/test split. No personal information is used.

**Live-site test set:** copied on 15 November 2026 from public product, search, hotel, event and game pages on Booking.com, Agoda, Expedia, Hotels.com, Priceline, Walmart, Macy's, Temu, eBay, Fashion Nova, Steam, StubHub, Ticketmaster, GetYourGuide and Viator. Collected with AI assistance and labelled by one labeller using the 2019 dataset's categories. Columns: `text`, `label` (1 = dark pattern), `category`, `source_site`, `page_type`, `date_collected`, `batch`. Amazon was skipped because its terms forbid automated agents, and pages behind a login or bot check (Shein, Etsy, Best Buy, most of Temu) were not used.
