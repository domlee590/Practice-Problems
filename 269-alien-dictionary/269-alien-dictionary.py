class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # Generate adjacency list, first to second letters
        adj = { char:set() for word in words for char in word }
        
        # Indegree tracking
        indegree = {char:0 for word in words for char in word}
        
        # Go through pairs
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))
            
            # Check for invalid word pair
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            
            # Find first differing char
            for c in range(minLen):
                if word1[c] != word2[c]:
                    if word2[c] not in adj[word1[c]]:
                        adj[word1[c]].add(word2[c])
                        indegree[word2[c]] += 1
                    break
        
        # Explore all letters to get topological ordering
        q = collections.deque()
        for letter, indeg in indegree.items():
            if indeg == 0:
                q.append(letter)
        
        order = ""
        while len(q) > 0:
            curLetter = q.popleft()
            
            order += curLetter
            
            for nextLetter in adj[curLetter]:
                indegree[nextLetter] -= 1
                if indegree[nextLetter] == 0:
                    q.append(nextLetter)
                    
        return order if len(order) == len(indegree.keys()) else ""