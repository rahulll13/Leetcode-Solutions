class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## base case : length checking 
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        

## S = abc
## T = abcd
## False

## S = ""
## T = ""
## True

## S = "a"
## T = "a"
### True
## Brute Force:
