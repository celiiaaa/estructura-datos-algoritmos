"""Unittest phase 2"""
import unittest
from bst import BinarySearchTree
from phase2_skeleton import BST2


def __bst_as_str(bst: BinarySearchTree) -> str:
    top = 10
    lst = bst.inorder_list()
    if len(lst) > top:
        return str(lst[0:top])[0:-1] + ", ..."
    else:
        return str(lst)


class Test(unittest.TestCase):

    def setUp(self):
        self.b1 = BST2()
        data = [14, 11, 18, 10, 13, 16, 19, 5, 12, 15, 17, 30, 4, 6, 29, 31, 2, 8, 24,
                33, 1, 3, 7, 9, 23, 25, 32, 34, 21, 27, 36, 20, 22, 26, 28, 35, 37]
        self.b2 = BST2()
        for e in data:
            self.b2.insert(e)
        data = [20, 15, 5, 18, 24, 22, 25, 30, 33, 80]
        self.b3 = BST2()
        for e in data:
            self.b3.insert(e)

    # Ejercicio 1.

    def test01_find_dist_k(self):
        """Arbol vacio."""
        print("Run test01_find_dist_k.")
        expected = []
        result = self.b1.find_dist_k(1, 1)
        self.assertEqual(expected, result, "Fail test01_find_dist_k.\n")
        print("find_dist_k_test01, OK!!!\n")

    def test02_find_dist_k(self):
        """Lista a retornar vacia."""
        print("Run test02_find_dist_k.")
        expected = []
        result = self.b2.find_dist_k(18, 8)
        self.assertEqual(expected, result, "Fail test02_find_dist_k.\n")
        print("test02_find_dist_k, OK!!!\n")

    def test03_find_dist_k(self):
        """n = 30, k = 0."""
        print("Run test03_find_dist_k.")
        expected = [30]
        result = self.b2.find_dist_k(30, 0)
        self.assertEqual(expected, result, "Fail test03_find_dist_k.\n")
        print("test03_find_dist_k, OK!!!\n")

    def test04_find_dist_k(self):
        """n = 30, k = 2."""
        print("Run test04_find_dist_k.")
        expected = [18, 24, 33]
        result = self.b2.find_dist_k(30, 2)
        self.assertEqual(expected, result, "Fail test04_find_dist_k.\n")
        print("test04_find_dist_k, OK!!!\n")

    def test05_find_dist_k(self):
        """n = 12, k = 6. Lista larga a retornar."""
        print("Run test05_find_dist_k.")
        expected = [4, 6, 23, 25, 32, 34]
        result = self.b2.find_dist_k(17, 7)
        self.assertEqual(expected, result, "Fail test05_find_dist_k.\n")
        print("test05_find_dist_k, OK!!!\n")

    def test06_find_dist_k(self):
        """n = 36, k = 13. Distancia k larga."""
        print("Run test06_find_dist_k.")
        expected = [1, 3, 7, 9]
        result = self.b2.find_dist_k(36, 13)
        self.assertEqual(expected, result, "Fail test06_find_dist_k.\n")
        print("test06_find_dist_k, OK!!!\n")

    def test07_find_dist_k(self):
        """n = 100, k = 2. Nodo no encontrado en el arbol."""
        print("Run test07_find_dist_k.")
        expected = []
        result = self.b2.find_dist_k(100, 2)
        self.assertEqual(expected, result, "Fail test07_find_dist_k.\n")
        print("test07_find_dist_k, OK!!!\n")

    def test08_find_dist_k(self):
        """n = 14, k = 6. Desde el nodo raiz."""
        print("Run test08_find_dist_k.")
        expected = [1, 3, 7, 9, 23, 25, 32, 34]
        result = self.b2.find_dist_k(14, 6)
        self.assertEqual(expected, result, "Fail test08_find_dist_k.\n")
        print("test08_find_dist_k, OK!!!\n")

    def test09_find_dist_k(self):
        """n = 4, k = 4. Siendo el nodo raiz uno de los que retornar."""
        print("Run test09_find_dist_k.")
        expected = [14, 7, 9, 13]
        result = self.b2.find_dist_k(4, 4)
        self.assertEqual(expected, result, "Fail test09_find_dist_k.\n")
        print("test09_find_dist_k, OK!!!\n")

    # Ejercicio 2.

    def test10_create_tree(self):
        """input_trees estan vacios."""
        print("Run test10_create_tree.")
        expected = []
        result = BST2()
        result = result.create_tree(self.b1, self.b1, "merge")
        result = result.inorder_list()
        self.assertEqual(expected, result, "Fail test10_create_tree.\n")
        print("test10_create_tree, OK!!!\n")

    def test11_create_tree(self):
        """opc = merge."""
        print("Run test11_create_tree.")
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 80]
        result = BST2()
        result = result.create_tree(self.b2, self.b3, "merge")
        # result.draw()
        result = result.inorder_list()
        self.assertEqual(expected, result, "Fail test11_create_tree.\n")
        print("test11_create_tree, OK!!!\n")

    def test12_create_tree(self):
        """opc = intersection."""
        print("Run test12_create_tree.")
        expected = [5, 15, 18, 20, 22, 24, 25, 30, 33]
        result = BST2()
        result = result.create_tree(self.b2, self.b3, "intersection")
        # result.draw()
        result = result.inorder_list()
        self.assertEqual(expected, result, "Fail test12_create_tree.\n")
        print("test12_create_tree, OK!!!\n")

    def test13_create_tree(self):
        """opc = difference."""
        print("Run test13_create_tree.")
        expected = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17,
                    19, 21, 23, 26, 27, 28, 29, 31, 32, 34, 35, 36, 37]
        result = BST2()
        result = result.create_tree(self.b2, self.b3, "difference")
        # result.draw()
        result = result.inorder_list()
        self.assertEqual(expected, result, "Fail test13_create_tree.\n")
        print("test13_create_tree, OK!!!\n")

    def test14_create_tree(self):
        """opc = abc. El opc no es valido."""
        print("Run test14_create_tree.")
        expected = []
        result = BST2()
        result = result.create_tree(self.b2, self.b3, "abc")
        result = result.inorder_list()
        self.assertEqual(expected, result, "Fail test14_create_tree.\n")
        print("test14_create_tree, OK!!!\n")

    def test15_create_tree(self):
        """opc = merge. Teniendo el input_tree1 vacio."""
        print("Run test15_create_tree.")
        expected = [5, 15, 18, 20, 22, 24, 25, 30, 33, 80]
        result = BST2()
        result = result.create_tree(self.b1, self.b3, "merge")
        # result.draw()
        result = result.inorder_list()
        self.assertEqual(expected, result, "Fail test15_create_tree.\n")
        print("test15_create_tree, OK!!!\n")

    def test16_create_tree(self):
        """opc = intersection. Teniendo el input_tree1 vacio."""
        print("Run test16_create_tree.")
        expected = []
        result = BST2()
        result = result.create_tree(self.b1, self.b3, "intersection")
        result = result.inorder_list()
        self.assertEqual(expected, result, "Fail test16_create_tree.\n")
        print("test16_create_tree, OK!!!\n")

    def test17_create_tree(self):
        """opc = difference. Teniendo el input_tree1 vacio."""
        print("Run test17_create_tree.")
        expected = []
        result = BST2()
        result = result.create_tree(self.b1, self.b3, "difference")
        result = result.inorder_list()
        self.assertEqual(expected, result, "Fail test17_create_tree.\n")
        print("test17_create_tree, OK!!!\n")

    def test18_create_tree(self):
        """opc = merge. Teniendo el input_tree2 vacio."""
        print("Run test18_create_tree.")
        expected = [5, 15, 18, 20, 22, 24, 25, 30, 33, 80]
        result = BST2()
        result = result.create_tree(self.b3, self.b1, "merge")
        result = result.inorder_list()
        self.assertEqual(expected, result, "Fail test18_create_tree.\n")
        print("test18_create_tree, OK!!!\n")

    def test19_create_tree(self):
        """opc = intersection. Teniendo el input_tree2 vacio."""
        print("Run test19_create_tree.")
        expected = []
        result = BST2()
        result = result.create_tree(self.b3, self.b1, "intersection")
        result = result.inorder_list()
        self.assertEqual(expected, result, "Fail test19_create_tree.\n")
        print("test19_create_tree, OK!!!\n")

    def test20_create_tree(self):
        """opc = difference. Teniendo el input_tree2 vacio."""
        print("Run test20_create_tree.")
        expected = [5, 15, 18, 20, 22, 24, 25, 30, 33, 80]
        result = BST2()
        result = result.create_tree(self.b3, self.b1, "difference")
        # result.draw()
        result = result.inorder_list()
        self.assertEqual(expected, result, "Fail test20_create_tree.\n")
        print("test20_create_tree, OK!!!\n")


if __name__ == '__main__':
    unittest.main()
