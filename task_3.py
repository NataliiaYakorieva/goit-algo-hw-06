import networkx as nx
from networkx import Graph
from typing import Dict, Tuple

from task_1 import create_metro_graph


def add_edge_distances(graph: Graph) -> None:
    """
    Adds distances (in kilometers) as weights to the edges of the metro graph.
    """
    # Distances between stations in kilometers
    distances: Dict[Tuple[str, str], float] = {
        ('Central', 'North'): 2.5,
        ('Central', 'South'): 3.2,
        ('Central', 'East'): 1.8,
        ('Central', 'West'): 2.0,
        ('West', 'Park'): 1.1,
        ('East', 'Park'): 0.9
    }
    for edge, distance in distances.items():
        # 'weight' attribute is used for Dijkstra
        graph[edge[0]][edge[1]]['weight'] = distance


def print_all_shortest_paths(graph: Graph) -> None:
    """
    Finds and prints the shortest paths and their total distances between all pairs of stations using Dijkstra's algorithm.
    """
    print("Shortest paths between all pairs of stations (using Dijkstra's algorithm, distance in km):\n")
    nodes: list[str] = list(graph.nodes())
    for source in nodes:
        for target in nodes:
            if source != target:
                try:
                    path: list[str] = nx.dijkstra_path(
                        graph, source, target, weight='weight')
                    length: float = nx.dijkstra_path_length(
                        graph, source, target, weight='weight')
                    print(
                        f"From {source} to {target}: Path: {path}, Total distance: {length} km")
                except nx.NetworkXNoPath:
                    print(f"No path from {source} to {target}")


if __name__ == "__main__":
    metro_graph: Graph = create_metro_graph()
    add_edge_distances(metro_graph)
    print_all_shortest_paths(metro_graph)
