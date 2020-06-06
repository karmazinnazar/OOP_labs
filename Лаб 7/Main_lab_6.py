from for_main_lab_6 import *
used_fl = []
while True:
    try:
        c = int(input("1 -> Ствооити/додати квітку у букет\n"
                      "2 -> Підрахувати вартість\n"
                      "3 -> Сортування за свіжістю\n"
                      "4 -> Задати діапазон довжини для квітів в букеті\n"
                      "5 -> Компоненти букету\n"
                      "0 -> Вихід\n"))

        if c == 1:
            c = int(input("1 -> Троянда\n"
                          "2 -> Ромашка\n"
                          "3 -> Тюльпан\n"
                          "4 -> Орхідея\n"))
            if c == 1:
                price = int(input("Ціна: "))
                fresh = int(input("Свіжість: "))
                len_f = int(input("Довжина: "))
                m = Rose(price, fresh, len_f)
                l .append(m)
                used_fl.append("Троянда")
            elif c == 2:
                price = int(input("Ціна: "))
                fresh = int(input("Свіжість: "))
                len_f = int(input("Довжина: "))
                m = Chamomile(price, fresh, len_f)
                l .append(m)
                used_fl.append("Ромашка")
            elif c == 3:
                price = int(input("Ціна: "))
                fresh = int(input("Свіжість: "))
                len_f = int(input("Довжина: "))
                m = Tulip(price, fresh, len_f)
                l .append(m)
                used_fl.append("Тюльпан")
            elif c == 4:
                price = int(input("Ціна: "))
                fresh = int(input("Свіжість: "))
                len_f = int(input("Довжина: "))
                m = Orchid(price, fresh, len_f)
                l .append(m)
                used_fl.append("Орхідея")
            else:
                print("Ви вибрали неправильний номер!")
        elif c == 2:
            print(get_price(l))
        elif c == 3:
            l.sort(key=comparator("fresh"))
            for i in l:
                print(i)
        elif c == 4:
            start = int(input("Початок діапазону: "))
            end = int(input("Кінець діапазону: "))
            for i in find_by_length(l, start, end):
                print(i)
        elif c ==5:
            print("Квіти в букеті: ", ", ".join(used_fl))
            pass
        elif c == 0:
            break
    except ValueError:
        print("Введіть коректний номер!")
