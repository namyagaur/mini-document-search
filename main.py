from pathlib import Path
folder = Path("documents")

print(folder)
print(folder.exists())
files = folder.glob("*.txt")

for file in files:
    print(file.read_text())