"""The idea is to sort the array in non-decreasing order.
Now, we know that the largest element will be at index (n - 1).
So, starting from index (n - 2), traverse the remaining array in reverse order.
As soon as we encounter an element which is not equal to the largest element,
return it as the second largest element in the array.
If all the elements are equal to the largest element, return -1."""

#Time Complexity: O(n*logn),as sorting the array takes O(n*logn) time and traversing the array can take O(n) time in the worst case, so total time complexity = (n*logn + n) = O(n*logn).
#Auxiliary space: O(1), as no extra space is required."""

def getSecondLargest(arr):
    n = len(arr)
    
    # Sort the array in non-decreasing order
    arr.sort()
  
    # start from second last element as last element is the largest
    for i in range(n - 2, -1, -1):
      
        # return the first element which is not equal to the largest element
        if arr[i] != arr[n - 1]:
            return arr[i]
    
    # If no second largest element was found, return -1
    return -1

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))