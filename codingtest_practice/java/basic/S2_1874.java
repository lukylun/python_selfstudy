import java.io.*;
import java.util.*;
public class S2_1874 {
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in)
        );

        int N = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();
//
//        int start = 0;
//
//        while (N-- > 0) {
//            int target = Integer.parseInt(br.readLine());
//
//            if (target > start) {
//                for (int i = start + 1; i <= target; i++) {
//                    stack.push(i);
//                    sb.append('+' + "\n");
//                }
//                start = target;
//            }
//            else if (stack.peek() != target) {
//                System.out.println("NO");
//                return;
//            }
//
//            stack.pop();
//            sb.append('-' + "\n");
//        }
//
//        System.out.println(sb);
        int A[] = new int[N];
        for (int i=0; i<N; i++) {
            A[i] = Integer.parseInt(br.readLine());
        }

        int num = 1;
        boolean res = true;
        StringBuffer bf = new StringBuffer();
        for (int i=0; i<A.length; i++) {
            int su = A[i];
            if (su >= num) {
                while (su>=num) {
                    stack.push(num++);
                    System.out.println(stack);
                    bf.append("+\n");
                }
                stack.pop();
                bf.append("-\n");
            }
            else {
                int n = stack.pop();
                if (n > su) {
                    System.out.println("NO");
                    res = false;
                    break;
                }
            }
        }
        if (res) System.out.println(bf.toString());
    }
}
