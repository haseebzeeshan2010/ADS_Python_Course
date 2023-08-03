import heapq

# Creating a heap
heap = []

# Adding elements to the heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)

# Searching for an element in the heap
element = 10
if element in heap:
    print(f"{element} found in the heap")
else:
    print(f"{element} not found in the heap")