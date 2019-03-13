class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        size = len(pushed)
        value = 0
        
        for i in range(size):
            if stack and popped[i] == stack[-1]:
                stack.pop()
            else:  
                while value < size and pushed[value] != popped[i]:
                    stack.append(pushed[value])
                    value = value + 1
                value = value + 1  
        return not stack
                
