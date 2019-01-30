import decision_tree

def train():
  tree = decision_tree.buildtree(decision_tree.my_data)
  decision_tree.savetree(tree)

def perform(x):
  tree = decision_tree.loadtree()
  prediction = decision_tree.classify(x, tree)
  print(prediction)

def drawtree():
  tree = decision_tree.loadtree()
  decision_tree.drawtree(tree, jpeg='treeview.jpg')
  decision_tree.printtree(tree)
  print("treeview.jpg")

# train()
perform(['(direct)', 'USA', 'yes', 5])
# drawtree()