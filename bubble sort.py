class Solution:
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n):
            a = i
            for j in range(i+1, n):
                if arr[j] < arr[a]:
                    a = j
            arr[i], arr[a] = arr[a], arr[i]
        return arr
