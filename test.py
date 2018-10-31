import h5py
import numpy as np

f = h5py.File('elmo_token_embeddings.hdf5')
key = ""
for k in f.keys():
    key = k

f2=open("embedding.tsv",encoding="utf-8",mode="w")

d = f[key]
index = 1
word1=None
word2=None
for k in d:
    if index==189:
        word1=k
    if index==267:
        word2=k
    if index==1000:
        break
    for i in k:
        f2.write(str(i))
        f2.write("\t")
    f2.write("\n")
    index+=1


from sklearn.manifold import TSNE
output = TSNE(n_components=2).fit_transform(np.array([word1,word2]))
print(output)
print((output[0][0]-output[1][0])*(output[0][0]-output[1][0])
      +(output[0][1]-output[1][1])*(output[0][1]-output[1][1]))
