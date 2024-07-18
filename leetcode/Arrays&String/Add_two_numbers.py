# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = self.to_list()
        list2 = self.to_list()
        print(list1, list2)

    def to_list(self, head: ListNode):
        my_list = list()
        curr  = head

        while curr:
            my_list.append(curr.val)
            curr = curr.next
        return my_list




ln1, ln2, ln3 = ListNode(2), ListNode("salam"), ListNode(78)

# print(ln1.val, ln1.next.val)