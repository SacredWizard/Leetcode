from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for i, j in prerequisites:
            adj_list[j].append(i)
            indegree[i] += 1

        queue = deque([i for i, d in enumerate(indegree) if d == 0])
        while queue:
            val = queue.popleft()
            numCourses -= 1
            for i in adj_list[val]:
                indegree[i] -= 1
                if not indegree[i]:
                    queue.append(i)
        if not numCourses:
            return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().canFinish(2, [[1, 0]]))
