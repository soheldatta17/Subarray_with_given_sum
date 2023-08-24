class Solution:
    def subArraySum(self,arr, n, s):
        if s in arr:
            b=arr.index(s)
            return [b+1,b+1]
	    sum = arr[0]
	    start = 0
	    i = 1
	    while i <= n:
         while sum > s and start < i-1:
	            sum -= arr[start]
	            start += 1
		      if sum == s:
		           return [start+1,i]
		      if i < n:
		           sum = sum + arr[i]
		      i += 1
	    return [-1]