# Create an empty adjacency list
adjacency_list = {}

# Add vertices and their adjacent vertices
adjacency_list[0] = [1, 2]
adjacency_list[1] = [0, 2, 3]
adjacency_list[2] = [0, 1, 3]
adjacency_list[3] = [1, 2]

# Print the adjacency list
for vertex, adjacent_vertices in adjacency_list.items():
    print(f"Vertex {vertex} is adjacent to: {adjacent_vertices}")