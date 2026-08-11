class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        cache = {}
        add = 0

        def recurse(n, turn):
            nonlocal add

            if n <= 0:
                return not turn

            if (n, turn) in cache:
                return cache[(n, turn)]

            results = set()

            for i in range(1, int(n ** 0.5) + 1):
                if recurse(n - i * i, not turn) == turn:
                    cache[(n, turn)] = turn
                    return turn

            if turn in results:
                result = turn
            else:
                result = not turn

            cache[(n, turn)] = result
            return result

        r = recurse(n, True)
        print(add)
        return r
