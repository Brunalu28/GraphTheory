from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import MeuGrafo

grafopb = MeuGrafo()

grafopb.adiciona_vertice("J")
grafopb.adiciona_vertice("C")
grafopb.adiciona_vertice("E")
grafopb.adiciona_vertice("P")
grafopb.adiciona_vertice("M")
grafopb.adiciona_vertice("T")
grafopb.adiciona_vertice("Z")

grafopb.adiciona_aresta("a1", "J", "C")
grafopb.adiciona_aresta("a2", "C", "E")
grafopb.adiciona_aresta("a3", "C", "E")
grafopb.adiciona_aresta("a4", "C", "P")
grafopb.adiciona_aresta("a5", "C", "P")
grafopb.adiciona_aresta("a6", "C", "M")
grafopb.adiciona_aresta("a7", "C", "T")
grafopb.adiciona_aresta("a8", "M", "T")
grafopb.adiciona_aresta("a9", "T", "Z")

print(grafopb)

print("Informações sobre o grafo da Paraíba: \n")

print('Vértices não adjacentes: ', grafopb.vertices_nao_adjacentes())
print('O grafo tem laço? ', grafopb.ha_laco())
print('Grau do vértice E: ', grafopb.grau('E'))
print('O grafo tem arestas paralelas: ', grafopb.ha_paralelas())
print('Arestas que incidem no vértice J: ', grafopb.arestas_sobre_vertice('J'))
print('O grafo é completo? ', grafopb.eh_completo())



