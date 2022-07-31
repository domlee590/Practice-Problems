class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #In-degree tracker: check how many pre-requisites a dependent course has
        inDegree = [0 for _ in range(numCourses)]
        
        # Pre-requisite -> Dependent courses map
        preqMap = [list() for _ in range(numCourses)]
        for dependentCourse, preq in prerequisites:
            preqMap[preq].append(dependentCourse)
            inDegree[dependentCourse] += 1
        
        # Create queue for Kahn's algorithm, adding free classes 
        # (no pre-req, indegree of 0)
        q = collections.deque()
        for course in range(numCourses):
            if inDegree[course] == 0:
                q.append(course)
        
        # Repeatedly remove courses with satisfied prerequisites from the graph
        # Add the new courses whose prerequisites became met
        taken = 0
        while len(q) > 0:
            course = q.popleft()
            taken += 1
            print(course)

            # Pre-req taken, decrease indegree
            for dependentCourse in preqMap[course]:
                inDegree[dependentCourse] -= 1
                
                # If now free to take (all pre-reqs taken)
                if inDegree[dependentCourse] == 0:
                    q.append(dependentCourse)
        
        return True if taken == numCourses else False
            