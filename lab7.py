# Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию.
# В программе должны быть реализованы минимум один класс, три атрибута, два метода


# Вариант 14. Конвейер сборки состоит из 10 технологических мест. На 4 из них требуется силовая подготовка (мужчины).
# Конвейер должен работать в 2 смены. Сформировать все возможные варианты рабочего расписания, если в цехе работает 20 рабочих: 12 женщин и 8 мужчин.
# "Часть 2:
# На заводе заметили, что разговоры между мужчинами занимают рабочее время,"
# "потому было решено ввести правило: мужчины на смене не могут стоять рядом на конвейере"
# "Все возможные смены с четыремя мужчинами и оставшимися женщинами между ними:"


class ShiftOMatic:
    men = 'M' * 4
    women = 'W' * 6
    shifts = []

    def __init__(self, shift):
        self.shift = shift

    def generate_shifts(self, shift_size_unused=None):
        pool = tuple(self.shift)
        shift_size_length = len(pool)
        shift_size = shift_size_length if shift_size_unused is None else shift_size_unused
        if shift_size > shift_size_length:
            return
        indices = list(range(shift_size_length))
        cycles_count = list(range(shift_size_length, shift_size_length - shift_size, -1))
        yield tuple(pool[x] for x in indices[:shift_size])
        while shift_size_length:
            for i in reversed(range(shift_size)):
                cycles_count[i] -= 1
                if cycles_count[i] == 0:
                    indices[i:] = indices[i + 1:] + indices[i:i + 1]
                    cycles_count[i] = shift_size_length - i
                else:
                    j = cycles_count[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    yield tuple(pool[i] for i in indices[:shift_size])
                    break
            else:
                return

    def separate_shifts(self):
        shift_separator = []
        new_shifts = []
        shifts = list(set(self.generate_shifts()))
        for i in range(len(shifts)):
            shift_separator.append(str(shifts[i]).replace('(', '').replace(')', '').replace("'", "").replace(',', '').replace(' ', ''))
        for i in shift_separator:
            if not 'MM' in i:
                new_shifts.append(i)
        print("На заводе заметили, что разговоры между мужчинами занимают рабочее время,"
              " потому было решено ввести правило: мужчины на смене не могут стоять рядом на конвейере\n"
              " Все возможные смены с четыремя мужчинами и оставшимися женщинами между ними:")
        for i in range(len(new_shifts)):
            print('Смена ' + str(i+1) + ': ' + str(new_shifts[i]))


schedule = ShiftOMatic(getattr(ShiftOMatic, 'men') + getattr(ShiftOMatic, 'women'))


ShiftOMatic.separate_shifts(schedule)
