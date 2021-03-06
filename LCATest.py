import unittest
import LCA


class TestLCA(unittest.TestCase):

    def test_LCA(self):
        root = LCA.Node(20) 
        root.left = LCA.Node(8) 
        root.right = LCA.Node(22) 
        root.left.left = LCA.Node(4) 
        root.left.right = LCA.Node(12) 
        root.left.right.left = LCA.Node(10) 
        root.left.right.right = LCA.Node(14)
        self.assertEqual(LCA.lca(root, 10,14).data,12) 
        self.assertEqual(LCA.lca(root, 14,8).data,8) 
        self.assertEqual(LCA.lca(root, 10,22).data, 20)  
              

if __name__ == "main":
    unittest.main()
