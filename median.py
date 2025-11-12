arr = [10, 40, 30, 20, 50]
arr.sort()
n = len(arr)
if n % 2 != 0:
    median = arr[int(n /2)]
else:
    median = (arr[int(n/2)- 1] + arr[int(n/2)]) / 2
print("median is :", median)
#middle value in a sorted list, formula n+1/2 th element or n+1/2 +1
