n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
left, right = 0, n-1
count = 0

while left < right:
    if arr[left] + arr[right] == x:
        count += 1
        left += 1
        right -= 1
    elif arr[left] + arr[right] < x:
        left += 1
    else:
        right -= 1

print(count)