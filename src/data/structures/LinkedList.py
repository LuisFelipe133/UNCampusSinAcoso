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

class LinkedList(Generic[T]):
    head:NodeList 
    tail:NodeList
    index:int
    
    #**************************** constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.index=0
    #**************************** metodos de verificación y atributos
    def isEmpty(self):
        return self.index==0
    def len(self):
        return self.index
     #**************************** Insertar o eliminar
    def pushFront(self,data:T):
        dataNode = NodeList(data)
        if self.isEmpty():
            self.head = dataNode = self.tail
        else:
           dataNode.next= self.head 
           self.head.prev= dataNode
           self.head = dataNode
        self.index+=1
    
    def pushBack(self,data:T):
        dataNode = NodeList(data)
        if self.head==None:
            self.head = dataNode
            self.tail = dataNode
        else:
            self.tail.next = dataNode
            dataNode.prev = self.tail
            self.tail = dataNode
        self.index+=1
    #**************************** Imprimir
    def printList(self):
        ref = self.head
        while(ref!=None):
            print(ref.data,end=" ")
            ref=ref.next
        print()

