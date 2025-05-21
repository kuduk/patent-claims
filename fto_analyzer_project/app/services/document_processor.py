from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List, Dict
import os

def process_and_chunk(file_path: str, batch: bool = False) -> List[Dict]:
    """
    Read a text file (or batch of files) and split into semantic chunks.
    Returns a list of dicts with keys: id, content, metadata.
    """
    docs: List[Dict] = []
    paths = [file_path]
    if batch and os.path.isdir(file_path):
        for fname in os.listdir(file_path):
            if fname.lower().endswith(".txt"):
                paths.append(os.path.join(file_path, fname))

    for path in paths:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        metadata = {"source": os.path.basename(path)}
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_text(text)
        for i, chunk in enumerate(chunks):
            docs.append({
                "id": f"{os.path.basename(path)}_chunk_{i}",
                "content": chunk,
                "metadata": metadata
            })
    return docs
