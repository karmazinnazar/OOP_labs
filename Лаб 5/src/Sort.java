public abstract class Sort {
    //реалізуем Bubble Sort
   public static void  sort(Text a){
        int n=a.text.length;
        for(int i=0;i<n-1;i++){
            for(int j=0;j<n-i-1;j++){
                if(a.text[j].Length()>a.text[j+1].Length()){
                    //міняємо елементи місцями
                    Sentence temp=new Sentence(a.text[j]);
                    a.text[j]=a.text[j+1];
                    a.text[j+1]=temp;
                }
            }
        }
    }
}
