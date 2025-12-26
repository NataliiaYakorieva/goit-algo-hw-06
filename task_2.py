import matplotlib.pyplot as plt
import networkx as nx
from networkx import Graph
from typing import List, Optional

from task_1 import create_metro_graph


def dfs_path(graph: Graph, start: str, goal: str) -> Optional[List[str]]:
    """
    Finds a path from start to goal using Depth-First Search (DFS).
    Returns the path as a list of nodes, or None if not found.
    """
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex == goal:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.neighbors(vertex):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None


def bfs_path(graph: Graph, start: str, goal: str) -> Optional[List[str]]:
    """
    Finds the shortest path from start to goal using Breadth-First Search (BFS).
    Returns the path as a list of nodes, or None if not found.
    """
    try:
        return nx.shortest_path(graph, source=start, target=goal)
    except nx.NetworkXNoPath:
        return None


def highlight_path(
        graph: Graph, path: Optional[List[str]], title: str) -> None:
    """
    Visualizes the graph and highlights the given path.
    """
    if path is None:
        print(f"No path to highlight for {title}.")
        return
    color_map: List[str] = [
        'orange' if node in path else 'skyblue' for node in graph.nodes()]
    edge_colors: List[str] = []
    path_edges = set(zip(path, path[1:]))
    for edge in graph.edges():
        if edge in path_edges or (edge[1], edge[0]) in path_edges:
            edge_colors.append('red')
        else:
            edge_colors.append('gray')
    plt.figure(figsize=(8, 6))
    nx.draw(
        graph,
        with_labels=True,
        node_color=color_map,
        node_size=1500,
        font_size=14,
        edge_color=edge_colors,
        width=2
    )
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    metro_graph: Graph = create_metro_graph()

    start_node: str = 'North'
    goal_node: str = 'Park'

    dfs_result: Optional[List[str]] = dfs_path(
        metro_graph, start_node, goal_node)
    bfs_result: Optional[List[str]] = bfs_path(
        metro_graph, start_node, goal_node)

    print(f"DFS path from {start_node} to {goal_node}: {dfs_result}")
    print(f"BFS path from {start_node} to {goal_node}: {bfs_result}")

    highlight_path(metro_graph, dfs_result, "DFS Path")
    highlight_path(metro_graph, bfs_result, "BFS Path")
