class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapST, mapTS = dict(), dict()
        
        for sChar, tChar in zip(s, t):
            
            #If we are creating a duplicate mapping in either direction
            if((sChar in mapST and mapST[sChar] != tChar) or
               (tChar in mapTS and mapTS[tChar] != sChar)):
                return False
            
            mapST[sChar] = tChar
            mapTS[tChar] = sChar
        
        return True