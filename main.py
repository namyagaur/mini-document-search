from pathlib import Path

folders = Path('documents')
files = folders.glob('*.txt')

documents = []
for file in files:
    documents.append({
        "source":file.name,
        "text": file.read_text()

    })

print(documents)