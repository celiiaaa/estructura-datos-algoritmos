import unittest
from phase1 import SList2


class Test(unittest.TestCase):
    def setUp(self):
        listas = {
            "lista1": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "lista2": [1, 2, 3, 4, 5, 1, 2, 6, 7],
            "lista3": [3, 3, 3, 4, 5, 6, 6, 6, 7, 7, 7, 7, 2, 8, 8],
            "lista4": [8, 8, 8, 8, 4, 5, 6, 6, 6, 7, 7, 7, 7],
            "lista5": [6, 6, 12, 12, 4, 4, 12, 12],
            "lista6": [5],
            "lista7": [1, 2, 3, 1, 2, 3],
            "lista8": [3, 9]
        }
        slists = []
        for lista in listas.values():
            slist = SList2()
            for e in lista:
                slist.addLast(e)
            slists.append(slist)
        self.sl1 = SList2()
        self.sl2, self.sl3, self.sl4, self.sl5, self.sl6, self.sl7, self.sl8, self.sl9 = slists

    # Tests del primer metodo.
    def test01_delLargestSeq(self):
        # Lista vacía.
        print('Run test1_delLargestSeq. Emtpy list.')
        expected = ''
        result = self.sl1
        result.delLargestSeq()
        self.assertEqual(expected, str(result), 'Fail. Empty list.')
        self.assertEqual(result._size, 0, 'Fail. Size of the empty list.')
        print("test1_delLargestSeq, OK!!!\n")

    def test02_delLargestSeq(self):
        # Secuencia a eliminar en el medio de la slist.
        print('Run test2_delLargestSeq. Middle sequence.')
        expected = '3,3,3,4,5,6,6,6,2,8,8'
        result = self.sl4
        result.delLargestSeq()
        self.assertEqual(expected, str(result), 'Fail. Middle sequence list.')
        self.assertEqual(result._size, 11, 'Fail. Size of the middle sequence list.')
        print("test2_delLargestSeq, OK!!!\n")

    def test03_delLargestSeq(self):
        # Secuencia a eliminar al final (cola) de la slist.
        print('Run test3_delLargestSeq. Tail sequence.')
        expected = '8,8,8,8,4,5,6,6,6'
        result = self.sl5
        result.delLargestSeq()
        self.assertEqual(expected, str(result), 'Fail. Tail sequence list.')
        self.assertEqual(result._size, 9, 'Fail. Size of the tail sequence list.')
        print("test3_delLargestSeq, OK!!!\n")

    def test04_delLargestSeq(self):
        # Secuencia a eliminar al final (cola) de la slist y formada por secuencias de la misma longitud.
        print('Run test4_delLargestSeq. Equal length sequence.')
        expected = '6,6,12,12,4,4'
        result = self.sl6
        result.delLargestSeq()
        self.assertEqual(expected, str(result), 'Fail. Equal length sequence list.')
        self.assertEqual(result._size, 6, 'Fail. Size of the equal length sequence list.')
        print("test4_delLargestSeq, OK!!!\n")

    def test05_delLargestSeq(self):
        # len=1. Formada por un elemento a eliminar.
        print('Run test5_delLargestSeq. One length list.')
        expected = ''
        result = self.sl7
        result.delLargestSeq()
        self.assertEqual(expected, str(result), 'Fail. One length list.')
        self.assertEqual(result._size, 0, 'Fail. Size of the one length list.')
        print("test5_delLargestSeq, OK!!!\n")

    def test06_delLargestSeq(self):
        # len=2. Formada por un elemento a eliminar.
        print('Run test6_delLargestSeq. Emtpy list.')
        expected = '3'
        result = self.sl9
        result.delLargestSeq()
        self.assertEqual(expected, str(result), 'Fail. Empty list.')
        self.assertEqual(result._size, 1, 'Fail. Size of the empty list.')
        print("test6_delLargestSeq, OK!!!\n")

    def test07_delLargestSeq(self):
        # Secuencia a eliminar al final (cola) de la slist y formada por secuencias del mismo tamaño.
        print('Run test7_delLargestSeq. Equal and repeated sequence.')
        expected = '1,2,3,1,2'
        result = self.sl8
        result.delLargestSeq()
        self.assertEqual(expected, str(result), 'Fail. Equal and repeated sequence list.')
        self.assertEqual(result._size, 5, 'Fail. Size of the equal and repeated sequence list.')
        print("test7_delLargestSeq, OK!!!\n")

    # Tests segundo metodo.
    def test08_fix_loop(self):
        # Lista vacia. return=False
        print('Run test8_fix_loop. Empty list')
        expected = ''
        result = self.sl1
        found = result.fix_loop()
        self.assertFalse(found, 'Fail. Return not correct.')
        self.assertEqual(expected, str(result), 'Fail. Equal and repeated sequence list.')
        self.assertEqual(result._size, 0, 'Fail. Size of the equal and repeated sequence list.')
        print("test8_fix_loop, OK!!!\n")

    def test09_fix_loop(self):
        # position=2, return=True.
        print('Run test9_fix_loop. position=2')
        expected = '1,2,3,4,5,6,7,8,9'
        result = self.sl2
        result.create_loop(2)
        # Para verificar que el loop se ha creado.
        """n = result._head
        for i in range(result._size+10):
            print(n.elem)
            n = n.next"""
        found = result.fix_loop()
        # Para buscar el ultimo nodo de la lista (tail) y comprobar que su next sea None.
        n = result._head
        for i in range(result._size - 1):  # while n.next: – Tambien podria ser así pero asi nos evitamos que si no funciona fix_loop, entremos en un bucle infinito.
            n = n.next
        self.assertIsNone(n.next, 'Fail. The next of the last node is not None.')
        self.assertTrue(found, 'Fail. Return not correct.')
        self.assertEqual(expected, str(result), 'Fail. Loop list position=2.')
        self.assertEqual(result._size, 9, 'Fail. Size not correct.')
        print("test9_fix_loop, OK!!!\n")

    def test10_fix_loop(self):
        # position=0, return=True.
        print('Run test10_fix_loop. position=0')
        expected = '1,2,3,4,5,6,7,8,9'
        result = self.sl2
        result.create_loop(0)
        # Para verificar que el loop se ha creado.
        """n = result._head
        for i in range(result._size+10):
            print(n.elem)
            n = n.next"""
        found = result.fix_loop()
        # Para buscar el ultimo nodo de la lista (tail) y comprobar que su next sea None.
        n = result._head
        for i in range(result._size - 1):  # while n.next: – Tambien podria ser así pero asi nos evitamos que si no funciona fix_loop, entremos en un bucle infinito.
            n = n.next
        self.assertIsNone(n.next, 'Fail. The next of the last node is not None.')
        self.assertTrue(found, 'Fail. Return not correct.')
        self.assertEqual(expected, str(result), 'Fail. Loop list position=0.')
        self.assertEqual(result._size, 9, 'Fail. Size not correct.')
        print("test10_fix_loop, OK!!!\n")

    def test11_fix_loop(self):
        # position=5, return=True.
        print('Run test11_fix_loop. position=0')
        expected = '1,2,3,4,5,1,2,6,7'
        result = self.sl3
        result.create_loop(5)
        # Para verificar que el loop se ha creado.
        """n = result._head
        for i in range(result._size+10):
            print(n.elem)
            n = n.next"""
        found = result.fix_loop()
        # Para buscar el ultimo nodo de la lista (tail) y comprobar que su next sea None.
        n = result._head
        for i in range(result._size-1): # while n.next: – Tambien podria ser así pero asi nos evitamos que si no funciona fix_loop, entremos en un bucle infinito.
            n = n.next
        self.assertIsNone(n.next, 'Fail. The next of the last node is not None.')
        self.assertTrue(found, 'Fail. Return not correct.')
        self.assertEqual(expected, str(result), 'Fail. Loop list position=5.')
        self.assertEqual(result._size, 9, 'Fail. Size not correct.')
        print("test11_fix_loop, OK!!!\n")

    def test12_fix_loop(self):
        # return=False. No creamos ningun loop.
        print('Run test12_fix_loop.')
        expected = '1,2,3,4,5,1,2,6,7'
        result = self.sl3
        # Para verificar que el loop no se ha creado.
        """n = result._head
        for i in range(result._size-1):
            print(n.elem)
            n = n.next"""
        found = result.fix_loop()
        self.assertFalse(found, 'Fail. Return not correct.')
        self.assertEqual(expected, str(result), 'Fail. Not loop list.')
        self.assertEqual(result._size, 9, 'Fail. Size not correct.')
        print("test12_fix_loop, OK!!!\n")

    def test13_fix_loop(self):
        # position=0, return=True. Lista de longitud uno.
        print('Run test13_fix_loop.')
        expected = '5'
        result = self.sl7
        result.create_loop(0)
        # Para verificar que el loop no se ha creado.
        n = result._head
        for i in range(result._size+3):
            # print(n.elem)
            n = n.next
        found = result.fix_loop()
        # Para buscar el ultimo nodo de la lista (tail) y comprobar que su next sea None.
        n = result._head
        for i in range(result._size - 1):  # while n.next: – Tambien podria ser así pero asi nos evitamos que si no funciona fix_loop, entremos en un bucle infinito.
            n = n.next
        self.assertIsNone(n.next, 'Fail. The next of the last node is not None.')
        self.assertTrue(found, 'Fail. Return not correct.')
        self.assertEqual(expected, str(result), 'Fail. Loop list len=1.')
        self.assertEqual(result._size, 1, 'Fail. Size not correct.')
        print("test13_fix_loop, OK!!!\n")

    def test14_fix_loop(self):
        # position=3, return=True. Lista de secuencia repetida.
        print('Run test14_fix_loop.')
        expected = '1,2,3,1,2,3'
        result = self.sl8
        result.create_loop(3)
        # Para verificar que el loop no se ha creado.
        n = result._head
        for i in range(result._size+4):
            # print(n.elem)
            n = n.next
        found = result.fix_loop()
        # Para buscar el ultimo nodo de la lista (tail) y comprobar que su next sea None.
        n = result._head
        for i in range(result._size - 1):  # while n.next: – Tambien podria ser así pero asi nos evitamos que si no funciona fix_loop, entremos en un bucle infinito.
            n = n.next
        self.assertIsNone(n.next, 'Fail. The next of the last node is not None.')
        self.assertTrue(found, 'Fail. Return not correct.')
        self.assertEqual(expected, str(result), 'Fail. Loop list position=3.')
        self.assertEqual(result._size, 6, 'Fail. Size not correct.')
        print("test14_fix_loop, OK!!!\n")

    # Tests tercer metodo.
    def test15_leftrightShift(self):
        # Lista vacia. left=True n=0
        print('Run test15_leftrightShift.')
        expected = ''
        result = self.sl1
        result.leftrightShift(True, 0)
        self.assertEqual(expected, str(result), 'Fail. Empty list.')
        # self.assertEqual(result._size, 0, 'Fail. Size of the empty list.')
        print("test15_leftrightShift, OK!!!\n")

    def test16_leftrightShift(self):
        # left=True n=4.
        print('Run test16_leftrightShift.')
        expected = '5,6,7,8,9,1,2,3,4'
        result = self.sl2
        result.leftrightShift(True, 4)
        self.assertEqual(expected, str(result), 'Fail. Empty list.')
        # self.assertEqual(result.__size, 9, 'Fail. Size of the empty list.')
        print("test16_leftrightShift, OK!!!\n")

    def test17_leftrightShift(self):
        # left=False n=3.
        print('Run test17_leftrightShift.')
        expected = '7,8,9,1,2,3,4,5,6'
        result = self.sl2
        result.leftrightShift(False, 3)
        self.assertEqual(expected, str(result), 'Fail. leftright left=False n=3.')
        # self.assertEqual(result.__size, 9, 'Fail. Size of the leftright list.')
        print("test17_leftrightShift, OK!!!\n")

    def test18_leftrightShift(self):
        # left=False n=10.
        print('Run test18_leftrightShift.')
        expected = '1,2,3,4,5,6,7,8,9'
        result = self.sl2
        result.leftrightShift(False, 10)
        self.assertEqual(expected, str(result), 'Fail. leftright left=False n=10.')
        # self.assertEqual(result.__size, 9, 'Fail. Size of the leftright list.')
        print("test18_leftrightShift, OK!!!\n")

    def test19_leftrightShift(self):
        # left=True n=4.
        print('Run test19_leftrightShift.')
        expected = '2,3,1,2,3,1'
        result = self.sl8
        result.leftrightShift(True, 4)
        self.assertEqual(expected, str(result), 'Fail. leftright left=False n=10.')
        # self.assertEqual(result.__size, 6, 'Fail. Size of the leftright list.')
        print("test19_leftrightShift, OK!!!\n")

    def test20_leftrightShift(self):
        # left=True n=0.
        print('Run test20_leftrightShift.')
        expected = '1,2,3,4,5,6,7,8,9'
        result = self.sl2
        result.leftrightShift(True, 0)
        self.assertEqual(expected, str(result), 'Fail. leftright left=True n=0.')
        # self.assertEqual(result.__size, 9, 'Fail. Size of the leftright list.')
        print("test20_leftrightShift, OK!!!\n")

    def test21_leftrightShift(self):
        # len=1. left=False n=1.
        print('Run test21_leftrightShift.')
        expected = '5'
        result = self.sl7
        result.leftrightShift(False, 1)
        self.assertEqual(expected, str(result), 'Fail. leftright left=False n=1.')
        # self.assertEqual(result.__size, 1, 'Fail. Size of the leftright list.')
        print("test21_leftrightShift, OK!!!\n")

    def test22_leftrightShift(self):
        # len=1. left=True n=1. len=1
        print('Run test22_leftrightShift.')
        expected = '5'
        result = self.sl7
        result.leftrightShift(True, 1)
        self.assertEqual(expected, str(result), 'Fail. leftright left=True n=1.')
        # self.assertEqual(result.__size, 1, 'Fail. Size of the leftright list.')
        print("test22_leftrightShift, OK!!!\n")

    def test23_leftrightShift(self):
        # len=2. left=False n=1.
        print('Run test23_leftrightShift.')
        expected = '9,3'
        result = self.sl9
        result.leftrightShift(False, 1)
        self.assertEqual(expected, str(result), 'Fail. leftright left=False n=1.')
        # self.assertEqual(result.__size, 2, 'Fail. Size of the leftright list.')
        print("test23_leftrightShift, OK!!!\n")


    def test_print_slists(self):
        # Imprime todas las listas utilizadas en este unittest.
        print(str(self.sl1))    # Empty
        print(str(self.sl2))    # 1,2,3,4,5,6,7,8,9
        print(str(self.sl3))    # 1,2,3,4,5,1,2,6,7
        print(str(self.sl4))    # 3,3,3,4,5,6,6,6,7,7,7,7,2,8,8
        print(str(self.sl5))    # 8,8,8,8,4,5,6,6,6,7,7,7,7
        print(str(self.sl6))    # 6,6,12,12,4,4,12,12
        print(str(self.sl7))    # 5
        print(str(self.sl8))    # 1,2,3,1,2,3
        print(str(self.sl9))    # 3,9


if __name__ == "__main__":
    unittest.main()