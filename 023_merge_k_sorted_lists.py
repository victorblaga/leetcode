from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        index = self
        vals = []
        while index is not None:
            vals.append(str(index.val))
            index = index.next

        return "->".join(vals)


def append(head, tail, val):
    if head is None:
        head = ListNode(val)
        return head
    else:
        node = ListNode(val)
        tail.next = node

        return tail


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists is None or len(lists) == 0:
            return None

        heap = list([(lists[i].val, i) for i in range(len(lists))])
        heapq.heapify(heap)
        head = tail = None

        while len(heap) > 0:
            list_val, lst_idx = heapq.heappop(heap)
            lst = lists[lst_idx]
            node = ListNode(list_val)
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node

            lst = lst.next
            if lst is not None:
                lists[lst_idx] = lst
                heapq.heappush(heap, (lst.val, lst_idx))

        return head


if __name__ == '__main__':
    def make_list(lst: List[int]):
        if len(lst) == 0:
            return None
        head = ListNode(lst[0])
        tail = head
        for val in lst[1:]:
            node = ListNode(val)
            tail.next = node
            tail = node

        return head

    l1 = make_list([1, 4, 5])
    l2 = make_list([1, 3, 4])
    l3 = make_list([2, 6])
    Solution().mergeKLists([l1, l2, l3])
