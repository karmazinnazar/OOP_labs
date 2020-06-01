public class Main {
    public static void main(String[] args) {
        System.out.println("Задані речення:");
        Letter [] arr=new Letter[6];//масив букв
        arr[0]=new Letter('W');
        arr[1]=new Letter('o');
        arr[2]=new Letter('r');
        arr[3]=new Letter('d');
        arr[4]=new Letter('0');
        arr[5]=new Letter('1');
        Letter [] arr1=new Letter[5];//мсив букв
        arr1[0]=new Letter('W');
        arr1[1]=new Letter('o');
        arr1[2]=new Letter('r');
        arr1[3]=new Letter('d');
        arr1[4]=new Letter('2');
        Word andrew=new Word(arr);
        Word anton =new Word(arr1);//створюю два слова
        symbols[] arr2=new symbols[2];
        Word[] arr3=new Word[2];
        arr3[0]=andrew;
        arr3[1]=anton;
        arr2[0]=new symbols(' ');
        arr2[1]=new symbols('.');//создаю массив слів и символів
        Sentence sen=new Sentence(arr3,arr2);
        sen.print();
        Letter [] arr4=new Letter[6];//повторюются дії вище
        arr4[0]=new Letter('W');
        arr4[1]=new Letter('o');
        arr4[2]=new Letter('r');
        arr4[3]=new Letter('d');
        arr4[4]=new Letter('0');
        arr4[5]=new Letter('3');
        Letter [] arr5=new Letter[7];
        arr5[0]=new Letter('W');
        arr5[1]=new Letter('o');
        arr5[2]=new Letter('r');
        arr5[3]=new Letter('d');
        arr5[4]=new Letter('0');
        arr5[5]=new Letter('0');
        arr5[6]=new Letter('4');
        Word andrew1=new Word(arr4);
        Word anton1 =new Word(arr5);
        symbols[] arr6=new symbols[2];
        Word[] arr7=new Word[2];
        arr7[0]=andrew1;
        arr7[1]=anton1;
        arr6[0]=new symbols(' ');
        arr6[1]=new symbols('.');
        Sentence sen1=new Sentence(arr7,arr6);
        sen1.print();
        System.out.println("Утворений текст:");
        Sentence[] arrsen=new Sentence[2];
        arrsen[0]=sen1;
        arrsen[1]=sen;
        Text txt=new Text(arrsen);
        txt.print();
        Sort.sort(txt);
        System.out.println("Відсортований текст:");
        txt.print();//речення мають помінятися місцями оскільк sen1 довше ніж sen
    }
}
