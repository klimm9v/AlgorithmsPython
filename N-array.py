from typing import List, Optional

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def pre_order(node):
            if node:
                result.append(node.val)
                for child in node.children:
                    pre_order(child)
        pre_order(root)
        return result