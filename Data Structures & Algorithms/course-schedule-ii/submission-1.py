class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        prereqs = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        visited = set()
        cycle = set()

        def dfs(root_course):
            if root_course in visited:
                return True
            if root_course in cycle:
                return False
            
            cycle.add(root_course)

            for prereq in prereqs[root_course]:
                if not dfs(prereq):
                    return False
            
            cycle.remove(root_course)
            visited.add(root_course)
            output.append(root_course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
        
        


        
            






        