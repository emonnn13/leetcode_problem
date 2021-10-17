def sort(arr):
    i = 0
    while i < len(arr):
        # print(i)
        correct = arr[i]-1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i+=1
    # else:
    #     return arr
    return arr 

# a = [0, 2, 1, 3]
a = [3,5,2,1,0]
# a = [5,4,3,2,1,0]

# a = [9,6,4,2,3,5,7,0,1]
r = sort(a)

print(r)

# for i in r:
#     print(f" value -> {i} ")

