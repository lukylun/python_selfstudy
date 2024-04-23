import java.util.*;
import java.io.*;

public class b1_1032 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in)
        );

        int T = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        char[] cName = st.nextToken().toCharArray();
        if (T==1) {
            System.out.println(cName);
        }
        else {
            for (int t=0; t < T-1; t++) {
                st = new StringTokenizer(br.readLine());
                char[] stName = st.nextToken().toCharArray();
                for (int i=0; i<cName.length; i++) {
                    if (cName[i] != stName[i]) {
                        cName[i] = '?';
                    }
                }
            }
            System.out.println(cName);
        }
    }
}
