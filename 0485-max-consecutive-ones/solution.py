class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:


            def solution(l, r):

                if l - r == 0:
                    return nums[l], nums[l], nums[l]
                
                mid = l + (r - l)//2
                ll, lr, lmax = solution(l, mid)
                rl, rr, rmax = solution(mid + 1, r)

                if ll == mid - l + 1: ll += rl
                if rr == r - (mid + 1) + 1: rr += lr
                return ll, rr, max(lr + rl, lmax, rmax)
            
            return solution(0, len(nums) - 1)[2]
