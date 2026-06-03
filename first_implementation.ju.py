# %%
import pandas as pd

data = pd.read_csv("spells_without_duplicates.csv")

# %%
data.columns

# %%
data

# %%
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

documents = [Document(page_content=str(description), metadata={'row_id': idx}) for idx, description in data['Description'].items()]

db = FAISS.from_documents(documents,
                          HuggingFaceEmbeddings(model_name='BAAI/bge-base-en-v1.5'))
# %%
def IR(query, k):
  retrieved_docs_direct = db.similarity_search(query, k=k)

  results = ""

  for doc in retrieved_docs_direct:
    row = doc.metadata.get('row_id')

    results += "Spell name: "
    results += str(data["Name"][row]) + "\n"
    results += 20*"-" + "\n"
    results += f"Class: {data['Class'][row]}\nLevel: {data['Level'][row]}\nSchool: {data['School'][row]}\nDuration: {data['Duration'][row]}\nCasting time: {data['Casting.time'][row]}\nComponents: {data['Components'][row]}\n"

    if data["Material"][row] != "NONE":
        results += f"Material: {data['Material'][row]}\n"

    if data["Ritual"][row] == "Yes":
        results += "Ritual\n"

    results += 20*"-" + "\n"
    results += "Description:\n"
    results += str(data["Description"][row]) + "\n\n"

  return results

# %% 

query = "I want to stop time"
k = 4

print(IR(query, k))


# TODO:
#
# * Enable filtering before the query
# * Make it into Shiny

