from pathlib import Path

folders = Path('documents')
files = folders.glob('*.txt')

documents = []
for file in files:
    documents.append({
        "source":file.name,
        "text": file.read_text()

    })

# print(documents)

def normalize_text(text):
    res = text.strip()
    text = res.lower()

    return text

for d in documents:
    d["text"] = normalize_text(d["text"])

print(documents)