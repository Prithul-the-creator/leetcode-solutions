class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1: return s
        rows = [[] for row in range(numRows)]


        i = 0
        currentRow = 0
        decreasing = False

        while i < len(s):
            if (currentRow + 1) % numRows == 0 and i != 0:
                decreasing = True
            if currentRow == 0:
                decreasing = False

            rows[currentRow].append(s[i])
            i += 1
            if not decreasing:
                currentRow += 1
            else:
                currentRow -= 1
        
        return "".join(["".join(x) for x in rows])

            
