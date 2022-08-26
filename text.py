a=[1,1,3,4,5,6,7]
a = "1231/123"
# print(a.split("/"))
from word import *
a = WordPOS("13123","123123")
# print(POS.key(a))
class A:
    def __init__(self) -> None:
        self._a = 1
class B(A):
    def __init__(self) -> None:
        super().__init__()
        print(self._a)

B()
from utils import *
D = dict()
D["a"]=1
dict_to_json(D,"aaa.json")
