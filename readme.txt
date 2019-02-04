Installation
$ virtualenv -p python3.6 venv
$ source venv/bin/activate
$ pip install Pillow
$ python main.py

Change main for your particular purpose

$ python main.py

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