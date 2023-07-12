def Binary_search(search,key):
    l=0
    h=len(search)-1
    while l <= h:
        mid = (l+h)//2
        mid_element = search[mid]
        

        if key == mid_element:
            return(mid)
        if key < mid_element:
            h = mid - 1
        else:
            l = mid + 1
    return("Not found")


list = [3,6,8,12,14,17,25,29,31,36,42,47,53,55,62]
key = float(input("What do you want to search for? "))


ans = Binary_search(list,key)
print(f"The number {key} is at index {ans}")