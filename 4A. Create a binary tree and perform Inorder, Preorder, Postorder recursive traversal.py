class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[0 for _ in range(vertices)]
                    for _ in range(vertices)]
        self.visited = [False] * vertices
 
    def create_graph(self):
        edges = int(input("Enter number of roads (edges): "))
 
        for _ in range(edges):
            source = int(input("Enter source vertex (0 to "
                               + str(self.vertices - 1) + "): "))
            destination = int(input("Enter destination vertex (0 to "
                                    + str(self.vertices - 1) + "): "))
 
            if (source < 0 or source >= self.vertices or
                    destination < 0 or destination >= self.vertices):
                print("Invalid vertex. Please enter valid vertex numbers.")
                continue
 
            # Undirected graph: update both directions.
            self.adj[source][destination] = 1
            self.adj[destination][source] = 1
 
    def display_graph(self):
        print("\\nAdjacency Matrix:")
        print("  ", end="")
        for i in range(self.vertices):
            print(i, end=" ")
        print()
 
        for i in range(self.vertices):
            print(i, end=" ")
            for j in range(self.vertices):
                print(self.adj[i][j], end=" ")
            print()
 
    def dfs(self, vertex):
        self.visited[vertex] = True
        print(vertex, end=" ")
 
        for neighbour in range(self.vertices):
            if (self.adj[vertex][neighbour] == 1 and
                    not self.visited[neighbour]):
                self.dfs(neighbour)
 
 
def main():
    vertices = int(input("Enter number of vertices: "))
 
    if vertices <= 0:
        print("Number of vertices must be greater than zero.")
        return
 
    graph = Graph(vertices)
    graph.create_graph()
    graph.display_graph()
 
    start = int(input("Enter starting vertex for DFS: "))
 
    if start < 0 or start >= vertices:
        print("Invalid starting vertex.")
        return
 
    graph.visited = [False] * vertices
    print("DFS Traversal:")
    graph.dfs(start)
    print()
 
 
if __name__ == "__main__":
    main()
