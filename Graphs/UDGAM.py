class UDGAM:
    def __init__(self, n):
        self.n = n
        self.m = [[0] * n for _ in range(n)]

    def add_edge(self, u, v):
        self.m[u][v] = 1
        self.m[v][u] = 1

    def display(self):
        print("Adjacency Matrix:")
        for row in self.m:
            for x in row:
                print(x, end=" ")
            print()

def main():
    n = int(input("Enter number of vertices: "))
    g = UDGAM(n)

    while True:
        u, v = map(int, input("Enter edge (u v): ").split())
        g.add_edge(u, v)

        ch = int(input("Enter -1 to quit or any other number to continue: "))
        if ch == -1:
            break

    g.display()

if __name__ == "__main__":
    main()
