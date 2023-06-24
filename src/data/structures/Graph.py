from .HashTable import HashTable
from .LinkedList import LinkedList

class Graph:
    adyacenciaLista:HashTable
    #*************************** Constructor
    def __init__(self):
        self.adyacenciaLista= HashTable()
    #*************************** Imprimir
    def printGraph(self):
        self.adyacenciaLista.printHashTable()
    #*************************** Añadir y eliminar
    def addVertex(self,vertexVal):
        repeatedVertex:bool = self.adyacenciaLista.find(vertexVal)
        if not repeatedVertex:
            self.adyacenciaLista.insert(vertexVal,[])
    
    def removeVertex(self,vertexToRemove):
        repeatedVertex:bool = self.adyacenciaLista.find(vertexToRemove)
        if repeatedVertex:
            self.adyacenciaLista.delete(vertexToRemove)
            for i in self.adyacenciaLista.table.array:
                if i != None and len(i)!=0:
                    current_edge:list = i[0][1]
                    if vertexToRemove in current_edge:
                        current_edge.remove(vertexToRemove)

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
        
    #*************************** Buscar y recorrer
    def findVertex(self,vertex):
        return self.adyacenciaLista.find(vertex)
    
    def findEdge(self,vertexOne,vertexTwo):
        repeatedVertexOne:bool = self.adyacenciaLista.find(vertexOne)
        if repeatedVertexOne:
            listaVertex:list = self.adyacenciaLista.get(vertexOne)
            if len(listaVertex)!=0 and listaVertex.__contains__(vertexTwo):
                return True
        return False