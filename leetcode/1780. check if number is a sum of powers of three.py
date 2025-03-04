class Solution:
    result = False

    def checkPowersOfThree(self, n: int) -> bool:
        import math

        def dfs(number, start):
            if number == 0:
                self.result = True
                return
            if number < 0:
                return

            for x in range(start, max_x):
                if visited[x]:
                    continue
                visited[x] = 1
                next_number = number - int(math.pow(3, x))
                dfs(next_number, x)
                visited[x] = 0

        max_x = int(math.log(n, 3)) + 1

        visited = [0] * max_x
        dfs(n, 0)
        return self.result

    def checkPowersOfThree2(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True