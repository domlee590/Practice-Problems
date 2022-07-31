class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Use Kahn's algorithm for topsort to generate array
        
        # Initialize map (array) for indegree of each course
        # The indegree will be the number of prerequisites a course has
        indegree = [0 for _ in range(numCourses)]
        
        # Generate a map, prerequisite -> dependent courses
        preqToDependent = [[] for _ in range(numCourses)]
        for dependent, preq in prerequisites:
            preqToDependent[preq].append(dependent)
            # Add to indegree of the dependent course
            indegree[dependent] += 1
        
        # Initialize a queue to store "free" courses without dependencies
        q = collections.deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
                
        # Repeatedly "remove" prerequisites by "taking" the class once it has an indegree of 0
        # Track this order in a list
        taken = []
        while len(q) > 0:
            course = q.popleft()
            taken.append(course)
            
            # By taking the course, the indegrees of its dependents decrease
            for dependent in preqToDependent[course]:
                indegree[dependent] -= 1
                # Check if a dependent course is now free to be taken
                if indegree[dependent] == 0:
                    q.append(dependent)
                    
        # Check if all courses have been taken
        return taken if len(taken) == numCourses else []