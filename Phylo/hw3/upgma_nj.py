from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO
from ete3 import Tree
import matplotlib.pyplot as plt

aln = AlignIO.read('SUP35_aln.best.fasta', 'fasta') # extracting alignment
calc = DistanceCalculator('identity')
dm = calc.get_distance(aln) # creating distance matrix
constructor_upgma = DistanceTreeConstructor(calc, 'upgma')
constructor_nj = DistanceTreeConstructor(calc, 'nj')
tree_upgma = constructor_upgma.upgma(dm)
tree_nj = constructor_nj.nj(dm)
plt.rcParams.update({'font.size': 15, 'lines.linewidth': 3})
plt.rcParams['figure.figsize'] = 20, 20 # size of picture
Phylo.draw(tree_upgma, do_show=False)
plt.axis('off') # remove coordinates
#plt.show()
plt.savefig('upgma.png')

plt.rcParams.update({'font.size': 15, 'lines.linewidth': 3})
plt.rcParams['figure.figsize'] = 20, 20 # size of picture
Phylo.draw(tree_upgma, do_show=False)
plt.axis('off') # remove coordinates
#plt.show()
plt.savefig('nj.png')

