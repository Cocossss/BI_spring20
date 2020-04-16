import matplotlib.pyplot as plt
import seaborn as sns

f = open('/media/cocos/E666-2771/feature_count.txt', 'r')

c = []
for line in f:
    list = line.split()
    if len(list) == 2:
        c.append(int(line.split()[1]))

print(len(c))
f.close()

s = sns.distplot(c)

plt.show()
