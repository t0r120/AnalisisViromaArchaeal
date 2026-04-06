# Archaeal Virome Analysis
 
> Systematic literature retrieval from PubMed using the NCBI Entrez API · Python · BioPython · In active development
 
![Python](https://img.shields.io/badge/Python-3.8+-blue) ![BioPython](https://img.shields.io/badge/BioPython-latest-green) ![Status](https://img.shields.io/badge/status-in%20development-yellow)
 
---
 
## Overview
 
A bibliometric retrieval tool for scientific literature on archaeal viruses — one of the least studied branches of the virosphere. The tool queries PubMed using curated MeSH terms and taxonomic synonyms, downloads original research articles in MEDLINE format, and stores them locally for downstream analysis.
 
---
 
## Motivation
 
Knowledge on archaeal viromes is fragmented across databases, constrained by isolation challenges, and limited by an evolving taxonomy. This project automates the retrieval pipeline so researchers can focus on analysis instead of manual literature searches.
 
---
 
## How it works
 
| Step | Description |
|------|-------------|
| 1 · Query | Curated boolean query with MeSH terms and taxonomic synonyms sent to PubMed Esearch |
| 2 · Retrieve | Article IDs fetched in batches of 100 via Efetch, respecting API rate limits |
| 3 · Store | Records saved in MEDLINE format to a configurable output directory via environment variables |
 
---
 
## Requirements
 
- Python 3.8+
- biopython
- NCBI API key (free at [ncbi.nlm.nih.gov/account](https://www.ncbi.nlm.nih.gov/account/))
 
---
 
## Setup
 
```bash
# 1. Clone the repo
git clone https://github.com/t0r120/Analisis-del-viroma-arqueal
 
# 2. Install dependencies
pip install biopython
 
# 3. Set environment variables
export NCBI_API_KEY=your_key_here
export MY_EMAIL=your_email@example.com
export VIRUS_DIR_PATH=/path/to/output/
 
# 4. Run
python main.py
```
 
---
 
## Roadmap
 
- [ ] Bibliometric analysis (publication trends, top authors, journals)
- [ ] Keyword co-occurrence network
- [ ] Export to CSV / structured formats
- [ ] CLI interface with configurable filters
 
---
 
*Built by a biology student turned software engineer · contributions welcome*
