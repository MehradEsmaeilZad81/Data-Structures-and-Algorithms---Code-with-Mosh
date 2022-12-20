class Node:
    def __init__(self, value):
        self._value = value
        self._next = None


class LinkedList(object):
    def __init__(self, head=None):
        self._head = head
        self._tail = None
        self._size = 0

    def _isEmpty(self):
        if self._head == None:
            return True
        return False

    def addLast(self, item):
        node = Node(item)
        if self._isEmpty():
            self._head = node
            self._tail = node
        else:
            self._tail._next = node
            self._tail = node
        self._size += 1

    def addFirst(self, item):
        node = Node(item)
        if self._isEmpty():
            self._head = node
            self._tail = node
        else:
            node._next = self._head
            self._head = node
        self._size += 1

    def indexOf(self, item):
        if not self._isEmpty():
            index = 0
            current = self._head
            while current:
                if current._value == item:
                    return index
                index += 1
                current = current._next
        return -1

    def contains(self, item):
        if not self._isEmpty():
            current = self._head
            while current:
                if current._value == item:
                    return True
                current = current._next
        return False
        # return self.indexOf(item) != -1 !!

    def removeFirst(self):
        if not self._isEmpty():
            if self._head == self._tail:
                self._head = None
                self._tail = None
            else:
                self._head = self._head._next
            self._size -= 1
        else:
            raise RuntimeError('List is empty')

    def _getPrevious(self, node):
        current = self._head
        while current:
            if current._next == node:
                return current
            current = current._next

    def removeLast(self):
        if not self._isEmpty():
            if self._head == self._tail:
                self._head = None
                self._tail = None
            else:
                previous = self._getPrevious(self._tail)
                self._tail = previous
                self._tail._next = None
            self._size -= 1
        else:
            raise RuntimeError('List is empty')
        
    def size(self):
        return self._size
    
    def __str__(self):
        current = self._head
        output = ''
        while current:
            output += str(current._value) + ' '
            current = current._next
        return output


# Test
list = LinkedList()
list.addLast(10)
list.addLast(20)
list.addFirst(40)
list.addLast(30)
print(list)
print(list.indexOf(10))
print(list.contains(20))
print('size:',list.size())
list.removeFirst()
print(list)
list.removeLast()
print('size:',list.size())
print(list)
# Output: 40 10 20 30
# Output: 1
# Output: True
# Output: size: 4
# Output: 10 20 30
# Output: size: 2
# Output: 10 20
