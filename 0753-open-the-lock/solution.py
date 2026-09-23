class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:

        if "0000" in deadends:
            return -1
        visited = set()
        visited.update(deadends)
        q = deque()
        q.append(("0000", 0))

        while q:

            current_node, moves = q.popleft()

            if current_node == target:
                return moves
            
            for i in range(4):
                option1 = current_node[:i] + str((int(current_node[i]) + 1) % 10) + current_node[i + 1:]
                option2 = current_node[:i] + str((int(current_node[i]) - 1) % 10) + current_node[i + 1:]
                if option1 not in visited:
                    q.append((option1, moves + 1))
                    visited.add(option1)
                if option2 not in visited:
                    q.append((option2, moves + 1))
                    visited.add(option2)
        return -1


        




