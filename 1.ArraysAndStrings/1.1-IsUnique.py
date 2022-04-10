# Given a string, determine if all characters are unique or not.

def is_unique(self, s):
    freq = {}
  
    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            return False
    
    return True
  
  
  
# Follow up: Do so without any additional data structure or space

