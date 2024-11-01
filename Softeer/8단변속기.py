# https://softeer.ai/practice/6283

import sys

nums = list(map(int, sys.stdin.readline().split()))

if all(nums[i]+1 == nums[i+1] for i in range(7)):
    print('ascending')
elif all(nums[i]-1 == nums[i+1] for i in range(7)):
    print('descending')
else:
    print('mixed')