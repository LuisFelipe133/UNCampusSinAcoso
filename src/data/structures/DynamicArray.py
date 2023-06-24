from typing import Generic,TypeVar
T = TypeVar("T")

class DynamicArray(Generic[T]):
    size:int = None #tamaño del array
    array:list = None #Lista que es el array
    index:int = None #En qué posición está el arreglo
    position:int = None #variables para buscar elementos

    #********************* constructor
    def __init__(self):
        self.size=5
        self.array=[]
        for i in range(0,self.size):
            self.array.append(None)
        self.index=0
    #********************* metodos de verificación o atributos

    def len(self):
        return self.size
    
    def isEmpty(self):
        return self.index==0
    
    def isFull(self):
        return self.size == self.index
    #***************************** insertar o eliminar
    def pushBack(self,data:T):
        if self.isFull():
            self.size*=2
            newArray = []
            for i in range(0,self.index):
                newArray.append(self.array[i])
            for j in range(self.index,self.size):
                newArray.append(None)
            self.array=newArray
            self.pushBack(data)
        else:
            self.array[self.index]=data
            self.index += 1

    def pushFront(self,data:T):
        if self.isFull():
            self.size*=2
            newArray = []
            for i in range(0,self.index):
                newArray.append(self.array[i])
            for j in range(self.index,self.size):
                newArray.append(None)
            self.array=newArray
            self.pushFront(data)
        else:
            for i in range(self.index,0,-1):
                self.array[i] = self.array[i-1]
            self.array[0]=data
            self.index+=1

    def popBack(self):
        if not self.isEmpty():
            self.index-=1
        else:
            raise Exception("No se puede eliminar elemento en lista vacia")

    def popFront(self):
        if not self.isEmpty():
            for i in range(0,self.index-1):
                self.array[i] = self.array[i+1]
            self.index-=1
        else:
            raise Exception("No se puede eliminar elemento en lista vacia")
    #****************************************** buscar elementos
    def topFront(self):
        return self.array[0]
    
    def topBack(self):
        return self.array[self.index]
    
    def contains(self,data:T):
        found:bool = False
        if not self.isEmpty():
            for i in range(0,self.index):
                if self.array[i]==data:
                    found=True
                    self.position=i
                    break
        return found

    def find(self,data:T):
        if self.contains(data):
            return self.position
    def update(self,pos:int,data:T):
        if pos<=self.size:
            self.array[pos] = data
            
    #****************************************** imprimir
    def printArray(self):
        if(self.index<=self.size):
            for i in range(0,self.index):
                if str(self.array[i])!='[]':
                    print(self.array[i],end=" ")
            print()
