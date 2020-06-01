class Lab_2:
    def funk_XOR(self):
        A = [['1', '2', '3', '4'],
             ['4', '5', '6', '2']]
        B = [['5', '6', '7', '8'],
             ['4', '5', '6', '3']]
        a = list('0'*len(B[0]))
        b = list('0'*len(A[0]))
        i = 0
        j = 0
        for element in A:
            A[i] = element + a
            i = +1

        for element1 in B:
            B[j] = b + element1
            j = +1
        C = A + B
        print("Множина С:", C)
        return C
    def func_main(self, C):
        i = 1
        D = []
        for element in C:
            min_val = int(min(C[i]))
            D.append(min_val)
            if i == 2:
                break
            i = +2
        print("Сума найменших елементів парних рядків:", sum(D))

        j = 0
        Q = []
        for element in C:
            max_val = int(max(C[j]))
            Q.append(max_val)
            if j == 2:
                break
            j = +2
        print("Сума найбільших елементів непарних рядків:", sum(Q))

a = Lab_2()
C = a.funk_XOR()
a.func_main(C)