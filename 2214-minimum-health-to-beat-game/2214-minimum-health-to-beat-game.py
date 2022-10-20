class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        
        hardest = max(damage)
        total = sum(damage)
        
        if hardest > armor:
            return total - armor + 1
        else:
            return total - hardest + 1