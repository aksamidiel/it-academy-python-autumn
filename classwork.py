import random
class WithProtected:
    def __init__(self, seed):
        self.seed = seed

    @staticmethod
    def _myhidden(seed, num):
        #secret
        random.seed(seed)
        return num + random()

    def randomize(self, num):
        random.seed(self._myhidden(num))

a = WithProtected()