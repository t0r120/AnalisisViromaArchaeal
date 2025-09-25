#-- Import
from Bio import Entrez
import os
#--- Requerimientos básicos de la API de pubmed (NCBI)
Entrez.api_key = os.getenv("NCBI_API_KEY")
Entrez.email = os.getenv("MY_EMAIL")

handle = Entrez.einfo(db="Pubmed")
record = Entrez.read(handle)
print(record)

