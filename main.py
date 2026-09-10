from pathlib import Path

folders = Path('documents')
files = folders.glob('*.txt')

documents = []
for file in files:
    documents.append({
        "source":file.name,
        "text": file.read_text()

    })

def tokenize(text):
    res = text.strip()
    text = res.lower()
    return text.split()


for d in documents:
    d["tokens"] = tokenize(d["text"])

def process_query(query):
    return query.strip().lower().split()

query = input("Enter your query")

print(process_query(query))

