library('ape')
tree1 <- read.tree('./data/life.txt')

# weird aesthetics, but i like it
plot(tree1, cex=0.3, edge.color = 'green', tip.color = 'blue')

is.rooted(tree1) #TRUE
tree1 <- root(tree1, 1)
is.rooted(tree1) #FALSE
plot(tree1, cex=0.3, edge.color = 'green', tip.color = 'blue')

s <- '(((A, B), (C, D)), E);'
tree2 <- read.tree(text=s)
plot(tree2, edge.color = 'green', tip.color = 'blue')
