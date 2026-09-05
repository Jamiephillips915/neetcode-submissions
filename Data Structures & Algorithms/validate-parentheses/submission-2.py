class Solution:
    def isValid(self, s: str) -> bool:
        NormalCount = 0
        SquareCount = 0
        CurlyCount = 0
        stack = []
        head = -1

        if len(s) % 2 == 1:
            return False
        else:
            for i in s:
                if i == "(":
                    NormalCount += 1
                    stack.append("(")
                    head += 1
                elif i == "[":
                    SquareCount += 1
                    stack.append("[")
                    head += 1
                elif i == "{":
                    CurlyCount += 1
                    stack.append("{")
                    head += 1
                elif i == ")":
                    NormalCount -= 1
                    if len(stack) == 0 or stack[head] != "(":
                        return False
                    else:
                        stack.pop(head)
                        head -= 1
                elif i == "]":
                    SquareCount -= 1
                    print(stack)
                    if len(stack) == 0 or stack[head] != "[":
                        return False
                    else:
                        stack.pop(head)
                        head -= 1
                else:
                    CurlyCount -= 1
                    if len(stack) == 0 or stack[head] != "{":
                        return False
                    else:
                        stack.pop(head)
                        head -= 1
            if CurlyCount == 0 and SquareCount == 0 and NormalCount == 0:
                return True
            else:
                return False