import sys
import queue
import enum
import random
import time
import matplotlib.pyplot as plt


class Color(enum.Enum):
    BLACK=0
    GRAY=127
    WHITE=255

class Vertex:

    # Vertex constructor (fields : name,distance,parent,color,data(discovered,finished))
    
    def __init__(self,name):
        self.name=name
        self.distance="inf"
        self.parent=None
        self.color=Color.WHITE
        self.discovered = 0
        self.finished = 0

#Default fields for vertex (distance = infinite, doesn't have parent, color = White (not visited yet), not discovered, not finished)

    def reset(self):
        self.distance="inf"
        self.parent=None
        self.color=Color.WHITE
        self.discovered=None
        self.finished=None

# Breadth - first search

def BFS(graph,source):                            

    source.reset()                      #Puts source fields to default
    v_queue = queue.Queue()             #Initializing queue

    for vertex in graph.keys():         #Go through all whole graph and painting every vertex white since they are yet to be discovered
        if vertex!=source:
            vertex.reset()
    source.color=Color.GRAY             #Starting at source vertex, putting color = Gray because he is discovered
    source.distance=0                   #Source distance initialized to 0
    source.parent=None                  #Source has no parent

    v_queue.put(source)                #Adding source to queue

    while not v_queue.empty() :          #While loop iterates as long as there remain gray vertices (discovered vertices)
        vs = v_queue.get()
        for vertex in graph[vs]:        
            if vertex.color is Color.WHITE:
                vertex.color=Color.GRAY
                vertex.parent=vs
                vertex.distance=vs.distance+1
                v_queue.put(vertex)
        vs.color=Color.BLACK

# Depth - first search

def DFS(graph,vertex):
    for vertex in graph.keys():     # Initialize every vertex to be white
        vertex.reset()
    time=0                          # Initialize time
    for vertex in graph.keys():     # Go through graph and find white vertex, when found jump in DFS_VISIT
        if vertex.color==Color.WHITE:
            DFS_VISIT(graph,vertex,time)

def DFS_VISIT(graph,u,time):

    time += 1                       # White vertex discovered
    u.discovered=time               # Set time of discovery
    u.color=Color.GRAY              # Set color grey of discovered vertex
    for vertex in graph[u]:         # Find white neighbours and set him as parent of neighbour he discovered
        if vertex.color==Color.WHITE:
            vertex.parent=u
            DFS_VISIT(graph,vertex,time)
    u.color=Color.BLACK             # After went through full depth of vertex, paint him black
    time+=1                         
    u.finished=time                 # Set time when vertex is finished

# Function for printing path from source to some vertex when BFS

def print_path(graph, s, v):
    BFS(graph, s)
    _print_path(s, v)

def _print_path(s, v):
    
    if v == s:
        print(s.name)
    elif v.parent == None:
        print('No path from ' + s.name + ' to ' + v.name + ' exists')
    else:
        _print_path(s, v.parent)
        print(v.name)



# Function for printing path from source to some vertex when DFS

def print_path_dfs(graph, s, v):
    DFS(graph,s)
    _print_path(s, v)

# Function for printing distance from source to some vertex

def print_distance(graph,s,v):
    BFS(graph, s)
    if s==v:
        print("Source!!! Distance is 0")
    else:
        print("Distance from",s.name,"to",v.name,"is",v.distance)

# Sum of all edges in graph

def sum_edges(graph) :
    sum = 0
    for key in graph.keys() :
        sum += len(graph[key])
    return sum

# Sum of all vetexes in graph

def sum_vertexes(graph) :
    return len(graph.keys())

# Generating list of random vertixes

def random_vert(size, elements) :

    vertices_names = random.sample(range(1, size + 1), elements)
    vertices = []
    for item in vertices_names :
        vertices.append(Vertex(item))
    return vertices

def generate_graph(size) :
    graph = {}
    vertices = random_vert(10000, size)
    for vertex in vertices :
        graph[vertex] = []
    for item in graph :
        edge_number = random.randint(0, size)
        random.shuffle(vertices)
        graph[item] = vertices[0:edge_number]
    return graph

def source(graph) :
    for item in graph :
        return item

"""option = 1 -> BFS
   option = 2 -> DFS
"""
def time_measure(graph, option) :
    time_start = 0
    time_end = 0
    if option == 1: #BFS
        time_start = time.clock()
        BFS(graph,source(graph))
        time_end = time.clock()
    else : # DFS
        time_start = time.clock()
        DFS(graph,source(graph))
        time_end = time.clock()
    return time_end - time_start

def analyse() :
    vertices = [5, 25, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    exectimebfs = []
    exectimedfs = []
    edges = []
    for item in vertices:
        temp_graph = generate_graph(item)
        # broj ivica
        edges.append(sum_edges(temp_graph))
        # vreme za BFS
        exectimebfs.append(time_measure(temp_graph, 1))
        # vreme za DFS
        exectimedfs.append(time_measure(temp_graph, 2))
    plot_graph(vertices, edges, exectimebfs, 'Breath-First-Search')
    plot_graph(vertices, edges, exectimedfs, 'Depth-First-Search')

def plot_graph(vertices, edges, exec_time, label) :
    """Kreiranje plota"""
    input_data = []
    for index, item in enumerate(vertices):
        input_data.append(item + edges[index])
    plt.plot(input_data, exec_time, label=label)
    plt.xlabel('V + E [n]')
    plt.ylabel('T[S]')
    plt.legend()
    print(label)
    for index, item in enumerate(vertices):
        print("Number of vertecies: {} Number of edges: {} Time: {}"\
        .format(item, edges[index], exec_time[index]))

#analyse()
#plt.show()
    
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
V = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')
G = Vertex('G')


BFSG = {
    A: [B, C, E],
    B: [A, D, E],
    C: [A, F, G],
    D: [B, E],
    E: [A, D, B],
    F: [],
    G: []
    }

print("---------------")
print("Printing path for BFS")
print_path(BFSG, A, G)
print("---------------")

R = Vertex('R')
S = Vertex('S')
W = Vertex('W')
T = Vertex('T')
U = Vertex('U')
Y = Vertex('Y')
X = Vertex('X')
Z = Vertex('Z')


BFSG = {
    S: [R, W],
    R: [S, V],
    V: [R],
    W: [S, T, X],
    T: [W, X, U, Y],
    X: [T, W, Y],
    U: [T, X, Y],
    Y: [T, X, U]
    }

print()
print("---------------")
print("Printing path for BFS")
print_path(BFSG, S, T)
print("---------------")
print_distance(BFSG, V, U)
print("------------")
print()


DFSG = {
    A: [B, C],
    B: [A,D],
    C: [A, F, G],
    D: [B],
    E: [],
    F: [],
    G: [C,E]
}

print_path_dfs(DFSG, A, G)
