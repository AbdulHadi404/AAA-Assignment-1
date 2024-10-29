from collections import defaultdict
from typing import List, Tuple, Dict

class SupplierGraph:
    def __init__(self):
        # Initialize the graph using a defaultdict of dictionaries to represent edges with weights
        self.graph: Dict[int, Dict[int, int]] = defaultdict(dict)
        # Initialize suppliers using a defaultdict of sets to keep track of product categories for each supplier
        self.suppliers: Dict[int, set] = defaultdict(set)

    def add_product(self, supplier_id: int, category: str):
        # Add a product category to a supplier
        self.suppliers[supplier_id].add(category)

    def add_edge(self, supplier_id1: int, supplier_id2: int, weight: int):
        # Add an undirected edge between two suppliers with a given weight (shared categories)
        self.graph[supplier_id1][supplier_id2] = weight
        self.graph[supplier_id2][supplier_id1] = weight

    def find_shared_categories(self, supplier_id1: int, supplier_id2: int) -> int:
        # Return the number of shared product categories between two suppliers
        return len(self.suppliers[supplier_id1].intersection(self.suppliers[supplier_id2]))

    def create_graph(self):
        # Create the supplier graph by adding edges based on shared product categories
        supplier_ids = list(self.suppliers.keys())
        for i in range(len(supplier_ids)):
            for j in range(i + 1, len(supplier_ids)):
                # Calculate weight based on shared categories and add edge if weight > 0
                weight = self.find_shared_categories(supplier_ids[i], supplier_ids[j])
                if weight > 0:
                    self.add_edge(supplier_ids[i], supplier_ids[j], weight)

    def prim_mst(self) -> List[Tuple[int, int]]:
        # Generate the Minimum Spanning Tree (MST) using Prim's algorithm
        start_supplier = next(iter(self.graph))  # Start from an arbitrary supplier
        visited = set([start_supplier])  # Track visited suppliers
        edges = []  # Temporary list to store candidate edges for the MST
        min_edges = []  # List to store the edges of the MST

        # Continue until all suppliers are visited
        while len(visited) < len(self.graph):
            # Explore all edges from the visited suppliers
            for u in visited:
                for v in self.graph[u]:
                    if v not in visited:
                        edges.append((u, v, self.graph[u][v]))  # Store the edge with its weight
            
            edges.sort(key=lambda x: x[2])  # Sort edges by weight
            
            # Add the minimum weight edge that connects to a new supplier
            for edge in edges:
                if edge[1] not in visited:
                    min_edges.append((edge[0], edge[1]))
                    visited.add(edge[1])  # Mark the supplier as visited
                    break
            edges = []  # Clear edges for the next iteration

        return min_edges  # Return the edges of the MST

    def find_parent(self, parent: List[int], i: int) -> int:
        # Helper function to find the root parent of a node with path compression
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def kruskal_mst(self) -> List[Tuple[int, int]]:
        # Generate the Minimum Spanning Tree (MST) using Kruskal's algorithm
        edges = []  # List to store all edges with their weights
        
        # Gather all edges from the graph
        for u in self.graph:
            for v in self.graph[u]:
                if u < v:  # Avoid duplicate edges
                    edges.append((self.graph[u][v], u, v))  # Store (weight, supplier1, supplier2)

        edges.sort(key=lambda x: x[0])  # Sort edges by weight
        
        max_id = max(self.graph.keys())  # Get the highest supplier ID for initializing union-find
        parent = list(range(max_id + 1))  # Create a parent list for union-find
        rank = [0] * (max_id + 1)  # Create a rank list to optimize union-find

        # Helper function to find the root parent of a node with path compression
        def find_parent(i: int) -> int:
            if parent[i] != i:
                parent[i] = find_parent(parent[i])  # Path compression
            return parent[i]

        # Helper function to union two sets
        def union(u: int, v: int):
            u_root = find_parent(u)  # Find root of u
            v_root = find_parent(v)  # Find root of v
            if rank[u_root] < rank[v_root]:
                parent[u_root] = v_root  # Attach smaller rank tree under higher rank tree
            elif rank[u_root] > rank[v_root]:
                parent[v_root] = u_root
            else:
                parent[v_root] = u_root  # Make one as root and increase its rank
                rank[u_root] += 1

        mst_edges = []  # List to store the edges of the MST
        for weight, u, v in edges:
            u_root = find_parent(u)  # Find root of u
            v_root = find_parent(v)  # Find root of v
            if u_root != v_root:  # If they are in different sets, union them
                mst_edges.append((u, v))  # Add edge to MST
                union(u, v)  # Union the two sets

        return mst_edges  # Return the edges of the MST
