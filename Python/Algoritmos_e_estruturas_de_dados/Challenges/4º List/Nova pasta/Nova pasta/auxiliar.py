class Aux:
    def __init__(self):
        return
    
    def quick_sort(self, iteravel):
        if len(iteravel) == 0:
            return []
        else:
            pivot = iteravel.pop()
            maiores = [x for x in iteravel if x >= pivot]
            menores = [x for x in iteravel if x < pivot]
            return self.quick_sort(menores) +[pivot]+ self.quick_sort(maiores)

    def ref (self,elemento, iteravel):
        ref = 0
        for x in iteravel:
            if x == elemento:
                return ref
            else:
                ref += 1
