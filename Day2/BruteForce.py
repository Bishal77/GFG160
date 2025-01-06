""" Using Temporary Array - O(n) Time and O(n) Space
The idea is to create a temporary array of same size as the input array arr[].

First, copy all non-zero elements from arr[] to the temporary array.
Then, fill all the remaining positions in temporary array with 0.
Finally, copy all the elements from temporary array to arr[].

Time complexity: O(n), as we are traversing the array three times.
Auxiliary Space : O(n), as we are using a temp[] array to move all the zeros."""

# function to move all zeroes to the end
def pushZerosToEnd(arr):
    n = len(arr)
    temp = [0] * n  
    
    # to keep track of the index in temp[]
    j = 0

    # Copy non-zero elements to temp[]
    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1

    # Fill remaining positions in temp[] with zeros
    while j < n:
        temp[j] = 0
        j += 1

    # Copy all the elements from temp[] to arr[]
    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)

    # Print the modified array
    for num in arr:
        print(num, end=" ")