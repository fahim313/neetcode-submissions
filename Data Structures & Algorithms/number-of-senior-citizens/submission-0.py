class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            age_str = i[11:13]
            age = int(age_str)

            if age>60:
                count += 1
        return count     

        
              
        