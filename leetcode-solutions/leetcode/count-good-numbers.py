class Solution:
    def countGoodNumbers(self, n: int) -> int:

        if n == 1:
            return 5 
        odd = n//2
        if n % 2==1:
            even = n//2+1
        else:
            even = n//2
        
        def power(num,a):
            if a == 1:
                return num
            if a % 2==1:
                return num*power((num*num) % (10**9+7),a//2)
            else:
                return power((num*num) % (10**9+7),a//2)
        return (power(5,even) * power(4,odd)) % (10**9+7)


            
    

