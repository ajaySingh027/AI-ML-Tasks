import time

def quicksort(array):
    if len(array) < 2:
        return array
    
    else:
        # selecting the first element as pivot
        pivot = array[0]

        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return (quicksort(less) + [pivot] + quicksort(greater))

t1 = time.time()
res = quicksort([1, 6, 8, 3, 4, 2, 9])
print("time: {}".format(time.time() - t1))
print(res)
    