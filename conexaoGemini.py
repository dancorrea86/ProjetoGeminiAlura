#Importações e configurações iniciais
import numpy as np
import pandas as pd
import google.generativeai as genai
import json
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

configure()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)


#Listando os modelos disponíveis
# for m in genai.list_models():
#   if 'embedContent' in m.supported_generation_methods:
#     print(m.name)


with open('md_data.json', encoding="utf8") as f:
    data = json.load(f)

documentos = []

for i in range(len(data)):
   documento = {
      "Título": (data[i]["titulo"]),
      "Conteúdo": (data[i]["conteudo"]),
   }

   documentos.append(documento)

df = pd.DataFrame(documentos)
df.columns = ["Titulo", "Conteudo"]


model = "models/embedding-001"

def embed_fn(title, text):
    return genai.embed_content(model=model,
                                    content=text,
                                    title=title,
                                    task_type="RETRIEVAL_DOCUMENT")["embedding"]

df["Embeddings"] = df.apply(lambda row: embed_fn(row["Titulo"], row["Conteudo"]), axis=1)






def gerar_e_buscar_consulta(consulta):
    model = "models/embedding-001"
    embedding_da_consulta = genai.embed_content(model=model,
                                    content=consulta,
                                    task_type="RETRIEVAL_QUERY")["embedding"]

    produtos_escalares = np.dot(np.stack(df["Embeddings"]), embedding_da_consulta)

    indice = np.argmax(produtos_escalares)
    return df.iloc[indice]["Conteudo"]



# trecho = gerar_e_buscar_consulta(consulta, df, model)
# print(trecho)



