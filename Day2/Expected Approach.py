"""One Traversal - O(n) Time and O(1) Space
The idea is similar to the two traversals approach where we took a pointer, say count to track where the next non-zero element should be placed.
However, on encountering a non-zero element, instead of directly placing the non-zero element at arr[count], we will swap the non-zero element with arr[count].
This will ensure that if there is any zero present at arr[count], it is pushed towards the end of array and is not overwritten.
Time Complexity: O(n), as we are traversing the array only once.
Auxiliary Space: O(1)
"""

class Solution:
	def pushZerosToEnd(self,arr):
	    count=0
	    for i in range(len(arr)):
	        if arr[i] != 0:
	            #temp=arr[i]
	            #arr[i]=arr[count]
	            #arr[count]=temp
	            #below is concise expression of wap you can do above 3 steps aswell
	            arr[i],arr[count]=arr[count],arr[i]
                count+=1