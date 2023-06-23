from typing import Generic,TypeVar
T = TypeVar("T")

class NodeList(Generic[T]):
    data:T = None
    next = None
    prev = None
    
    def __init__(self,data:T):
        self.data=data
        self.next= None
        self.prev = None
