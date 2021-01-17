def solution():
    for i in range(len(nums)):
        temp_nums = []
        temp_nums.extend(nums)

        nums.remove(i)
        new_nums.append(multiply_nums())


def multiply_nums():
    multiplied = 1
    for i in nums:
        multiplied *= i
    return multiplied


nums = [1, 2, 3, 4, 5]
new_nums = []

solution()
print(new_nums)
