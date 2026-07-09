class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum,pro=0,1
        while n>0:
            r=n%10
            pro*=r
            sum+=r
            n//=10

        return pro-sum