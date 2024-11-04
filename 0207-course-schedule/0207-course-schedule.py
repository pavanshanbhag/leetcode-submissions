from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        top_order = []
        graph = defaultdict(list)
        indegree = [0] * numCourses
        # Build Graph
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            indegree[pair[0]] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
     
        while queue:
            node = queue.popleft()
            top_order.append(node)
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        return len(top_order) == numCourses