class FishNumber:
    def __init__(self,nb) -> None:
        self.nb=nb

    def __add__(self,b):
        return FishNumber("["+self.nb+","+b.nb+"]")

    def __str__(self):
        return self.nb