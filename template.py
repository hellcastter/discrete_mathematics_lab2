"""
member1: <Name Surname>
member2: <Name Surname>
"""
from typing import List, Dict


def read_csv(file_name: str) -> Dict[int, List[int]]:
    """
    Read graph represented as matrix in .csv file and return it
    as dictionary where each key represents a vertex, while the value
    represent the list of matrices adjacent to the key
    
    :param file_name: string
    :rtype: dict(key=int, value=list(int))
    :return: graph
    """
    pass


def bfs(graph: Dict[int, List[int]]) -> List[int]:
    """
    perform bfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    
    :param graph: dict(key=int, value=list(int))
    :rtype: list(int)
    :return: bfs-result
    """
    # Your code goes here(delete "pass" keyword)
    pass


def dfs(graph: Dict[int, List[int]]) -> List[int]:
    """
    perform dfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    
    :param graph:  dict(key=int, value=list(int))
    :rtype: list(int)
    :return: dfs-result
    """
    # Your code goes here(delete "pass" keyword)
    pass


def calc_pow(graph: Dict[int, List[int]]) -> Dict[int, int]:
    """
    calculate power of every vertex of your graph(i.e. number adjacent edges)
    
    :param graph: dict(key=int, value=list(int))
    :rtype: dict(key=int, value=int)
    :return: vertices and their powers
    """
    # Your code goes here(delete "pass" keyword)
    pass


def find_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    here is another way of representing a graph:
    edges - is a list of edges of a graph,
    where each edge is also a list of two integers,
    which represent 2 adjacent vertices
    find if there is a way from the source vertex to the destination one
    
    :param n: int
    :param edges: list(list(int))
    :param source: int
    :param destination: int
    :rtype: bool
    :return:
    """
    # Your code goes here(delete "pass" keyword)
    pass
