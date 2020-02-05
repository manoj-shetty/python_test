import sys
del sys.argv[0]

test_arr = [64, 34, 25, 12, 22, 11, 90]

print(test_arr)
arr_len = len(test_arr)
i = 0
count = 0
while i < arr_len -1:
    if int(test_arr[i]) > int(test_arr[i+1]):
        test_arr[i], test_arr[i+1] = int(test_arr[i+1]), int(test_arr[i])
        # print("--->", end=" ")
        # print(test_arr)
        i = -1
    i += 1
    count += 1

print(test_arr)
print(count)

def bubbleSort(arr):
    n = len(arr)
    count1 = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
            count1 += 1
    print(count1)
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
print (arr)
