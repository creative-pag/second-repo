def selection_sort(data):
    n = len(data)
    for i in range (0,n-1):
        mid_index = i
        for j in range(i+1,n):
            if data[mid_index] > data[j]:
                mid_index= j
        temp = data[i]
        data[i] = data[mid_index]
        data[mid_index] = temp
    return data
marks = [10,20,15,14,20,5,19,16]
print("datataset before selection sort",marks)
sorted_marks = selection_sort(marks)
print("dataset after selection sort",sorted_marks)