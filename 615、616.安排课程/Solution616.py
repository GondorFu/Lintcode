class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {int[]} the course order
    def findOrder(self, numCourses, prerequisites):
        # Write your code here
        indegree  = [0 for i in range(numCourses)] 
        preCourse = [[] for i in range(numCourses)]
        for v in prerequisites:
            preCourse[v[1]].append(v[0])
            indegree[v[0]] += 1
        q = list()
        for i, v in enumerate(indegree):
            if v == 0:
                q.append(i)
        res = list()
        while len(q) > 0:
            i = q.pop()
            res.append(i)
            for v in preCourse[i]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        if len(res) < numCourses:
            return []
        else:
            return res