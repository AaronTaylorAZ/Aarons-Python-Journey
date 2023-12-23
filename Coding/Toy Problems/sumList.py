# sumArray
# /*
#  * Given an array of numbers, calculate the greatest contiguous sum of numbers in it.
#  * A single array item will count as a contiguous sum.
#  *
#  * example 1: sumArray([1, 2, 3]); // => 6
#  * example 2: sumArray([1, 2, 3, -4]); // 6
#  * example 3: sumArray([1, 2, 3, -4, 5]); // 7
#  * example 4: sumArray([4, -1, 5]); // => 8
#  * example 5: sumArray([10, -11, 11]); // 11
#  */

def sumArray(list):
    largestsum = 0
    currentsum = 0
    for i in range(len(list) - 1):
        print("if", list[i],"is greater than or equal to 0 or", list[i+1], "is less than",list[i])
        if list[i] >= 0 or list[(i+1)] > list[i]:
            print(currentsum, "plus equals ", list[i])
            currentsum += list[i]
        if list[len(list)-1]:
            currentsum += list[(i+1)]
        if currentsum > largestsum:
            print("else if ", currentsum, "is greater than ", largestsum)
            largestsum = currentsum
    print(currentsum, largestsum)
    return largestsum
        
        
print(sumArray([1,2,3,-7,8]))