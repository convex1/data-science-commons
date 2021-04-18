def removeDuplicates(nums):

    # O(n log n)
    nums.sort()

    start_index = 0
    end_index = 1
    len_nums = len(nums)

    # O(n)
    while end_index < len_nums:

        if nums[start_index] == nums[end_index]:
            del nums[end_index]
            len_nums -= 1
            continue

        start_index += 1
        end_index += 1

    return nums, len(nums)


print("Unique elements of array with it's length: ", removeDuplicates([1,1,2]))