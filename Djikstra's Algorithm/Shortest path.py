class Min_heap(list):

    """Summary of heap class here.

    Create a heap with using list as a data structure

    Attributes:
        __init__: A list hold data
        __repr__: return str
        swap(): swap two object in heap
        insert: insert object in heap
        extract_min: get the min object in heap
        decrease_key: change value of the object in heap
        
    """

    def __init__(self):
        # A list hold objects from user
        self.min_heap = list([])

    def __repr__(self):
        # representation of min-heap class objects
        rep=''
        for i in self.min_heap:
          rep += (str(i)+ ', ')
        return rep

    def swap(self, parents_index, child_index):
        # swap two objects in heap by their index
        temp_value = self.min_heap[parents_index]
        self.min_heap[parents_index] = self.min_heap[child_index]
        self.min_heap[child_index] = temp_value

    def insert(self,value_pair):
        # insert a key_value_pair object in heap
        #check if new key_pair is in heap: if have just return dont allow being update
        for i in self.min_heap:
            if i[0] == value_pair[0]:
                return
        #append key_value_pair object in heap
        self.min_heap.append(value_pair)
        # doing  heapify
        value_index = len(self.min_heap) - 1  #new object's index
        parents_index = (value_index -1) //2  #parent's index
        # if check value_index > 0 and parent's value > new object's value do
        while (value_index > 0) and (self.min_heap[parents_index][1] > self.min_heap[value_index][1]):
            self.swap(parents_index,value_index) # swap two objects
            value_index = parents_index          # set new object's index to its parent's index
            parents_index = (value_index-1) //2  # set new parent's index
            #stop when value_index <= 0 and parent's value < new object's value
        
    def extract_min(self):
        # get the min object in heap
        # swap min object to last index
        self.swap(0,len(self.min_heap)-1)
        # extract min object
        min_value = self.min_heap.pop(len(self.min_heap)-1)
        #reheapify our first object
        value_index = 0  #reheapify object's index
        # if only two object in heap, just bruteforce
        if len(self.min_heap) == 2:
            if self.min_heap[0][1] >  self.min_heap[1][1]:
                self.swap(0,1)
            return min_value

        # if reheapify object's index is less than (length of heap)//2 and if reheapify object's index is less than (length of heap) do
        while (value_index < (len(self.min_heap)-1)//2) and (value_index < len(self.min_heap)-1 ):
            # compare reheapify object's childrens
            child_index_left = (value_index*2)+1
            child_index_right = (value_index*2)+2
            #if reheapify object's value greater than one of each
            if (self.min_heap[value_index][1] > self.min_heap[child_index_left][1]) or (self.min_heap[value_index][1] > self.min_heap[child_index_right][1]):
                if self.min_heap[child_index_left][1] < self.min_heap[child_index_right][1]:
                    self.swap(value_index,child_index_left)
                    value_index = child_index_left
                else:
                    self.swap(value_index,child_index_right)
                    value_index = child_index_right
            # if not greater than both, we stop and break the while loop
            else:
                break
            
        return min_value


    def decrease_key(self,value_pair):
        #set return index to -1 for return false
        key_index = -1

        # search if object is in min_heap
        for i in range(len(self.min_heap)):
            if self.min_heap[i][0] == value_pair[0]:
                 # get the index of the object
                key_index = i
                
        if key_index < 0:
            return False

        #set the new value for object 
        self.min_heap[key_index] = value_pair
        #reheapify our object
        value_index = key_index
        parents_index = (value_index -1)//2
        
        #compare to its parents if our object is greater than 0 and parent's value is greater than object values
        while (value_index > 0) and (self.min_heap[parents_index][1] > self.min_heap[value_index][1]):
            self.swap(parents_index,value_index)  # swap two objects
            value_index = parents_index           # set new object's index to its parent's index
            parents_index = (value_index-1)//2    # set new parent's index


class Graph(object):
    
    """Summary of graph class here.

    Create an adjacencylist for graph data structure

    Attributes:
        __init__: adjacencylist for hold data
        __repr__: return str for user debug
        
        
    """


    def __init__(self, vertex=0):
        #example A [('J', 18), ('H', 79), ('I', 81)]
        self.vertex = vertex    # provide in txt file first row
        self.edges = 0          # number edges 
        self.adjacencylist = dict({})  # a dictonary for all vertex in txt file 
        self.characters = ['A','B','C','D','E','F','G','H','I','J','K',
                           'L','M','N','O','P','Q','R','S','T','U','V',
                           'W','X','Y','Z']
        # since its using alphabet and number of alphabet is define by vertex number
        # create a list inside each vertex
        for i in self.characters[:vertex]:
            self.adjacencylist[i]=list([])
            
    
    def __repr__(self):
        #return str for user debug
        #example A [('J', 18), ('H', 79), ('I', 81)]
        rep =''
        for i in self.adjacencylist:
           rep += str(i) + ' ' + str(self.adjacencylist[i])+'\n'
        return rep[:-1]
    

    def __getitem__(self,V):
        # it describes objects that are "containers", meaning they contain other objects.
        # This includes strings, lists, tuples, and dictionaries.
        # so that can run for loop
        return self.adjacencylist[V]
        
            
    def addedge(self,starting,termination,weight):
        # add edge for vertex in graph
        self.edges += 1
        # B [('C', 22)]
        self.adjacencylist[starting].append((str(termination),weight))
        # C [('H', 50), ('I', 97), ('B', 22)]
        self.adjacencylist[termination].append((str(starting),weight))



def bulid_graph(file):
    
    """readfile and add edges into Graph

    Args:
    
        file: external file

    Returns:
        example: A [('D', 30), ('E', 93), ('C', 79)]
                 B [('J', 92), ('K', 86), ('G', 100), ('Q', 50), ('N', 61), ('P', 50)]
                 C [('A', 79), ('I', 10), ('E', 50)]
                 
    Raises:
      if readline error

    """

    f = open(file,"r")                                      #open file
    vertex = f.readline()                                   #readline (first row is vertex)
    graph  = Graph(int(vertex))                             #create graph objects
    edge = f.readline()                                     #add edges 
    while edge:                                             # while can read line do
        try:                                                # try
            edge = edge.split(" ")
            graph.addedge(edge[0],edge[1],eval(edge[2]))    # v, u, value
            edge = f.readline()
        except:
            print("Error")
    return graph


def initialize(G):
    
    """intialize for DIJKSTRA

    Args:
        Graph: dictionary inside list

    Returns:
        distance: a dictionay with all vertex with inf distance
        parent:   a dictionay with all vertex with no parents

        {'A': inf, 'B': inf, 'C': inf}
        {'A': '', 'B': '', 'C': ''}

    """
    
    distance= {}
    parent = {}
    v = G.vertex
    characters = ['A','B','C','D','E','F','G','H','I','J','K',
                           'L','M','N','O','P','Q','R','S','T','U','V',
                           'W','X','Y','Z']
    for i in characters[:v]:
        distance[i] = float('inf')
        parent[i] = ''

    return distance, parent


def DIJKSTRA(G,start):

    '''
        DIJKSTRA(G, s)
    1 for all v ∈ V
    2   dist(v) = ∞
    3   π(v) = nil
    4 dist(s) = 0
    5 H = V(G)
    6 while H != ∅
    7   u = Extract-Min(H)
    8     for all w ∈ N(u) that are in H
    9       if dist(u) + wt(u, w) < dist(w)
    10         dist(w) = dist(u) + wt(u, w)
    11         π(w) = u
    12         Decrease-Key(H, (w, dist(w)))
    '''

    #initalize
    distance, parent = initialize(G)
    
    #set first vertex key to zero (weight) which is start object
    distance[start] = 0
    #insert all into the heap O(nlogn)
    
    H = Min_heap()
    for i in distance:
        H.insert((i,distance[i]))
    # ('A', 0), ('B', inf), ('C', inf)

    #While heap is not empty do
    while not H:
        # try extract
        try:
            min_pair = H.extract_min() #('A', 0)
        # if not mean epmty return distance and parent for build path
        except:
            return distance, parent 

        # EXTRACT-MIN in heap
        u = min_pair[0]
        dis = min_pair[1]
        # for each w  in heap that is adjacent to u
        for w in G[u]:
            # add up there distance with u
            temp_dis = dis + w[1]
            # if distance between (u, w) < distance itself do
            if temp_dis < distance[w[0]]:
                # change the  w distance inside distance dictionary
                distance[w[0]] = dis + w[1]
                 # change the  w parent to u inside parent dictionary
                parent[w[0]] = u
                # decrease the key pair value in heap
                H.decrease_key(( w[0],distance[w[0]]) )
                
    return distance, parent

def path(parents,endstop):
    
    """create path for endstop from start to end

    Args:
        parent:   a dictionay with all vertex with no parents
        endstop: end vertex

    Returns:
        shortest_path: a str object

    """
    
    shortest_path =" "+ endstop

    while parents[endstop] is not '':
        parent = parents[endstop]
        shortest_path = " " + parent + shortest_path
        endstop = parent
    return shortest_path[1:]
    

def main():

    print("#Author: Wilson Wu\n#Date:2021.05.20\n#StudentID:1939700\n")
    
    file_list = ["Case1.txt","Case2.txt","Case3.txt"]
    
    for file in file_list:
        graph=bulid_graph(file)
        distance, parent = DIJKSTRA(graph,"A")
        shortest_path = path(parent,"B")
        print("{}:\n{}\n{}\n".format(file,distance["B"],shortest_path))        

if __name__ == "__main__":
    main()
    
