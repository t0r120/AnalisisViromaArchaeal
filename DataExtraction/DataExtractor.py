#-- Import
from Bio import Entrez
import os
import time

main_directory = os.getenv("VIRUS_DIR_PATH")
ouput_file = os.path().join(main_directory, "pubmed_out.txt")

#--- Requerimientos básicos de la API de pubmed (NCBI)
Entrez.api_key = os.getenv("NCBI_API_KEY")
Entrez.email = os.getenv("MY_EMAIL")
os.makedirs(main_directory, exist_ok=True)



# -- Consulta
term = '''("archaeal virus"[Title/Abstract] OR  "archaeal viruses"[Title/Abstract] OR  "Archaea virus"[Title/Abstract] OR  "archaea viruses"[Title/Abstract] OR  "archaeoviruses"[Title/Abstract] OR  ("Archaea"[MeSH Terms] AND "Viruses"[MeSH Terms] AND (archaea*[Title/Abstract] AND virus*[Title/Abstract]))) 
AND "journal article"[pt] NOT (review[pt] OR editorial[pt] OR letter[pt] OR news[pt])'''


#-- Busqueda (Esearch)

handle = Entrez.esearch(db="Pubmed", term = term  , retmax=1000) # Obtener solo lo 10 primeros registros 
record = Entrez.read(handle)
id_list = record["IdList"]
print(f"Total de artículos encontrados: {len(id_list)}")

#-- Descarga de consulta (Efetch) en bloques de 100

batch_size =  100


