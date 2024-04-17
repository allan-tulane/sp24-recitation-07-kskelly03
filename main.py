from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
      current_node = frontier.pop()
      for neighbor in graph[current_node]:
        if neighbor not in result:
            result.add(neighbor)
            frontier.add(neighbor)
    return result

def connected(graph):
  start_node = next(iter(graph))
  reached = reachable(graph, start_node)
  return len(reached) == len(graph) 

def n_components(graph):
  """
  Returns:
    the number of connected components in an undirected graph
  """
  visited_nodes = set() 
  count = 0
  for node in graph:
    if node not in visited_nodes:
      new_visited = reachable(graph, node)
      visited_nodes.update(new_visited)
      count += 1  
  return count

        
        
  
  

