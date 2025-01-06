<h1>Move all zeros to end of array</h1>
<h3 align="center">Difficulty: Easy || Accuracy: 45.51%</h3>
<h4 align="center">Company Tags : Paytm, Amazon, Microsoft, Samsung, SAP Labs, Linkedin, Bloomberg</h4>
<br>
<p>You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.</p>

Examples:
Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]<br>
Output: [1, 2, 4, 3, 5, 0, 0, 0]<br>
Explanation: There are three 0s that are moved to the end.
<br><br>
Input: arr[] = [10, 20, 30]<br>
Output: [10, 20, 30]<br>
Explanation: No change in array as there are no 0s.
<br><br>
Input: arr[] = [0, 0]<br>
Output: [0, 0]<br>
Explanation: No change in array as there are all 0s.
<br><br>
Constraints:<br>
1 ≤ arr.size() ≤ 10^5<br>
0 ≤ arr[i] ≤ 10^5
<br><br>
Topic Tags<br>
Arrays, Data Structures
<br><br>
Expected Complexities<br>
Time Complexity: O(n)<br>
Auxiliary Space: O(1)
