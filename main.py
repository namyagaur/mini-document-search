from pathlib import Path
folder = Path("documents")

print(folder)
print(folder.exists())
files = folder.glob("*.txt")

for file in files:
    with open(file,'r') as f:
        text = f.read()
    print(text)