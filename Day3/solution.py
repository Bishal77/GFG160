class Solution:
    def reverseArray(self, arr):
        
        for i in range(len(arr)//2):
            temp=arr[i]
            arr[i]=arr[len(arr)-i-1]
            arr[len(arr)-i-1]=temp
            
        