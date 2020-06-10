# You
# have
# an
# array
# of
# logs.Each
# log is a
# space
# delimited
# string
# of
# words.
#
# For
# each
# log, the
# first
# word in each
# log is an
# alphanumeric
# identifier.Then, either:
#
# Each
# word
# after
# the
# identifier
# will
# consist
# only
# of
# lowercase
# letters, or;
# Each
# word
# after
# the
# identifier
# will
# consist
# only
# of
# digits.
# We
# will
# call
# these
# two
# varieties
# of
# logs
# letter - logs and digit - logs.It is guaranteed
# that
# each
# log
# has
# at
# least
# one
# word
# after
# its
# identifier.
#
# Reorder
# the
# logs
# so
# that
# all
# of
# the
# letter - logs
# come
# before
# any
# digit - log.The
# letter - logs
# are
# ordered
# lexicographically
# ignoring
# identifier,
# with the identifier used in case of ties.The digit-logs should be put in their original order.
#
# Return
# the
# final
# order
# of
# the
# logs.
#
# Example
# 1:
#
# Input: logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
# Output: ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
#
# Constraints:
#
# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed
# to
# have
# an
# identifier, and a
# word
# after
# the
# identifier.
from typing import List


def is_letter(log: str):
    parts = log.split(" ", 2)
    return not parts[1].isdigit()


def log_msg(log: str):
    parts = log.split(" ", 1)
    return "{}{}".format(parts[1], parts[0])


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        for log in logs:
            if is_letter(log):
                letter.append(log)
            else:
                digit.append(log)

        letter.sort(key=log_msg)
        letter.extend(digit)

        return letter


if __name__ == '__main__':
    print(Solution().reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
