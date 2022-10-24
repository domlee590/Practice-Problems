class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        '''
        from collections import defaultdict
        
        userSite = defaultdict(list)
        
        for i in range(len(username)):
            userSite[username[i]].append((timestamp[i], website[i]))
            
        for user in userSite.keys():
            userSite[user].sort()
        
        triples = defaultdict(int)
        for sites in userSite.values():
            if len(sites) >= 3:
                sequences = self.formSequences(sites)
                for seq in sequences:
                    triples[seq] += 1
        
        highScore = max(triples.values())
        candidates = []
        for triple, score in triples.items():
            if score == highScore:
                candidates.append(triple)
        
        candidates.sort()
        print(triples)
        return candidates[0]
        
    def formSequences(self, sites):
        res = []
        for i in range(len(sites) - 2):
            for j in range(i+1, len(sites) - 1):
                for k in range(j+1, len(sites)):
                    res.append((sites[i][1], sites[j][1], sites[k][1]))
        
        return res
        '''

        
        users = defaultdict(list)
    
        for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0],x[1])): 
            users[user].append(site)

        patterns = Counter()

        for user, sites in users.items():
            patterns.update(Counter(set(combinations(sites, 3))))

        return max(sorted(patterns), key=patterns.get)