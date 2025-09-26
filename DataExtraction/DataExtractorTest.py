#-- Import
from Bio import Entrez
import os
import time
#--- Requerimientos básicos de la API de pubmed (NCBI)
Entrez.api_key = os.getenv("NCBI_API_KEY")
Entrez.email = os.getenv("MY_EMAIL")

# -- Primer prueba -- 
# -- Buscando las publicaciones relacionadas a la busqueda (Esearch) -- 

# -- Consulta
term = '''("archaeal virus"[Title/Abstract] OR  "archaeal viruses"[Title/Abstract] OR  "Archaea virus"[Title/Abstract] OR  "archaea viruses"[Title/Abstract] OR  "archaeoviruses"[Title/Abstract] OR  ("Archaea"[MeSH Terms] AND "Viruses"[MeSH Terms] AND (archaea*[Title/Abstract] AND virus*[Title/Abstract]))) 
AND "journal article"[pt] NOT (review[pt] OR editorial[pt] OR letter[pt] OR news[pt])'''
handle = Entrez.esearch(db="Pubmed", term = term  , retmax=10) # Obtener solo lo 10 primeros registros 
record = Entrez.read(handle)

# -> Numero de publicaciones -> 512
# -- Obteniendo un resumen de los datos de cada Id relacionado a las publicaciones (Esummary) --

#for id in record['IdList']:
#    handle_id = Entrez.esummary(db = "Pubmed", term = term,  id = id)
#    record_id = Entrez.read(handle_id)
#    time.sleep(3) # -> Tiempo de pausa impuesta por NCBI  
#    print(record_id)

# -- Descargando los registros de pubmed con Efetch -- 
for id in record['IdList']:
    handle_fetch  = Entrez.efetch(db = "Pubmed", id = id, rettype = "uilist", retmode = "text")
    record_fetch = Entrez.read(handle_fetch)
    time.sleep(3)





