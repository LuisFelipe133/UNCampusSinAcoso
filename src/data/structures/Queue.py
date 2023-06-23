from .LinkedList import LinkedList
from typing import Generic, TypeVar
T = TypeVar("T")

class Queue(LinkedList):
    def __init__(self):
        super().__init__
    
    def enqueue(self,data:T):
        print(data)