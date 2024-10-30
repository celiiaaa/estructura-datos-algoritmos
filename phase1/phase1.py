from slist import SList
from slist import SNode
import sys

class SList2(SList):

    def delLargestSeq(self):
        """Metodo que elimina la secuencia de numeros iguales y consecutivos mas larga."""
        if self.isEmpty():                          # En el caso de estar vacia.
            print('Empty List')                         # se imprime que la lista esta vacia.
            return None
        if self._size == 1:                         # En el caso de que la lista sea de un elemento.
            self.removeFirst()                          # se elimina el unico elemento que hay en la lista.
            return None
        # Se inicializa las variables que vamos a utilizar.
        nodeIt = self._head                         # variable con la que nos desplazaremos en la slist para buscar la secuencia mas larga.
        count = 1                                   # contador de longitud de la secuencia.
        max_count = 0                               # contador que guarda la longitud de la secuencia mas larga.
        sec_ini = None                              # variable que guarda el nodo inicial de la secuencia actual (en la que estamos en cada momento).
        sec_end = None                              # variable que guarda el nodo final de la secuencia actual (en la que estamos en cada momento).
        node_ini = None                             # variable que guarda el nodo inicio de la secuencia de mayor longitud.
        node_end = None                             # variable que guarda el nodo fin de la secuencia de mayor longitud.
        while nodeIt:                               # Se ejecuta mientras exista nodeIt:
            if nodeIt.next and nodeIt.elem == nodeIt.next.elem: # la secuencia continua.
                count += 1                          # Se incrementa el count por haber una aparicion mas de elementos iguales y consecutivos.
                if count > max_count:               # Se actualiza max_count con el valor mas grande hasta ahora.
                    max_count = count
            else:                               # En caso contrario, el elemento de nodeIt es distinto al del nodeIt.next,
                sec_end = nodeIt.next               # se declara que nodeIt.next es el fin de la secuencia actual.
                if count >= max_count:              # Si count es mayor o igual a max_count, es decir, si la secuencia actual es mas larga o igual que la secuencia mas larga que habia hasta el momento,
                    node_ini = sec_ini                  # actualizamos y guardamos el inicio y el fin de la secuencia (siendo esta la nueva secuencia mas larga hasta el momento).
                    node_end = nodeIt.next
                    max_count = count                   # actualizamos max_count con el nuevo valor.
                if nodeIt.next == None:         # Si hemos llegado al final de la slist
                    if node_ini == None:            # Y node_ini (nodo inicial de la secuencia de mayor longitud) es None, no existe,
                        self._head = node_end           # se asigna como cabeza de slist a node_end.
                    elif node_end == None:          # Y node_end (nodo final de la secuancia de mayor longitud) es None, no existe,
                        node_ini.next = None            # se le asigna el valor None al siguiente de node_ini, se hace que sea la cola de la slist.
                    else:                           # Y hay node_ini y node_end, es decir, la secuencia se encuentra en medio de la slist.
                        node_ini.next = node_end        # se enlaza node_ini y node_end, eliminando la secuencia de mayor longitud.
                    self._size -= max_count         # Se actualiza el tamaño de la slist, restando max_count.
                sec_ini = nodeIt                # Se actualiza sec_ini cada vez que se empieza una nueva secuencia, es decir, la siguiente.
                count = 1                       # Se resetea el contador count a 1.
            nodeIt = nodeIt.next            # Se pasa al siguiente nodo.
        return None

    def fix_loop(self):
        """Metodo que devuelve un True o un False si encuentra o no un loop y lo arregla eliminandolo."""
        if self.isEmpty():                          # Si la lista se encuentra vacía,
            return False                                # la funcion retorna un false que indica que no se ha encontrado con un loop.
        current = self._head                        # variable con la que nos desplazaremos en la slist buscando si hay un loop.
        found = False                               # variable que guarda si se ha encontrado o no un loop, se inicializa con un False al no haber encontrado un loop.
        while current and not found:                # Se ejecuta mientras que el nodo actual no sea None y mientras que no se haya encontrado un bucle:
            nodeIt = self._head                         # variable con la que nos desplazaremos en la slist para comparar con el nodo current.
            end = False                                 # variable para identificar que nodeIt sea current, es decir, hemos terminado de comparar con ese nodo current.
            while nodeIt and not end:                   # Se ejecuta mientras que exista nodeIt y no sea end:
                if nodeIt == current:                       # Si nodeIt es current,
                    end = True                                  # se termina con ese nodo current, pasando al siguiente nodo.
                if nodeIt == current.next:                  # Si nodeIt es current.next,
                    current.next = None                         # el siguiente de current se asigna el valor de None, arreglando asi el loop.
                    found = True                                # se actualiza el valor de found para indicar que hemos encontrado un bucle y ya ha sido arreglado.
                nodeIt = nodeIt.next                        # Se pasa al siguiente nodeIt.
            current = current.next                      # Se pasa al siguiente current.
        return found                                # Se devuelve si se ha encontrado o no un loop en la SList.

    def create_loop(self, position):
        # this method is used to force a loop in a singly linked list
        if position < 0 or position > len(self) - 1:
            raise ValueError(f"Position out of range [{0} - {len(self) - 1}]")
        current = self._head
        i = 0
        # We reach position to save the reference
        while current and i < position:
            current = current.next
            i += 1
        # We reach to tail node and set the loop
        start_node = current
        print(f"Creating a loop starting from {start_node.elem}")
        while current.next:
            current = current.next
        current.next = start_node

    def leftrightShift(self, left: bool, n: int):
        """Metodo que coge los n primero o ultimos al final o al principio de la SList, depende de left."""
        if self._size>1 and 0<n<=self._size:        # Si la longitud de la lista es mayor que 1 y la n es [1,len(SList)],
            nodeIt = self._head                         # variable con la que nos desplazaremos por la slist.
            aux = SList()                               # slist auxiliar en la que añadiremos los elementos que se van a mover.
            if left == True:                            # Si left es True,
                r = n                                       # los nodos que se van a añadir en la slist auxiliar son los n primeros.
            else:                                       # En caso contrario, si left es False,
                r = self._size - n                          # los nodos que se van a añadir en la slist auxiliar son los n ultimos.
            for i in range(r):                          # Se ejecuta r veces:
                aux.addLast(nodeIt.elem)                    # se añade los r nodos en la lista auxiliar.
                prev = nodeIt  # newTail                    # guardamos el prev (el nodo anterior al actual).
                nodeIt = nodeIt.next                        # pasamos al siguiente nodo.
            tail = self._head                           # variable para guardar la nueva cola de la slist.
            for i in range(self._size - 1):             # Se ejecuta len(slist)-1:
                tail = tail.next                            # pasamos al siguiente nodo, buscando la nueva cola.
            self._head = nodeIt                         # Asignamos que la nueva cabeza de la slist sea el nodo actual.
            tail.next = aux._head                       # Enlazamos la slist auxiliar, utilizando el nodo tail.
            if left is True:                            # Si left es True,
                prev.next = None                            # se declara que prev (el nodo previo al nodo actual) sea None, es decir, que sea la cola de la slist.
        return None







if __name__=='__main__':

    l=SList2()
    print("list:",str(l))
    print("len:",len(l))

    for i in range(7):
        l.addLast(i+1)

    print(l)
    print()

    l=SList2()
    print("list:",str(l))
    print("len:",len(l))

    for i in range(7):
        l.addLast(i+1)

    print(l)
    print()

    # No loop yet, no changes applied
    l.fix_loop()
    print("No loop yet, no changes applied")
    print(l)
    print()

    # We force a loop
    l.create_loop(position=6)
    l.fix_loop()
    print("Loop fixed, changes applied")
    print(l)
    print()
    print()

    
    l = SList2()
    for i in [1,2,3,4,5]:        
        l.addLast(i)
    print(l.delLargestSeq())


    l=SList2()
    for i in range(7):
         l.addLast(i+1)

    print(l)
    l.leftrightShift(False, 2)
    print(l)
    
    