class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumxsum(n1): 
            squareSum = 0; 
            while(n1): 
                squareSum += (n1 % 10) * (n1 % 10); 
                n1 = int(n1 / 10); 
            return squareSum;
    
        p1 = n; 
        p2 = n; 
        while(True): 

        
            p1 = sumxsum(p1); 

        
            p2 = sumxsum(sumxsum(p2)); 
            if(p1 != p2): 
                continue; 
            else: 
                break; 

        return (p1 == 1); 
