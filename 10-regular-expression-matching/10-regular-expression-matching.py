class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Do a top-down memoization
        cache = {}
        
        def dfs(i, j):
            # Check cache
            if (i, j) in cache:
                return cache[(i,j)]
            
            # i points to s, j points to p
            if i >= len(s) and j >= len(p):
                cache[(i, j)] = True
                return True     # Patterns match
            if j >= len(p):
                cache[(i, j)] = False
                return False    # Patterns cannot match, some s remains but p done
            
            match = (i < len(s)) and (s[i] == p[j] or p[j] == ".") # Check character match or any char "."
            
            # Check for kleene if j is in bounds
            if (j + 1) < len(p) and p[j + 1] == "*": 
                # return SKIP STAR or MATCH 1st AND REPEAT STAR
                cache[(i,j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i,j)]
            
            # Check for simple match
            if match:
                cache[(i,j)] = dfs(i + 1, j + 1)
                return cache[(i,j)]
            
            # If there is no star and characters do not match
            return False
        
        # Call the search
        return dfs(0, 0)