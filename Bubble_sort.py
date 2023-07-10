import random
unsorted = [4,1,2,6,3,5]
swaps = 1
passes = 0
temp = 0

print(f"original array is {unsorted}")
while swaps != 0:
    swaps = 0
    for i in range(0,len(unsorted)-1):   
        temp = unsorted[i]

        if unsorted[i] > unsorted[i+1]:
            unsorted[i] = unsorted[i+1]
            unsorted[i+1] = temp
            swaps +=1
            print(f"{unsorted} swapped")
        else:
            print(f"{unsorted} No swap")    
    passes+=1
    if swaps != 0:
        print(f"Pass {passes} is complete with {swaps} swaps in this pass")
        print(f"The array is {unsorted}")
    else:
        print(f"Sorted Array: {unsorted}")