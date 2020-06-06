import operator


class Flower(object):
    def __init__(self, price, fresh, len_f):
        self.price = price
        self.fresh = fresh
        self.len_f = len_f
        self.name = "Квітка"

    def __str__(self):                              # y.о - умовні одиниці
        return str(str("Квітка у букеті : {0}, Ціна : {1} у.о., Свіжість : {2} у.о., Довжина стебла квітки :"
                       " {3}".format(self.name, self.price, self.fresh, self.len_f)))

    def get_price(self):
        return self.price

    def get_e_len_f(self):
        return self.len_f

    def __getitem__(self, item):
        if item == 'price':
            return self.price
        elif item == 'fresh':
            return self.fresh
        elif item == 'len_f':
            return self.len_f
        else:
            return None


class Rose(Flower):  # квітка 1
    def __init__(self, price, fresh, len_f):
        Flower.__init__(self, price, fresh, len_f)
        self.name = "Троянда"


class Chamomile(Flower):   # квітка 2
    def __init__(self, price, fresh, len_f):
        Flower.__init__(self, price, fresh, len_f)
        self.name = "Ромашка"


class Tulip(Flower):  # квітка 3
    def __init__(self, price, fresh, len_f):
        Flower.__init__(self, price, fresh, len_f)
        self.name = "Тюльпан"


class Orchid(Flower):   # квітка 4
    def __init__(self, price, fresh, len_f):
        Flower.__init__(self, price, fresh, len_f)
        self.name = "Орхідея"


def comparator(param):
    return operator.attrgetter(param)

l = []


def get_price(l):
    price = 0
    for i in l:
        price += i.get_price()
    return price


def find_by_length(l, start, end):
    return [i for i in l if i.get_e_len_f() <= end and i.get_e_len_f() >= start]