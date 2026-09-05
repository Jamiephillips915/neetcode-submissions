class LinkedList:
    def __init__(self, head):
        self.head = head
        
        
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in hashmap:
                hashmap[key] = LinkedList(head=Node(val=strs[i], next=None))
            else:
                current = hashmap[key].head
                while current.next != None:
                    current = current.next
                current.next = Node(val=strs[i], next=None)
        output = [[] for _ in range(len(hashmap))]
        index = 0
        for i in hashmap.values():
            currentItem = i.head
            while currentItem != None:
                output[index].append(currentItem.val)
                currentItem = currentItem.next
            index += 1
        return output