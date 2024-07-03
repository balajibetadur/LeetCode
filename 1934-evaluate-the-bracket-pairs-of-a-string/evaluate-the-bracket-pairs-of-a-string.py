class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = dict(knowledge)
        # for key, value in knowledge.items(): s = s.replace(f"({key})", value)
        
        res = ''
        temp = ''
        key_found = False
        for ch in s:
            if ch == '(': key_found = True
            elif ch == ')': 
                res += knowledge.get(temp, '?')
                temp = ''
                key_found = False
            else: 
                if key_found: temp += ch
                else: res += ch
        return res
