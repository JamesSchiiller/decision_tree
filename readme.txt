$ virtualenv -p python3.6 venv
$ source venv/bin/activate

$ pip install Pillow

$ python 

>>> tree = decision_tree.buildtree(decision_tree.my_data)
<decision_tree.decisionnode object at 0x10554e048>

>>> decision_tree.classify(['(direct)', 'USA', 'yes', 5], tree)
{'Basic': 4}

>>> decision_tree.drawtree(tree, jpeg='treeview.jpg')
treeview.jpg

>>> decision_tree.printtree(tree)
0:google?
3:21?
{'Premium': 3}
  T-> None
2:no?
{'None': 1}
    T-> None
{'Basic': 1}
    F-> None
  F-> None
T-> None
0:slashdot?
{'None': 3}
  T-> None
2:yes?
{'Basic': 4}
    T-> None
3:21?
{'Basic': 1}
      T-> None
{'None': 3}
      F-> None
    F-> None
  F-> None
F-> None

References
Programming Collective Intelligence, pp. 142-158, Toby Segaran