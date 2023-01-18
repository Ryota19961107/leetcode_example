class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low_ram, high_ram = low % 2, high % 2
        if low_ram == 0 and high_ram == 0:
            return (high - low) // 2
        else:
            return (high - low) // 2 + 1