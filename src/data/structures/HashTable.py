from .DynamicArray import DynamicArray
from .LinkedList import LinkedList

class HashTable:

    mapList:DynamicArray
    size:int
    alpha:float
    a:int
    b:int
    x:int

    class HashData:
         def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self,size=14,alpha=0.75,a=6,b=17,x=5641):
        self.mapList = DynamicArray()
        for i in range(0,size-1):
            self.mapList.pushBack(None)
        self.size=size
        self.alpha=alpha
        self.a=a
        self.b =b
        self.x = x

    def __iter__(self):
        self.indexIterable:int = 0
        self.listIterable:list = self.to_list()
        return self
    
    def to_list(self) -> list:
        indexIterable:int = 0
        lista:list = []
        while indexIterable < self.size:
            if self.mapList.array[indexIterable] is not None:
                hash_list:LinkedList = self.mapList.array[indexIterable]
                indexIterable += 1
                for hash in hash_list:
                    lista.append(hash)
            else:
                indexIterable += 1
        return lista
    
    def __next__(self):
        if self.indexIterable == len(self.listIterable):
            raise StopIteration
        else:
            self.indexIterable += 1
            return self.listIterable[self.listIterable-1]

    
    def isPrime(self,number:int):
        if number<=1:
            return False
        for i in range(2,int(number**0.5)+1):
            if number %i ==0:
                return False
        return True
            
    def getPrimeNumber(self,number:int):
        prime = number+1
        while not self.isPrime(prime):
            prime+=1
        return prime

    def hashFunctionInt(self,data:int):
        hashValue = (((self.a*data)+ self.b) % self.getPrimeNumber(self.size)) % self.size
        return hashValue

    def hashFunctionString(self,data:str):
        hashValue=0
        for i in range(len(data)-1,-1,-1):
            hashValue = ((hashValue * self.x) + ord(data[i])) % self.x % self.size
        return hashValue
    
    def get(self, key):
        if (str(type(key))=="<class 'int'>"):
            hashId = self.hashFunctionInt(key)
        elif (str(type(key))=="<class 'float'>"):
            hashId = self.hashFunctionInt(round(key))
        else:
            hashId = self.hashFunctionString(str(key))

        linked:LinkedList = self.mapList.array[hashId]
        for hashed in linked:
            hashed:HashTable.HashData
            if str(hashed.key) == str(key):
                return hashed.value
        raise KeyError("Key is not in HashTable")
    
    def find(self, key: int) -> bool:
        try:
            self.get(key)
            return True
        except Exception:
            return False
    
    def set(self, key:int, data:object) -> None:
        newHash:HashTable.HashData = HashTable.HashData(key, data)
        if (str(type(key))=="<class 'int'>"):
            hashId = self.hashFunctionInt(key)
        elif (str(type(key))=="<class 'float'>"):
            hashId = self.hashFunctionInt(round(key))
        else:
            hashId = self.hashFunctionString(str(key))
        linked:LinkedList = self.mapList.array[hashId]
        if linked is None:
            raise KeyError("Key is not in HashTable")
        for hash in linked:
            hash:HashTable.HashData
            if hash.key == key:
                oldHash:HashTable.HashData =  hash
                oldHashId = linked.findPosition(oldHash)
                linked.update(oldHashId, newHash)
                return
    def getKey(self) -> int:
        acc:int = 0
        for hash in self:
            acc += 1
        return acc
    
    def  loadFactor(self):
        return self.getKey()/self.size
    
    def rehash(self) -> None:
        loadFactor = self.loadFactor()
        if loadFactor > self.alpha:
            newTable:HashTable = HashTable(size=self.size*2)
            for hash in self:
                hash:HashTable.HashData
                newTable.insert(hash.key, hash.value)
            self.mapList = newTable.mapList
            self.size = newTable.size

    def insert(self,index:int,data:object):
        if self.find(index):
            self.set(index, data)
        else:
            if (str(type(index))=="<class 'int'>"):
                hashId = self.hashFunctionInt(index)
            elif (str(type(index))=="<class 'float'>"):
                hashId = self.hashFunctionInt(round(index))
            else:
                hashId = self.hashFunctionString(str(index))
            
            notHashed:HashTable.HashData = HashTable.HashData(index, data)
            if (self.mapList.array[hashId] == None):
                linked = LinkedList()
                linked.pushBack(notHashed)
                self.mapList.array[hashId] = linked
            else:
                linked:LinkedList = self.mapList.array[hashId]
                linked.pushBack(notHashed)
            self.rehash()
