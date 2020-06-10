import collections
import time

current_id = 0


def next_id():
    global current_id
    result = current_id
    current_id += 1

    return result


class Solution(object):
    def criticalConnections(self, n, connections):
        visited = set()
        disc = {}
        low = {}
        graph = collections.defaultdict(list)

        for src, dest in connections:
            graph[src].append(dest)
            graph[dest].append(src)

        result = []

        def visit(node, parent):
            visited.add(node)
            node_id = next_id()
            disc[node] = node_id
            low[node] = node_id
            # cycle_ids[cycle_id].add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visit(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > disc[node]:
                        result.append([node, neighbor])
                elif neighbor != parent:
                    low[node] = min(low[node], disc[neighbor])

        visit(0, -1)

        return result


if __name__ == '__main__':
    Solution().criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])
