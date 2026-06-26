class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:



        def binarySearch(row, target):

            start, mid, end = 0, len(row)//2, len(row) - 1
            

            while start <= end:
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    start = mid + 1
                    mid = (start + end) // 2
                else:
                    end = mid - 1
                    mid = (start + end) // 2
            
            return False
        

        for row in matrix:
            if row[-1] >= target:
                return binarySearch(row, target)
            
        
        return False


            
        
        
