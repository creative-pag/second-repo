def mergesort(alist):
    if len(alist) >1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i= j= k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i+=1
            else:
                alist[k]= righthalf[j]
                j+=1
            k+=1
        while i< len(lefthalf):
            alist[k] = lefthalf[i]
            i+=1
            k+=1
        while j< len(righthalf):
            alist[k]= righthalf[j]
            j+=1
            k+=1
        return alist
marks = [1,8,5,13,75,16,20] 
result = mergesort(marks)
print(result)
# merge sort --
