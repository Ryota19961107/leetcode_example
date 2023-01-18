from typing import Optional

import collections

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return root
        
        rootBNode = TreeNode(root.val)
        queue = collections.deque([(rootBNode, root)])
        
        while queue:
            prevBNode = None
            headBNode = None
            parent, curr = queue.popleft()
            for child in curr.children:
                newBNode = TreeNode(child.val)
                if prevBNode:
                    prevBNode.right = newBNode
                else:
                    headBNode = newBNode
                prevBNode = newBNode
                queue.append((newBNode, child))
            parent.left = headBNode
        
        return rootBNode
                    
        
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return data
        
        rootNode = Node(data.val, [])
        quene = collections.deque([(rootNode, data)])
        
        while quene:
            parent, curr = quene.popleft()
            firstChild = curr.left
            sibling = firstChild
            while sibling:
                newNode = Node(sibling.val, [])
                parent.children.append(newNode)
                quene.append((newNode, sibling))
                sibling = sibling.right
        return rootNode
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))