from .HashTable import HashTable
from .LinkedList import LinkedList

class Graph:
    adyacenciaLista:HashTable

    def __init__(self):
        self.adyacenciaLista= HashTable()
    
    def printGraph(self):
        self.adyacenciaLista.printHashTable()

    def addVertex(self,vertexVal):
        repeatedVertex:bool = self.adyacenciaLista.find(vertexVal)
        if not repeatedVertex:
            self.adyacenciaLista.insert(vertexVal,LinkedList())

    def addEdge(self,vertexBegin,vertexEnd):
        repeatedVertexBegin:bool = self.adyacenciaLista.find(vertexBegin)
        repeatedVertexEnd:bool = self.adyacenciaLista.find(vertexEnd)
        if repeatedVertexBegin and repeatedVertexEnd:
            vBeginList:LinkedList = self.adyacenciaLista.get(vertexBegin)
            vEndList:LinkedList = self.adyacenciaLista.get(vertexEnd)
            if str(vertexBegin) == str(vertexEnd):
                if vBeginList.isEmpty() or not vBeginList.contains(vertexEnd):
                    vBeginList.pushBack(vertexEnd)
            else:
                if vBeginList.isEmpty() or not vBeginList.contains(vertexEnd):
                    vBeginList.pushBack(vertexEnd)
                if vEndList.isEmpty() or not vEndList.contains(vertexBegin):
                    vEndList.pushBack(vertexBegin)
        else:
            raise Exception("One or both vertex don't exist")