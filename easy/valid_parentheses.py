class Solution:
    def isValid(self, s):
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in pairs:
                if len(stack) == 0 or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0
