from pathlib import Path
folders = Path("documents")
def load_documents(folders):
    files = folders.glob("*.txt")
    documents = []
    for f in files:
        documents.append({
            "source" : f.name,
            "text": f.read_text(),
            "tokens": tokenize(f.read_text())
        })

    return documents

def normalize_text(text):
    return text.strip().lower()

def tokenize(text):
    return normalize_text(text).split()

def process_query(query):
    return tokenize(query)

def doc_token(docs):
    for d in docs:
        d['tokens'] = tokenize(d['text'])

def calculate_score(query,doc_token):
    query_token = process_query(query)
    score = 0
    for q in query_token:
        if q in doc_token:
            score += 1
    return score

def rank_res(res):
    res.sort(key = lambda x : x['score'], reverse = True)
def retrieve(query,docs,k):
    res = []
    for d in docs:

        res.append({
            'source': d['source'],
            'score' : calculate_score(query,d['tokens'])
        })

    rank_res(res)
    return res[:k]

def display_res(res):
    print(res)