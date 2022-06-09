class Tomato:
    states = {
        1: 'Отсутствует',
        2: 'Цветение',
        3:  'Зеленый',
        4:  'Красный'
        }
    def init(self):
        self._index = 1
        self._state = self.states[self._index]
        
    def grow(self):
        self._index +=1
        self._state = self.states[self._index]
        print(f'Томат перешел на стадию {self._state}')

    def info(self):
        return f'Томат на стардии {self._state}'
    
    def is_ripe(self):
        if self._index == 4:
            print(f'Томат Поспел')
            return True
        return False
    def str(self) -> str:
        return 'Томат'

class TomatoBush:
    def init(self, number_tomato):
        self.number_tomato = number_tomato
        self.tomatoes = []
        for i in range(self.number_tomato):
            self.tomatoes.append(Tomato())
    
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
    
a = TomatoBush(6)

for i in a.tomatoes:
    print(i.info())

a.grow_all()
a.grow_all()
a.grow_all()

for i in a.tomatoes:
    print(i.info())