
edges =  [('a', 's'), ('i', 'z'), ('c', 'p'), ('d', 'p'), ('d', 'u'), ('b', 'e'), ('b', 'g'),
          ('f', 'p'), ('g', 'm'), ('h', 't'), ('h', 'y'), ('i', 'w'), ('i', 'j'), ('i', 'x'),
          ('k', 's'), ('k', 'l'), ('a', 'm'), ('n', 'u'), ('a', 'o'), ('a', 'v'), ('n', 'p'),
          ('a', 'q'), ('a', 'h'), ('p', 'r'), ('l', 's'), ('t', 'v'), ('u', 'y'), ('j', 'v'),
          ('a', 'j'), ('r', 'w'), ('r', 'u'), ('f', 'x'), ('x', 'y'), ('j', 'x'), ('d', 'j'),
          ('b', 'k'), ('b', 'x'), ('b', 'w')]

def edges_to_connections(edges: list[tuple[str, str]]) -> dict[str,list[str]]:
    """ Returns a dict with for each node the nodes it is connected with. """
    connections = {}
    for n1, n2 in edges:
        if not n1 in connections:
            connections[n1] = []
        connections[n1].append(n2)
        if not n2 in connections:
            connections[n2] = []
        connections[n2].append(n1)
    return connections

def print_all_paths(connections, path, goal):
    raise NotImplementedError

if __name__ == "__main__":
    connections = edges_to_connections(edges)
    print_all_paths(connections, 'a', 'b')
