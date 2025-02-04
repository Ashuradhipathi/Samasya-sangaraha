# Steps to run

```python 
pip install uv

uv venv --python 3.12.1

uv pip install  -r app/docs/requirements.txt

```

# Contents

## app

It contains all the logic of the code.

### mongo.py

It contaisn the creation of mongo clinet and function to retrieve values

### rag.py

It contains the helper functions for RAG

### pages
It contains the streamlit pages

### svagatam.py
It is the home page of the website

### create_index.py 
When the python file is run, it creates atlas vector search index in MongoDB 
