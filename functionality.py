import pandas as pd
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

data = pd.read_csv("spells_without_duplicates.csv")

documents = [Document(page_content=str(description), metadata={'row_id': idx})
                 for idx, description in data['Description'].items()]

db = FAISS.from_documents(documents,
                      HuggingFaceEmbeddings(model_name='BAAI/bge-base-en-v1.5'))

def IR(db, query, k):

    retrieved_docs_direct = db.similarity_search(query, k=k)

    results = ""

    for doc in retrieved_docs_direct:
        row = doc.metadata.get('row_id')

        results += "## " + str(data["Name"][row]) + "\n\n"
        results += f"**Class**: {data['Class'][row]}\n\n**Level**: {data['Level'][row]}\n\n**School**: {data['School'][row]}\n\n**Duration**: {data['Duration'][row]}\n\n**Casting time**: {data['Casting.time'][row]}\n\n**Components**: {data['Components'][row]}\n\n"

        if data["Material"][row] != "NONE":
            results += f"**Material**: {data['Material'][row]}\n\n"

        if data["Ritual"][row] == "Yes":
            results += "**Ritual**\n\n"

        results += "**Description**:\n\n"
        results += str(data["Description"][row]) + "\n\n"
        results += "---\n\n"

    return results

