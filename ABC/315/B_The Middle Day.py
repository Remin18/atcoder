M = int(input())
nums = list(map(int, input().split()))

center_day = int((sum(nums) + 1) / 2)
month = 1
for num in nums:
    if center_day > num:
        center_day -= num
        month += 1
    else:
        break

print(*[month, center_day])
