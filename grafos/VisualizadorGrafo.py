import networkx as nx
import matplotlib.pyplot as plt
   
  
class VisualizadorGrafo:
   
    def __init__(self):
        self.visual = []
          
    def agregar_arista(self, a, b):
        arista = [a, b]
        self.visual.append(arista)
          
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()