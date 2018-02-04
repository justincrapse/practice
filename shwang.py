from blue import Blue

class Water(Blue):
    def laugh(self):
        print('yum yum')

class Oil(Blue):
    pass

mi = Water()
print(isinstance(mi, Oil))