class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        total=0
        for details in shift:
            
            if details[0]==0:
                total+=details[1]
            if details[0]==1:
                total-=details[1]
        
        print(total)
        if total<0:
            for index in range(0,abs(total)):
                s=s[-1]+s[0:-1]
        else:
            for index in range(0,total):
                s=s[1:]+s[0]
                
        return s