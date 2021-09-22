from collections import deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        result = list()

        for i, j in prerequisites:
            adj_list[j].append(i)
            indegree[i] += 1

        queue = deque([i for i, d in enumerate(indegree) if d == 0])
        while queue:
            val = queue.popleft()
            result.append(val)
            numCourses -= 1
            for i in adj_list[val]:
                indegree[i] -= 1
                if not indegree[i]:
                    queue.append(i)
        if not numCourses:
            return result
        else:
            return []


if __name__ == "__main__":
    print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
