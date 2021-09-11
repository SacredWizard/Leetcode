class Solution:
    def search(self, nums, target) -> int:
        length = len(nums)
        low, high = 0, length - 1

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        start = low
        low, high = 0, length - 1

        if nums[start] <= target <= nums[high]:
            low = start
        else:
            high = start

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1


if __name__ == "__main__":
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
