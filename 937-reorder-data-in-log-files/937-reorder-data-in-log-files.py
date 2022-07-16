class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #split logs
        
        letterLog = []
        digitLog = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digitLog.append(log)
            else:
                letterLog.append(log)
        
        #First, sort letterLog by identifiers
        #(will be overwritten by lex sort if not same)
        letterLog.sort(key = lambda x: x.split()[0])
        
        #Lex sort
        letterLog.sort(key = lambda x: x.split()[1:])
        
        return letterLog + digitLog
        