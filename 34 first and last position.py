class Solution:

    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        low, high = 0, len(nums) - 1
        result = list()

        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                if mid == 0 or nums[mid - 1] != target:
                    result.append(mid)
                    break
                else:
                    high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    result.append(mid)
                    break
                else:
                    low = mid + 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        if not result:
            return [-1, -1]
        else:
            return result


if __name__ == "__main__":
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
