"""One pass search method:
The approach is to traverse the array twice.
In the first traversal, find the maximum element.
In the second traversal, find the maximum element ignoring the one we found in the first traversal."""
"""Time Complexity: O(2*n) = O(n), as we are traversing the array only once.
Auxiliary space: O(1), as no extra space is required."""

# Python program to find the second largest element in the array
# using two traversals

# Function to find the second largest element in the array
def getSecondLargest(arr):
    n = len(arr)
    
    #return -1 when length of array is less than 2 as there wont be any second largest element
    if n<2 :
        return -1
    
    largest = secondLargest = float('-inf') #initialize to negative infinity
    
    #finding the second largest element
    for num in arr:
        # If arr[i] > largest, update second largest with largest and largest with arr[i]
        if num > largest:
            secondLargest = largest
            largest = num
        #ignore the one we found in the first traversal and check for others in arr[i] and update secondLargest
        elif num > secondLargest and num != largest:
            secondLargest = num
    
    #To check if there exist other unique element rather than single largest. Example: arr[i] = [10,10,10,10]
    if secondLargest == float('-inf'):
        return -1
    else:    
        return secondLargest

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))