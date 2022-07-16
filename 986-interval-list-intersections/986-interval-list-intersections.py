class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        intA, intB = 0, 0

        while intA < len(firstList) and intB < len(secondList):
            low = max(firstList[intA][0], secondList[intB][0]) #latest start
            high = min(firstList[intA][1], secondList[intB][1]) #earliest end
            
            if low <= high:
                res.append([low, high])
            
            #pass interval with earliest end
            if firstList[intA][1] < secondList[intB][1]:
                intA += 1
            else:
                intB += 1
        
        return res