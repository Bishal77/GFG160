"""Two Traversals - O(n) Time and O(1) Space
The idea is to move all the zeros by traversing the array twice.

First Traversal: Shift non-zero elements
Traverse the array and maintain the count of non-zero elements.
This count is initialized with 0 and keeps track of where the next non-zero element should be placed in the array.
If the element is non-zero, place it at arr[count] and increment count by 1.
After traversing all the elements, all non-zero elements will be shifted to the front while maintaining their original order.

Second Traversal: Fill remaining positions with zeros
After the first traversal, all non-zero elements will be at the start of the array and count will store the index where the first zero should be placed.
Iterate from count to the end of array and fill all indices with 0."""

def pushZerosToEnd(arr):
    
    # Count of non-zero elements
    count = 0  

    # If the element is non-zero, replace the element at index 'count' with this element and increment count
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been shifted to the front. Make all elements 0 from count to end.
    while count < len(arr):
        arr[count] = 0
        count += 1

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)
    for num in arr:
        print(num, end=" ")