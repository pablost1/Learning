from Node import Node

class Tree:
    def __init__(self, data = None):
        if data:
            self.__root = Node(data)
        else:
            self.__root = data
        self.__depth = 0
        return

    def __str__(self):
        return ' -- '.join(self.inOrder(self.__root))

    def __repr__(self):
        print(n2)
        print(self.__root) 
        print(' -- '.join(self.preOrder(self.__root)))
        return ' -- '.join(self.preOrder(self.__root))

    def __bool__(self):
        return bool(self.__root)

    def inOrder(self, node):
        
        if node:
            fp = []
            lp = []
            if node._leftS:
                fp = self.inOrder(node._leftS)
            aux = [str(node)] ###could be print
            if node._rightS:
                lp = self.inOrder(node._rightS)
            return fp + aux + lp
        else:
            raise ValueError("Tree's Node is not Valid")
       
    def postOrder(self,node):
        if node:
            fp = []
            lp = []
            aux = [str(node)]
            if node._leftS:
                fp = self.postOrder(node._leftS)
            
            if node._rightS:
                lp = self.postOrder(node._rightS)

            aux = [str(node)]
            return  fp + lp + aux
        else:
            raise ValueError("Tree's Node is not Valid")

    def preOrder(self, node):
        if node:
            fp = []
            lp = []
            aux =[str(node)]
            if node._leftS:
               fp =  self.preOrder(node._leftS)
            
            if node._rightS:
               lp = self.preOrder(node._rightS)
            return aux+ fp +lp
        else:
            raise ValueError("Tree's Node is not Valid")

    def getRoot(self):
        return self.__root
    def setRoot(self, node):
        self.__root = node
        return



if __name__ == "__main__":
    tree = Tree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6._leftS = n7
    n6._rightS = n8
    n5._leftS = n6
    n5._rightS = n9
    n3._leftS = n4
    n3._rightS = n5
    n2._leftS = n1
    n2._rightS = n3
    tree.setRoot(n2)
    print(tree.preOrder(n2))
    print(tree.inOrder(n2))
    a = n2
    repr(a)
    
    
