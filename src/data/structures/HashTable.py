from .DynamicArray import DynamicArray
class HashTable:
    table:DynamicArray = None
    size:int = 14
    alpha:float = 0.75
    numItems:int=0
    a:int = 5
    b:int = 15
    x:int = 3470

    def __init__(self):
        #self.table = [[] for _ in range(self.size)]
        self.table = DynamicArray()
        for i in range(self.size):
            self.table.pushBack([])

    def __str__(self)->str:
        return str(self.table)
    
    def printHashTable(self):
        self.table.printArray()
    
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

    def insert(self, key, value):
        indexedHash =0
        if(str(type(key))=="<class 'int'>"):
            indexedHash = self.hashFunctionInt(key)
        elif(str(type(key))=="<class 'str'>"):
            indexedHash = self.hashFunctionString(key)
        for kvp in self.table.array[indexedHash]:
            if kvp[0] == key:
                kvp[1] = value
                return 
        self.table.array[indexedHash].append([key, value])

    def delete(self, key):
        indexedHash =0
        if(str(type(key))=="<class 'int'>"):
            indexedHash = self.hashFunctionInt(key)
        elif(str(type(key))=="<class 'str'>"):
            indexedHash = self.hashFunctionString(key)
        for kvp in self.table.array[indexedHash]:
            if kvp[0] == key:
                self.table.array[indexedHash].remove(kvp)
                return
        raise KeyError("Key not found.")

    def get(self, key):
        indexedHash =0
        if(str(type(key))=="<class 'int'>"):
            indexedHash = self.hashFunctionInt(key)
        elif(str(type(key))=="<class 'str'>"):
            indexedHash = self.hashFunctionString(key)
        for kvp in self.table.array[indexedHash]:
            if kvp[0] == key:
                return kvp[1]
        raise KeyError("Key not found.")
    def find(self,key):
        try:
            self.get(key)
            return True
        except:
            return False 

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False