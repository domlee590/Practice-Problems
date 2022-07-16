class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1, map2 = dict(), dict()
        
        for n in nums1:
            map1[n] = map1.get(n, 0) + 1
        for n in nums2:
            map2[n] = map2.get(n, 0) + 1
        
        res = []
        for key in map1.keys():
            if key in map2.keys():
                for _ in range(min(map1[key], map2[key])):
                    res.append(key)
                           
        return res