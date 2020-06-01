public class Sentence {
    Word[] arr;
    symbols[] arr1;

    public Sentence() {
        arr = new Word[0];
        arr1 = new symbols[0];
    }

    public Sentence(Word[] a, symbols[] b) {
        if (a.length != b.length) {//якщо речення коректне то кількість розділяючих знаків(враховуючи крапку) така ж
                                   // як і кількість слів
            System.out.println("Incorrect sentence");
        }
        arr = a;
        arr1 = b;
    }

    public Sentence(Sentence a) {
        arr=new Word[a.arr.length];
        arr1=new symbols[a.arr.length];
        for (int i = 0; i < a.arr.length; i++) {
            this.arr[i] = a.arr[i];
            this.arr1[i] = a.arr1[i];
        }
    }

    void print() {
        String s = "";
        for (int i = 0; i < arr.length; i++) {
            s += arr[i].String1();
            s += arr1[i].symbol;
        }
        System.out.println(s);
    }

    int Length() {
        int res = 0;
        for (int i = 0; i < arr.length; i++) {
            res += arr[i].Length();// добавляю довжину кожного слова
            res++;//тому,  щто символ завжди довжини 1
        }
        return res;
    }
}
