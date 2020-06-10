opened = ["(", "[", "{"]
closed = [")", "]", "}"]
pairs = list(zip(opened, closed))


def is_open(paren):
    return paren in opened


def is_close(paren):
    return paren in closed


def is_match(o_paren, c_paren):
    return (o_paren, c_paren) in pairs


class Solution:
    def isValid(self, s: str) -> bool:
        opened_stack = []
        for char in s:
            if is_open(char):
                opened_stack.append(char)
            elif is_close(char):
                if len(opened_stack) == 0:
                    return False

                current_open = opened_stack.pop()
                if not is_match(current_open, char):
                    return False
            else:
                return False

        return len(opened_stack) == 0


if __name__ == '__main__':
    for inpt in [
        "()",
        "()[]{}",
        "(]",
        "([)]"
    ]:
        print(Solution().isValid(inpt))