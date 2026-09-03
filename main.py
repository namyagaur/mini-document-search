from pathlib import Path

folders = Path('documents')
files = folders.glob('*.txt')

def load_doc(p):
    print(Path(p).read_text())
    
for file in files:
    load_doc(file)
