"""Two pass search method:
The idea is to keep track of the largest and second largest element while traversing the array.
Initialize largest and second largest with -inf(negative infinity). Now, for any index i,

If arr[i] > largest, update second largest with largest and largest with arr[i].
Else If arr[i] < largest and arr[i] > second largest, update second largest with arr[i]."""
"""Time Complexity: O(n), as we are traversing the array only once.
Auxiliary space: O(1)"""

# Python program to find the second largest element in the array
# using one traversal

# function to find the second largest element in the array
def getSecondLargest(arr):
    n = len(arr)
    
    #return -1 when length of array is less than 2 as there wont be any second largest element
    if n<2 :
        return -1

    largest = secondLargest = float('-inf') #initialize to negative infinity
    

    # finding the second largest element
    for i in range(n):

        # If arr[i] > largest, update second largest with largest and largest with arr[i]
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
      
        # If arr[i] < largest and arr[i] > second largest, 
        # update second largest with arr[i]
        elif arr[i] < largest and arr[i] > secondLargest:
            secondLargest = arr[i]

    return secondLargest

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))
