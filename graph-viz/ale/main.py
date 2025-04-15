# Write a function that generates a DOT representation of a graph
# https://en.wikipedia.org/wiki/DOT_(graph_description_language)#Undirected_graphs
# https://dreampuf.github.io/GraphvizOnline/?engine=dot

complex_graph = {'a': {'b': {'c': None, 'd': None}, 'e': {'f': None, 'g': None}, 'h': {'i': None, 'k': {'l': None, 'm': None}}}}
first_graph = {'a': {'b': {'c': None}}}
# a -> b -> c
second_graph = {'a': {'b': {'c': None, 'd': None}}}

print(first_graph)

# {(a, b)}
def get_edges(graph):
    edges = set() # set ist dictionaryvon unique key ohne value
    # s'loop sruu dä grääf
    for k, v in graph.items():
        if v == None:
            continue
        else:
            for kk in v.keys():
                edges.add((k, kk))
            # edges.update((set(k, kk) for kk in v.keys()))
            edges.update(get_edges(v))
    return edges

def print_dot(edges):
    print('digraph a {')
    for a, b in edges:
        print(f'{a} -> {b};')
    print('}')

def main():
    first_edges = get_edges(first_graph)
    assert(first_edges == {('a', 'b'), ('b', 'c')})
    assert(get_edges(second_graph) == {('a', 'b'), ('b', 'c'), ('b', 'd')})
    print_dot(get_edges(complex_graph))

if __name__ == '__main__':
    main()
