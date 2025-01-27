from collections import defaultdict


class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):

        # Bước 1: Xây dựng đồ thị
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        # Hàm DFS để kiểm tra xem có đường từ u đến v không
        def dfs(u, target, visited):
            if u == target:
                return True
            visited.add(u)
            for neighbor in graph[u]:
                if neighbor not in visited and dfs(neighbor, target, visited):
                    return True
            return False

        # Bước 2: Trả lời các truy vấn
        result = []
        for u, v in queries:
            result.append(dfs(u, v, set()))
        return result

        