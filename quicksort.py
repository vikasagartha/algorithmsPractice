'''
Algorithm:
    1. Right most elmeent is the pivot 
    2. Create a 'wall' at the front of the list
        - to the left are elements < pivot, to the right are elements > pivot 
        - the wall is not an index, it is a location b/n indices. Hence, keep a 'rightOfWall' index rather than an index
    3. Iterate over all elements, except the final element which because that is the pivot
        - if larger, continue
        - if smaller, place to the right of the wall and shift the all one step to the right 
    4. Place the pivot to the right of the wall by swapping it with the element to the right of the wall
    5. Recurse

Running Time: O(n^2) worst case, best case O(nlogn)
'''
def swap(index1, index2, arr):
    arr[index1], arr[index2] = arr[index2], arr[index1]
    return arr
def recursiveQuicksort(nums):
    l = len(nums)
    if(l<=1):
        #print "array: ", nums
        return nums
    else:
        #print "array: ", nums,
        lastIndex = l-1
        pivotIndex = lastIndex 
        pivot = nums[pivotIndex]
        #print "pivot: ", pivot,
        rightOfWall = 0
        for index in range(rightOfWall, pivotIndex):
            if(nums[index]>=pivot):
                continue
            else:
                nums = swap(rightOfWall, index, nums)
                rightOfWall = rightOfWall + 1
        nums = swap(rightOfWall, pivotIndex, nums) 
        left = nums[0:rightOfWall]
        right = nums[rightOfWall+1:l]
        #print ", left: ",left, ", right: ",right
        return recursiveQuicksort(left) + [pivot] + recursiveQuicksort(right)

numbers = raw_input("Enter numbers to be quicksorted (separated by space): ")
sortedArray = recursiveQuicksort(map(int, numbers.split(' ')))
output = ' '.join(map(str, sortedArray))
print output
