"""Is the tree at this node balanced?

To make this a bit more readable, let's alias our class name:

    >>> N = BinaryNode

For a tree of 1 item:

    >>> tree1 = N(1)
    >>> tree1.is_balanced()
    True

For a tree of 2 items:

  1
 /
2

    >>> tree2 = N(1,
    ...           N(2))
    >>> tree2.is_balanced()
    True

Three:

  1
 / \
2   3

    >>> tree3 = N(1,
    ...           N(2), N(3))
    >>> tree3.is_balanced()
    True

Four:

     1
    / \
   2   4
  /
 3

    >>> tree4 = N(1,
    ...           N(2,
    ...             N(3)),
    ...           N(4))
    >>> tree4.is_balanced()
    True

Five:

     1
   /---\
  2     5
 / \
3   4

    >>> tree5 = N(1,
    ...           N(2,
    ...             N(3), N(4)),
    ...           N(5))
    >>> tree5.is_balanced()
    True

Imbalanced Four:

    1
   /
  2
 / \
3   4

    >>> tree4i = N(1,
    ...            N(2,
    ...              N(3), N(4)))
    >>> tree4i.is_balanced()
    False
"""


class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_balanced(self):
        """Is the tree at this node balanced?"""
        nodes_to_look_at = [self]
            
        while nodes_to_look_at:
            for node in nodes_to_look_at:
                if node.left and node.right:
                    nodes_to_look_at.extend([node.left,node.right])
                    nodes_to_look_at.remove(node)
                elif node.left:
                    if node.left.left and node.left.right:
                        return False
                    elif node.left.left:
                        if node.left.left.right or node.left.left.left:
                            return False
                        else:
                            return True
                    elif node.left.right:
                        if node.left.right.right or node.left.right.left:
                            return False
                        else:
                            return True
                    else:
                        return True
                elif node.right:
                    if node.right.left and node.right.right:
                        return False
                    elif node.right.left:
                        if node.right.left.right or node.right.left.left:
                            return False
                        else:
                            return True
                    elif node.right.right:
                        if node.right.right.left or node.right.right.right:
                            return False
                        else:
                            return True
                else:
                    return True





if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED! GO GO GO!\n"
