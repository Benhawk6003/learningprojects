def solution(list_nums, num):
    j = len(numbers) - 1

    for i in range(len(numbers)):
        num_sum = numbers[i] + numbers[j]

        if num_sum < k:
            i += 1
        elif num_sum > k:
            j -= 1
        else:
            return True

    return False


k = 17
numbers = [10, 15, 3, 7]
numbers.sort()

print(solution(numbers, k))

