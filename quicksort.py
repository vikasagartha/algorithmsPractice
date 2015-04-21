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
