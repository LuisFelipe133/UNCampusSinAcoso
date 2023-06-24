from typing import Generic,TypeVar
T = TypeVar("T")

class NodeTree(Generic[T]):
    data:T = None 
    left = None
    right = None

    def __init__(self,data:T):
        self.data=data