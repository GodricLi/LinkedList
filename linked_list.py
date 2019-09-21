"""
链表的定义：链表是一种物理存储上非连续，数据元素的逻辑顺序通过链表中的指针链接次序，实现的一种线性存储结构。
链表的特点：链表由一系列节点（链表中每一个元素称为节点）组成，节点在运行时动态生成（malloc），每个节点包括两个部分：
　　　　　　一个是存储数据元素的数据域
　　　　　　另一个是存储下一个节点的地址的指针域
"""


class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.prior = None


class SingleLinkedList:
    """
    单向链表
    """

    def __init__(self, heda=None):
        self._head = heda
        self.length = 0

    def is_empty(self):
        """判断是否为空"""
        return self.length == 0

    def add_tail(self, element):
        """
        尾插法：从尾部添加元素
        :param element:需要添加进去的元素
        :return:
        """
        # 创建一个节点
        node = Node(element)
        if self._head is None:
            self._head = node
        else:
            cur = self._head
            # cur=node,node.next=None
            while cur.next:
                cur = cur.next
            cur.next = node
            return cur.next
        self.length += 1

    def add_head(self, element):
        """
        头插法：从头部插入
        :param element: 需要添加进去的元素
        :return:
        """
        node = Node(element)
        if self._head is None:
            self._head = node
        else:
            node.next = self._head
            self._head = node
        self.length += 1

    def size(self):

        """
        获取链表的大小
        ：return：int
        """
        count = 0
        if self._head is None:
            return count

        else:
            cur = self._head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def insert(self, item: Node, index: int):
        """
        往链表中指定位置插入值
        :param item: 插入的节点
        :param index: 插入的位置
        :return:
        """
        if index < 0 or index > self.length:
            print('index out of range')
            return
        # 构建节点
        if isinstance(item, Node):
            node_insert = item
        else:
            node_insert = Node(item)
        if index == 0:
            node_insert.next = self._head
            self._head = node_insert
        else:
            # 找到index的前一个节点
            pre = self._head
            for i in range(self.length):
                if i == index - 1:
                    node_insert.next = pre.next
                    pre.next = node_insert
                    break
                pre = pre.next
        self.length += 1
        return

    def delete(self, index: int):
        """
        删除指定位置的节点
        :param index: 节点的位置
        :return:
        """
        # 判空
        if self.is_empty():
            print('empty chain')
            return
        if index < 0 or index > self.length:
            print('index out of range')
            return

        if index == 0:
            self._head = self._head.next
        else:
            pre = self._head
            for i in range(self.length):
                if i == index - 1:
                    pre.next = pre.next.next
                    break
                pre = pre.next
        self.length -= 1
        return

    def update(self, item, index: int):
        """
        修改节点item值
        :param item: 修改之后的值
        :param index:节点的位置
        :return:
        """
        # 判空
        if self.is_empty():
            print('empty chain')
            return
        if index < 0 or index >= self.length:
            print('index out of range')
            return

        node = self._head
        for i in range(self.length):
            if i == index:
                node.item = item
                return
            node = node.next

    def get_item(self, index: int):
        """
        获取指定位置的节点item
        :param index:指定位置
        :return:item
        """
        # 判空
        if self.is_empty():
            print('empty chain')
            return
        if index < 0 or index >= self.length:
            print('index out of range')
            return

        node = self._head
        for i in range(self.length):
            if i == index:
                return node.item
            node = node.next

    def traversal(self):
        """链表遍历"""
        if self._head is None:
            return
        else:
            cur = self._head
            while cur:
                print(cur.item)
                cur = cur.next

    def reverse(self):
        """
        单向链表的反转：Input:1>2>3>4>5
                     Output:5>4>3>2>1
        思路：先将head.next断开，即指向断开的元素pre（none）;再将pre赋值head，将head赋值head.next;最后将head赋值pre
        :return:
        """
        if self._head is None or self.size() == 1:
            return
        else:
            pre = None
            cur = self._head
            while cur is not None:
                post = cur.next
                cur.next = pre
                pre = cur
                cur = post
            self._head = pre            # 逆向后的头节点
            self.traversal()


if __name__ == '__main__':
    single_link = SingleLinkedList()
    single_link.add_head(1)
    single_link.add_head(2)
    single_link.add_head(3)
    # single_link.add_tail(1)
    # single_link.add_tail(2)
    # single_link.add_tail(3)
    single_link.traversal()
    single_link.reverse()
    print(single_link.size())
    print(single_link.length)
