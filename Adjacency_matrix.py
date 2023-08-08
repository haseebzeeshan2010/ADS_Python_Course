# Define the number of vertices in the graph
num_vertices = 4

# Create an empty adjacency matrix
adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

# Add edges to the adjacency matrix
adjacency_matrix[0][1] = 1
adjacency_matrix[0][2] = 1
adjacency_matrix[1][0] = 1
adjacency_matrix[1][2] = 1
adjacency_matrix[1][3] = 1
adjacency_matrix[2][0] = 1
adjacency_matrix[2][1] = 1
adjacency_matrix[2][3] = 1
adjacency_matrix[3][1] = 1
adjacency_matrix[3][2] = 1

# Print the adjacency matrix
for row in adjacency_matrix:
    print(row)