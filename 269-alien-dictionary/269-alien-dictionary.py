class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # Generate adjacency list, first to second letters
        adj = { char:set() for word in words for char in word }
        
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
                    adj[word1[c]].add(word2[c])
                    break
            
        # Explore all letters to get topological ordering
        stack = []
        visited = {} # True = Current Path, False = Completed, Absent = Unvisited
        
        def dfsTopsort(letter):
            # Check if letter is in current path (cycle if True)
            if letter in visited:
                return visited[letter]
            
            visited[letter] = True

            # Recur for all subsequent letters
            for nextLetter in adj[letter]:
                if dfsTopsort(nextLetter):
                    return True # Cycle found

            # Postorder append afer subsequent letters added
            visited[letter] = False # Letter complete
            stack.append(letter)
        
        for letter in adj.keys():
            if dfsTopsort(letter):
                return ""
        
        return "".join(stack[::-1])