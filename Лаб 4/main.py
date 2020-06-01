class Clothing:
    def __init__(self):
        # Словник clothing містить набір речей з вказаною для них вартістю
        clothing = {"T-shirt": 10, "hat": 5, "jacket": 25, "coat": 30, "shorts": 15}
        # Наступні два рядки сторюють словник за значенням
        list_a = list(clothing.items())
        list_a.sort(key=lambda i: i[1])
        print("Сортування за зростанням:")
        for i in list_a:
            print(i[0], ':', i[1])

        list_b = list_a
        list_b.reverse()
        print("Сортування за спаданням:")
        for i in list_b:
            print(i[0], ':', i[1])


Clothing()