- Make sure embeddings are <= 600 dimensions
- Change text splitter to something more optimised
- Parse the LLM responses, and try to ensure it's limited to multiple choice answers
- Load other documents into vector database
- Add logic to load vector database and take the first n relevant documents and prepend them to the question


- 
    - Load Documents
    - Split Loaded Text
    - Embed and Store Splits
    - Save Vector database to a file
- 
    - Load Vector database
    - Load Quiz CSV
    - For each question
        - Load relevant documents
        - Put in front of LLM query
        - Parsing the answer
        - Fill the CSV
    - Save CSV