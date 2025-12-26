import networkx as nx
import matplotlib.pyplot as plt
from networkx import Graph


def create_metro_graph() -> Graph:
    """
    Creates and returns an undirected graph representing a city's metro network.
    """
    graph: Graph = nx.Graph()
    stations: list[str] = ['Central', 'North', 'South', 'East', 'West', 'Park']
    graph.add_nodes_from(stations)
    edges: list[tuple[str, str]] = [
        ('Central', 'North'),
        ('Central', 'South'),
        ('Central', 'East'),
        ('Central', 'West'),
        ('West', 'Park'),
        ('East', 'Park')
    ]
    graph.add_edges_from(edges)
    return graph


def analyze_graph(graph: Graph) -> None:
    """
    Prints basic characteristics of the graph.
    """
    num_nodes: int = graph.number_of_nodes()
    num_edges: int = graph.number_of_edges()
    print(f"Number of nodes (stations): {num_nodes}")
    print(f"Number of edges (lines): {num_edges}")

    degrees: dict[str, int] = dict(graph.degree())
    print("Degree of each node (number of connections):")
    for station, degree in degrees.items():
        print(f"{station}: {degree}")


if __name__ == "__main__":
    metro_graph: Graph = create_metro_graph()
    analyze_graph(metro_graph)

    # Visualization
    plt.figure(figsize=(8, 6))
    nx.draw(
        metro_graph,
        with_labels=True,
        node_color='skyblue',
        node_size=1500,
        font_size=14,
        edge_color='gray'
    )
    plt.title("City Transport Network (Metro Map)")
    plt.show()
