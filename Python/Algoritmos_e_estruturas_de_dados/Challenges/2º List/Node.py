class Node:
    #Right/leftS means Right/left Son
    def __init__(self,data,left=None,right=None,father=None):
        self._data = data
        self._leftS = None
        self._rightS = None
        self._father = None
        return
    def getData(self):
        return self._data

    def __str__(self):
        return str(self.getData())
    
    def __repr__(self):
        return str('Node('+str(self.getData())+', ' +str(self._leftS) +', ' + str(self._rightS)+', '+str(self._father)+ ')')
        #return 'Node('+ ', '.join([str(self.getData()), str(self._leftS), str(self._rightS), str(self._father)] +')'
