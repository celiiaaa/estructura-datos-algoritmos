"""Phase 2. Class BST2"""
from dlist import DList
from bintree import BinaryNode
from bst import BinarySearchTree
from avl import AVLTree


class BST2(BinarySearchTree):
    """Class BST2."""

    # Ejercicio 1.

    def find_dist_k(self, n: int, k: int) -> list:
        """Encuentra todos los nodos que desde n distan k enlaces"""
        aux = []
        node = self.search(n)
        if self._root is None or node is None:
            return aux
        return self._find_dist_k(node, self._root, k, aux)

    def _find_dist_k(self, node1: BinaryNode, node2: BinaryNode, k: int, lista: list):
        """Funcion recursiva"""
        if node2 is not None:
            lca = self._lca(self._root, node1, node2)
            if (self.depth(node1) - self.depth(lca)) + (self.depth(node2) - self.depth(lca)) == k:
                lista.append(node2.elem)
            self._find_dist_k(node1, node2.left, k, lista)
            self._find_dist_k(node1, node2.right, k, lista)
            return lista

    def _lca(self, node: BinaryNode, node1: BinaryNode, node2: BinaryNode):
        """Funcion recursiva que devuelve el nodo ancestro comun mas bajo"""
        if node is not None:
            if node.elem > node1.elem and node.elem > node2.elem:
                return self._lca(node.left, node1, node2)
            if node.elem < node1.elem and node.elem < node2.elem:
                return self._lca(node.right, node1, node2)
            return node

    # Ejercicio 2.

    def create_tree(self, input_tree1: BinarySearchTree, input_tree2: BinarySearchTree, opc: str):
        """Devuelve un BST dependiendo del opc"""
        aux = AVLTree()
        if input_tree1._root is None and input_tree2._root is None:
            print('Error. Input trees are empty.')
            return aux
        if opc == 'merge':
            # El BST devuelto es el resultante de la union entre ambos arboles.
            return self._merge(input_tree1._root, input_tree2._root, aux)
        if opc == 'intersection':
            # El BST devuelto es el resultante de la interseccion entre ambos arboles.
            return self._intersection(input_tree1, input_tree2._root, aux)
        if opc == 'difference':
            if input_tree2._root is None:
                return input_tree1
            # El BST devuelto es el resultante de la diferencia entre ambos arboles.
            return self._difference(input_tree2, input_tree1._root, aux)
        # El opc no es valido.
        print('Error. The opc value is not valid.')
        return aux

    def _merge(self, node1: BinaryNode, node2: BinaryNode, ftree: AVLTree):
        """Funcion recursiva. Añade en aux todos los nodos que esten en tree1 o en tree2"""
        if node1:
            if not self._is_in(ftree._root, node1):
                ftree.insert(node1.elem)
            self._merge(node1.left, node2, ftree)
            self._merge(node1.right, node2, ftree)
        if node2:
            if not self._is_in(ftree._root, node2):
                ftree.insert(node2.elem)
            self._merge(node1, node2.left, ftree)
            self._merge(node1, node2.right, ftree)
        return ftree

    def _intersection(self, tree: BinarySearchTree, node: BinaryNode, ftree: AVLTree):
        """Funcion recursiva. Añade en aux todos los nodos que esten en tree1 y en tree2"""
        if node is not None:
            if self._is_in(tree._root, node):
                ftree.insert(node.elem)
            self._intersection(tree, node.left, ftree)
            self._intersection(tree, node.right, ftree)
        return ftree

    def _difference(self, tree: BinarySearchTree, node: BinaryNode, ftree: AVLTree):
        """Funcion recursiva. Añade en aux todos los nodos que esten en tree1 pero no en tree2"""
        if tree._root:
            if node is not None:
                if not self._is_in(tree._root, node):
                    ftree.insert(node.elem)
                self._difference(tree, node.left, ftree)
                self._difference(tree, node.right, ftree)
            return ftree

    def _is_in(self, node1: BinaryNode, node2: BinaryNode):
        """Funcion recursiva"""
        if node1 is not None and node2 is not None:
            if node1.elem == node2.elem:
                return True
            elif node1.elem > node2.elem:
                return self._is_in(node1.left, node2)
            else:
                return self._is_in(node1.right, node2)


# Some usage examples
if __name__ == '__main__':
    input_list = [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]
    # input_list_01 = [5, 1, 7, 9, 23]
    # input_list_02 = [1, 9, 11]

    input_list_01 = [5, 12, 2, 1, 3, 9]
    input_list_02 = [9, 3, 21]

    # Build and draw first tree
    tree1 = BinarySearchTree()
    for x in input_list_01:
        tree1.insert(x)
    tree1.draw()

    # Build and draw second tree
    tree2 = BinarySearchTree()
    for x in input_list_02:
        tree2.insert(x)
    tree2.draw()

    function_names = ["merge", "intersection", "difference"]

    for opt in function_names:
        res = BST2()
        res.create_tree(tree1, tree2, opt)
        print(f"-- Result for {opt} method. #{res.size()} nodes")
        res.draw()
