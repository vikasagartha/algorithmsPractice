import unittest
from binaryTree import *

class binaryTreeTestCase(unittest.TestCase): 

    def test_calculateHeight(self):
        #empty Tree
        T = bTree()   
        self.assertEqual(T.calculateHeight(), 0)

        #single Node
        T = bTree(None, 3)   
        self.assertEqual(T.calculateHeight(), 1)

        T.insertLeaf(1)
        T.insertLeaf(2)
        T.insertLeaf(5)
        T.insertLeaf(4)
        self.assertEqual(T.calculateHeight(), 3)

if __name__ == '__main__':
    unittest.main()
