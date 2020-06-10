from typing import Union


class DoubleLinkedList(object):
    def __init__(self, key: Union[int, str], val: int, prev=None, after=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.after = after

    def __repr__(self):
        if self.key == "head":
            return "{}: {}. After: {}".format(self.key, self.val, self.after.key)
        elif self.key == "tail":
            return "{}: {}. Prev: {}.".format(self.key, self.val, self.prev.key)
        else:
            return "{}: {}. Prev: {}. After: {}".format(self.key, self.val, self.prev.key, self.after.key)

    @staticmethod
    def create_list():
        head = DoubleLinkedList("head", -1)
        tail = DoubleLinkedList("tail", -1)
        head.after = tail
        tail.prev = head

        return head, tail


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        head, tail = DoubleLinkedList.create_list()
        self.head = head
        self.tail = tail

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove_node(node)
        self.insert_at_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_node(node)
            self.insert_at_front(node)
        else:
            node = DoubleLinkedList(key, value)
            self.cache[key] = node
            self.insert_at_front(node)
            if len(self.cache) > self.capacity:
                node = self.remove_from_back()
                del self.cache[node.key]

    def remove_node(self, node):
        prev = node.prev
        after = node.after
        prev.after = after
        after.prev = prev

        node.prev = None
        node.after = None

    def insert_at_front(self, node):
        node.prev = self.head
        node.after = self.head.after
        self.head.after.prev = node
        self.head.after = node

    def remove_from_back(self):
        node = self.tail.prev
        node.prev.after = self.tail
        self.tail.prev = node.prev
        node.prev = None
        node.after = None

        return node

    def __repr__(self):
        index = self.head
        lst = []
        while index is not None:
            lst.append(str(index.key))
            index = index.after

        return "LRUCache(cache={}, keys={})".format(repr(self.cache), "[{}]".format(";".join(lst)))


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    cache.get(2)