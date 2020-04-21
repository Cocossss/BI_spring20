from gtfparse import read_gtf
import pysam
from BCBio import GFF
import seaborn as sns
import matplotlib.pyplot as plt

file = './data/genes.gtf'

db = read_gtf(file)
id = db['gene_id']
start = db['start']
end = db['end']

lens = {}
for i in range(len(id)):
    lens[id[i]] = end[i] - start[i]


features = {}
f = open('feature_count.txt')
for line in f:
    list = line.split()
    features[list[0]] = int(list[1])
f.close()

scale = 0
for k, v in lens.items():
    features[k] /= v
    scale += features[k]

scale /= 1000000

print(scale)

for k, v in features.items():
    features[k] /= scale

cut = []
num=0
for k, v in features.items():
    if v >= 5:
        cut.append(v)
        num += 1

print(num)
print(num/len(lens)*100, '%')
s = sns.distplot([cut])
plt.show()

