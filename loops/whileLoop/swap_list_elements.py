# swap the list elements with there adjusting index with out using slicing

L = [11,20,12,45,67,89]

i = 0
while i<len(L)-1:
    L[i],L[i+1] = L[i+1],L[i]
    i += 2
print(L)