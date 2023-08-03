import heapq

# Create an empty heap
heap = []

# Add elements to the heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)

# Print the original heap
print("Original Heap:", heap)

# Insert a value into the heap
value = 7
heap.append(value)
heapq.heapify(heap)

# Print the updated heap
print("Updated Heap:", heap)