public class Word {
    Letter[] arr;
    public Word(){
        arr=new Letter[0];
    }
    public Word(Letter[] a){
        arr=a;
    }
    String String1(){
        String s="";
        for(int i=0;i<arr.length;i++){
            s+=arr[i].a;
        }
        return s;
    }
    int Length(){
        return arr.length;
    }
}
