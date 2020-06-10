class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        result = []
        index = self
        while index is not None:
            result.append(index.val)
            index = index.next

        return repr(result)


def has_next(list_node: ListNode):
    return list_node.next is not None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i1 = l1
        i2 = l2
        r_val = i1.val + i2.val
        carry = r_val >= 10
        r_val = r_val % 10
        result = ListNode(r_val, None)
        r = result
        while has_next(i1) or has_next(i2):
            i1 = i1.next or ListNode(0, None)
            i2 = i2.next or ListNode(0, None)
            r_val = i1.val + i2.val
            if carry:
                r_val += 1
            carry = r_val >= 10
            r_val = r_val % 10
            r.next = ListNode(r_val, None)
            r = r.next

        if carry:
            r.next = ListNode(1, None)

        return result


if __name__ == '__main__':
    def create_linked_list(lst) -> ListNode:
        if len(lst) == 0:
            return None

        result = ListNode(lst[0], None)
        index = result
        for i in range(1, len(lst)):
            val = lst[i]
            node = ListNode(val, None)
            index.next = node
            index = node

        return result

    i1 = create_linked_list([2, 4, 3])
    i2 = create_linked_list([5, 6, 4])
    i3 = Solution().addTwoNumbers(i1, i2)
    print(i3)