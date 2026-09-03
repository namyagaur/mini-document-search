from pathlib import Path
folder = Path("documents")

print(folder)
print(folder.exists())

print(folder.glob("*.txt"))