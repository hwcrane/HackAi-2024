from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

data = open('./documents/CFR/CFR-2023-title14-vol1.htm').read().split('\n\n')
print(len(data))

# Sentences are encoded by calling model.encode()
embedding = model.encode(data, convert_to_tensor=True)
question = model.encode("What type of microphone must be installed to meet the recording requirements of paragraph (a)(2) of 14 CFR 23.1457", convert_to_tensor=True)

cosine_scores = util.cos_sim(embedding, question)

print(data[cosine_scores.argmax()])


