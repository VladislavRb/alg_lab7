from graph import CompleteGraph
from weight_matrices import *


c_graph = CompleteGraph(weight_matrices_array[1])
print(*c_graph.prim())
print(*c_graph.kruskal())
