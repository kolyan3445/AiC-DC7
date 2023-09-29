#Вариант 14. Конвейер сборки состоит из 10 технологических мест. На 4 из них требуется силовая подготовка (мужчины).
#Конвейер должен работать в 2 смены. Сформировать все возможные варианты рабочего расписания, если в цехе работает 20 рабочих: 12 женщин и 8 мужчин.
#TODO: Новая техника - меньше требуется в смену - не требуется силовая подготовка
#Новая техника увеличила эффективность в 2 раза, потому требования по местам снижены в 2 раза, как и требования по физ. подготовке

class ShiftOMatic:
    def __init__(self, iterable, r=None):
        self.pool = tuple(iterable)
        self.n = len(self.pool)
        self.r = self.n if r is None else r
        if self.r > self.n:
            return
        self.indices = list(range(self.n))
        self.cycles = list(range(self.n, self.n - self.r, -1))

    def generate_shifts(self):
        yield tuple(self.pool[i] for i in self.indices[:self.r])
        while self.n:
            for i in reversed(range(self.r)):
                self.cycles[i] -= 1
                if self.cycles[i] == 0:
                    self.indices[i:] = self.indices[i + 1:] + self.indices[i:i + 1]
                    self.cycles[i] = self.n - i
                else:
                    j = self.cycles[i]
                    self.indices[i], self.indices[-j] = self.indices[-j], self.indices[i]
                    yield tuple(self.pool[i] for i in self.indices[:self.r])
                    break
            else:
                return

shift = 'M' * 8 + 'W' * 12
shift_o_matic = ShiftOMatic(shift, 5)
shifts = list(set(shift_o_matic.generate_shifts()))

print("Новая техника увеличила эффективность в 2 раза, потому требования по местам снижены в 2 раза, как и требования по физ. подготовке \nРасписание в соответствии с новыми условиями:")

for i in shifts:
    print(i)