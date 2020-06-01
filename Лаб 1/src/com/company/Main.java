public class Main{
    public static void main(String [] args){
        double S = 0;
        float a = 1;
        float b = 2;
        int n = 3;
        int m = 2;
        final int C = 2;

        for (float i = a; i <= n; i++){
            for(float j = b; j <= m; j++){
                 S = S + ((i-j)/(i+C));
            }
        }
        System.out.println(S);
    }
}