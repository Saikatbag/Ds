class Solution:
    def duplicates(self, arr, n):
        a = []
        for i in range(len(arr)):
            if arr.count(arr[i]) >1:
                a.append(arr[i])
        if len(a) >0:
            b=set(a)
            b=list(b)
            b.sort()
            return b
        else:
            a.append(-1)
            return a