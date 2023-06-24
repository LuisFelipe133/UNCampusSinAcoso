from typing import Generic,TypeVar
from .NodeTree import NodeTree
from .Queue import Queue
T = TypeVar("T")

class BST(Generic[T]):
    root:NodeTree 
    size:int

    #**************************************** Constructor
    def __init__(self):
        self.root = None
        self.size = 0
    #**************************************** métodos de verificación
    def isEmpty(self):
        return self.root == None

    def heightSubTree(self,branch:NodeTree):
        if branch is None:
            return 0
        else:
            lef = self.heightSubTree(branch.left)
            rig = self.heightSubTree(branch.right)
            height = 1+ max(lef,rig)
            return height
        
    def height(self):
        return self.heightSubTree(self.root)
    
    #**************************************** métodos de insertar y eliminar
    def insert(self,data:T):
        self.root = self.insertPriv(data,self.root)

    def insertPriv(self,data:T,ref:NodeTree):
        dataNode = NodeTree(data)
        if ref is None:
            ref = dataNode
        else:
            if data < ref.data:
                ref.left = self.insertPriv(data,ref.left)
            elif data > ref.data:
                ref.right = self.insertPriv(data,ref.right)
            elif data == ref.data:
                print(data,"ya está en el arbol")
        return ref
    
    def delete(self,data:T):
        self.root = self.deletePriv(data,self.root)

    def deletePriv(self,data:T,ref:NodeTree):
        if ref is None:
            return ref
        if data < ref.data:
            ref.left = self.deletePriv(data,ref.left)
        elif data > ref.data:
            ref.right = self.deletePriv(data,ref.right)
        else:
            if ref.left == None:
                temp = ref.right
                ref = None
                return temp
            elif ref.right == None:
                temp = ref.left
                ref = None
                return temp
            else:
                temp = self.findMinNode(ref.right)
                ref.data = temp.data
                ref.right = self.deletePriv(temp.data,ref.right)
        return ref

    #**************************************** Buscar en el arbol
    def findMinNode(self,ref:NodeTree):
        if ref.left is None:
            return ref
        return self.findMinNode(ref.left)
    
    def findMin(self, ref:NodeTree):
        if ref.left is None:
            return ref.data
        return self.findMin(ref.left)
    
    
    def findMax(self,ref:NodeTree):
        if ref.right is None:
            return ref
        return self.findMax(ref.right)
    
    def findElement(self,data:T):
        return self.findPriv(self.root,data)
    
    def findPriv(self,ref:NodeTree,data:T):
        if ref is None or ref.data == data:
            return ref
        elif data < ref.data:
            return self.findPriv(ref.left,data)
        elif data > ref.data:
            return self.findPriv(ref.right,data)
        
        
    def leftChild(self,ref:NodeTree):
        if ref.left is None:
            return ref
        else:
            return self.leftChild(ref.left)
        
    def rightChild(self,ref:NodeTree):
        if ref.right is None:
            return ref
        else:
            return self.rightChild(ref.right)
    
    def next(self,ref:NodeTree):
        if ref is None:
            return None
        else:
            if ref.right != None:
                return self.leftChild(ref.right)
            else:
                try:
                    return self.rightChild(ref)
                except:
                    return ref.right
    #**************************************** Imprimir y recorrer el arbol
    def printPreorderSubTree(self,node:NodeTree):
        if node != None:
            print(node.data,end=" ")
            self.printPreorderSubTree(node.left)
            self.printPreorderSubTree(node.right)

    def printPreOrder(self):
        self.printPreorderSubTree(self.root)
    
    def printInOrderSubTree(self,node:NodeTree):
        if node != None:
            self.printInOrderSubTree(node.left)
            print(node.data,end=" ")
            self.printInOrderSubTree(node.right)

    def printInOrder(self):
        self.printInOrderSubTree(self.root)
    
    def printPostOrderSubTree(self,node:NodeTree):
        if node != None:
            self.printPostOrderSubTree(node.left)
            self.printPostOrderSubTree(node.right)
            print(node.data,end=" ")

    def printPostOrder(self):
        self.printPostOrderSubTree(self.root)
    
    def printLevelOrder(self):
        if self.isEmpty():
            return None
        else:
            cola = Queue()
            cola.enqueue(self.root)
            while not cola.isEmpty():
                print(cola.first().data,end=" ")
                if cola.first().left !=None:
                    cola.enqueue(cola.first().left)
                if cola.first().right !=None:
                    cola.enqueue(cola.first().right)
                cola.dequeue()
    
        


