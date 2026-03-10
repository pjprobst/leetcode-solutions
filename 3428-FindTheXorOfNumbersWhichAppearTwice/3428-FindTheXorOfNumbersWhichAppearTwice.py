# Last updated: 3/10/2026, 5:51:38 PM
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen = set()
        pairs = []
        for num in nums:
            if num in seen:
                pairs.append(num)
            else:
                seen.add(num)
        if not pairs:
            return 0
        total = pairs[0]
        print(pairs)
        for i in range(1, len(pairs)):
            print(total)
            total = total ^ pairs[i]
        return total
