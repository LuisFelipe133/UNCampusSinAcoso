from typing import Generic,TypeVar
from .NodeTree import NodeTree
from .BST import BST
T = TypeVar("T")

class AVL(BST):
    def __init__(self):
        super().__init__()
    
    def rotateRight(self,node:NodeTree):
        if node is None or node.left is None:
            return node
        else:
            parent = node.left
            node.left = parent.right
            parent.right = node
            if self.root == node:
                self.root = parent
            return parent
    
    def rotateLeft(self,node:NodeTree):
        if node is None or node.right is None:
            return node
        else:
            parent = node.right
            node.right = parent.left
            parent.left = node
            if self.root == node:
                self.root = parent
            return parent
    
    def doubleRightRotation(self,node:NodeTree):
        node.left = self.rotateLeft(node.left)
        return self.rotateRight(node)

    def doubleLeftRotation(self,node:NodeTree):
        node.right = self.rotateRight(node.right)
        return self.rotateLeft(node)
    
    def getBalance(self,ref:NodeTree):
        return self.heightSubTree(ref.left) - self.heightSubTree(ref.right)
    
    def insertPriv(self, data: T, ref: NodeTree):
        if ref is None:
            ref = NodeTree(data)
        else:
            if data < ref.data:
                ref.left = self.insertPriv(data,ref.left)
            elif data > ref.data:
                ref.right = self.insertPriv(data,ref.right)
        balance = self.getBalance(ref)
        if balance >1 and data > ref.left.data:
            ref = self.doubleRightRotation(ref)
        if balance >1 and data < ref.left.data:
            ref = self.rotateRight(ref)
        if balance <-1 and data > ref.right.data:
            ref = self.doubleLeftRotation(ref)
        if balance <-1 and data > ref.right.data:
            ref = self.rotateLeft(ref)
        return ref


    
    def insert(self, data: T):
        self.root = self.insertPriv(data,self.root)