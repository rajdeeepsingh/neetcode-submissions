class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if k == 0:
            return False

        left = 0
        window = set()

        for i in range(len(nums)):
            if i - left > k:
                window.remove(nums[left])
                left += 1

            if nums[i] in window:
                return True
            window.add(nums[i])
            
        return False