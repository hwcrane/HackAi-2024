from sentence_transformers import SentenceTransformer, util
import torch
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

data = open('./documents/CFR/CFR-2023-title14-vol1.htm').read().split('\n')
print(len(data))

# Sentences are encoded by calling model.encode()
embedding = model.encode(data, convert_to_tensor=True)
question = model.encode("What type of microphone must be installed to meet the recording requirements of paragraph (a)(2) of 14 CFR 23.1457", convert_to_tensor=True)

cosine_scores = [(i, e) for i, e in enumerate(util.cos_sim(embedding, question))]

best = sorted(cosine_scores, key=lambda x: x[1], reverse=True)[:5]
for i, _ in best:
    print(data[i])






