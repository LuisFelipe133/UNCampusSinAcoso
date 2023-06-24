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
            self.adyacenciaLista.insert(vertexVal,[])

    def addEdge(self,vertexBegin,vertexEnd):
        repeatedVertexBegin:bool = self.adyacenciaLista.find(vertexBegin)
        repeatedVertexEnd:bool = self.adyacenciaLista.find(vertexEnd)
        if repeatedVertexBegin and repeatedVertexEnd:
            vBeginList:list = self.adyacenciaLista.get(vertexBegin)
            vEndList:list = self.adyacenciaLista.get(vertexEnd)
            if str(vertexBegin) == str(vertexEnd):
                if len(vBeginList)==0 or not vBeginList.__contains__(vertexEnd):
                    vBeginList.append(vertexEnd)
            else:
                if len(vBeginList)==0 or not vBeginList.__contains__(vertexEnd):
                    vBeginList.append(vertexEnd)
                if len(vEndList)==0 or not vEndList.__contains__(vertexBegin):
                    vEndList.append(vertexBegin)
        else:
            raise Exception("One or both vertex don't exist")
        
    def findVertex(self,vertex):
        return self.adyacenciaLista.find(vertex)
    
    def findEdge(self,vertexOne,vertexTwo):
        repeatedVertexOne:bool = self.adyacenciaLista.find(vertexOne)
        if repeatedVertexOne:
            listaVertex:list = self.adyacenciaLista.get(vertexOne)
            if len(listaVertex)!=0 and listaVertex.__contains__(vertexTwo):
                return True
        return False