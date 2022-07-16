class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig = len(digits) - 1
        
        while digits[dig] == 9 and dig >= 0:
            digits[dig] = 0
            dig -= 1
        
        if dig == -1:
            return [1] + digits
        else:
            digits[dig] += 1
            return digits
        
        