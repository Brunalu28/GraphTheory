from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''

        # o(n2)
        arestas = self.arestas
        vertices = self.vertices
        naoAdjacentes = set()
        for v in vertices:
            adjacentes = []
            for a in arestas:
                if arestas[a].v1.rotulo == v.rotulo:
                    v2 = arestas[a].v2.rotulo
                    adjacentes.append(v2)
                elif arestas[a].v2.rotulo == v.rotulo:
                    v1 = arestas[a].v1.rotulo
                    adjacentes.append(v1)
            for vn in vertices:
                if vn.rotulo != v.rotulo and vn.rotulo not in adjacentes:
                    naoAdjacentes.add(f'{v.rotulo}-{vn.rotulo}')
        return naoAdjacentes


    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        # o(n)
        arestas = self.arestas
        for a in arestas:
            if arestas[a].v1.rotulo == arestas[a].v2.rotulo:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''

        # o(n)
        if not self.existe_vertice(V):
            raise VerticeInvalidoError()
        else:
            grau = 0
            arestas = self.arestas
            for a in arestas:
                if arestas[a].v1.rotulo == V:
                    grau += 1
                if arestas[a].v2.rotulo == V:
                    grau += 1
            return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        # 0(n)
        arestas = self.arestas
        conjuntoArestas = []
        for a in arestas:
            aresta = (arestas[a].v1.rotulo, arestas[a].v2.rotulo)
            if aresta in conjuntoArestas or aresta[::-1] in conjuntoArestas:
                return True
            else:
                conjuntoArestas.append(aresta)
        return False


    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        # 0(n)
        arestas = self.arestas
        if not self.existe_vertice(V):
            raise VerticeInvalidoError()
        else:
            arestasIncidentes = []
            for a in arestas:
                if arestas[a].v1.rotulo == V or arestas[a].v2.rotulo == V:
                    arestasIncidentes.append(arestas[a])
            return arestasIncidentes

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        # O(n)
        if self.ha_paralelas() or self.ha_laco():
            return False

        completo = len(self.vertices) - 1
        vertices = self.vertices

        for v in vertices:
            if self.grau(v) != completo:
                return False
        return True