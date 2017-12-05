array_A = [1,5,3,0,6,8,4,2,7,9]
print(array_A, "Length = ", len(array_A))

for i in range(1, len(array_A)):
    key = array_A[i]
    j = i - 1
    while j > 0 and array_A[j] > key:
        array_A[i] = array_A[j]
        array_A[j] = key
        j = j - 1
print(array_A)