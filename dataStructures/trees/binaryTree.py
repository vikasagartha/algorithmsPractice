'''
Create a bTree:
    T = bTree(myParent, myValue, myLeftChild, myRightChild)
    All parameters are optional, but value is important
'''
class bTree:
    def __init__(self, parent=None, value=None, left=None, right=None):
        self.parent=parent
        self.value=value
        self.left=left
        self.right=right
        self.right=right

    def calculateHeight(self):
        if not self.value:
            return 0
        elif self.left and self.right:
            return 1 + max(self.left.calculateHeight(), self.right.calculateHeight())
        elif self.left and not self.right:
            return 1 + self.left.calculateHeight()
        elif not self.left and self.right:
            return 1 + self.right.calculateHeight()
        else:
            return 1

    def insertLeaf(self, value):
        if not self.value:
            self.value=value
        elif value<self.value:
            if not self.left:
                self.left = bTree(self)
            self.left.insertLeaf(value)
        elif value>self.value:
            if not self.right:
                self.right= bTree(self)
            self.right.insertLeaf(value)
        else:
            return

    def inOrderTraverse(self):
        if self.left:
            self.left.inOrderTraverse()
        print self.value, " ",
        if self.right:
            self.right.inOrderTraverse()

    def searchBST(self, searchVal):
        if not self.value:
            return None
        elif self.value==searchVal:
            return self
        elif searchVal<self.value and self.left:
            return self.left.searchBST(searchVal)
        elif searchVal>self.value and self.right:
            return self.right.searchBST(searchVal)
        else:
            return None

    def maxNode(self): 
        if not self.value:
            return None
        elif self.right:
            return self.right.maxNode()
        else: 
            return self

    def minNode(self): 
        if not self.value:
            return None
        elif self.left:
            return self.left.minNode()
        else: 
            return self
    '''
    Returns the value that is
        1. < searchVal
        2. Closest to searchVal
    '''
    def predecessor(self, searchVal):
        node = self.searchBST(searchVal) 
        if not node:
            print "No such node"
        if self.left:
            return self.left.maxNode()
        else:
            return None

    def hasNoChildren(self):
        return not (self.left or self.right)

    def deleteChild(self, childValue):
        if self.left and self.left.value == childValue:
            self.left = None
        else:
            self.right = None

    def deleteNode(self, searchVal):
        node = self.searchBST(searchVal) 
        if not node:
            print "No such node"
        elif node.hasNoChildren():
            node.parent.deleteChild(self.value)
        else:
            return

    def printNodeInfo(self):
        print "Key " + str(self.value)
        if self.parent:
            print "Parent key = " + str(self.parent.value)
        if self.left:
            print "Left Child key = " + str(self.left.value)
        else:
            print "No left child"
        if self.right:
            print "Right Child key = " + str(self.right.value)
        else:
            print "No right child"

    '''
    A neat method for printing trees
    Source: http://stevekrenzel.com/articles/printing-trees
    '''
    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(self.value)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret
