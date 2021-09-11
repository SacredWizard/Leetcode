import bisect


class Solution:
    def searchInsert(self, nums, target):
        print(bisect.bisect_left(nums, target))
        beg, end = 0, len(nums)
        while beg < end:
            mid = (beg + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                beg = mid + 1
        return beg


if __name__ == "__main__":
    print(Solution().searchInsert([1, 3, 5, 6], 5))
    print(Solution().searchInsert([1, 3, 5, 6], 0))
    print(Solution().searchInsert([1, 3, 5, 6], 2))
    print(Solution().searchInsert([1, 3, 5, 6], 7))
    print(Solution().searchInsert([1], 0))
