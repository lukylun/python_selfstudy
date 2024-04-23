import java.io.*;
import java.util.*;

public class S1_2178 {
    static int[] dr = {0, 1, 0, -1};
    static int[] dc = {1, 0, -1, 0};
//    static int[][] v;
    static boolean[][] v;
    static int[][] miro;


    static int N, M;

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in)
        );
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        v = new boolean[N][M];
        miro = new int[N][M];

        for (int i=0; i<N; i++) {
            String line = br.readLine();
            char[] charArray = line.toCharArray();
            for (int j=0; j<M; j++) {
                miro[i][j] = Integer.parseInt(String.valueOf(charArray[j]));
            }
        }
//        v[0][0] = 1;
        bfs(0, 0);
        System.out.println(miro[N-1][M-1]);
    }

    private static void bfs(int i, int j) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {i, j});
        v[i][j] = true;

        while(!queue.isEmpty()) {
            int now[] = queue.poll();
            for (int d = 0; d<4; d++) {
                int ni = now[0] + dr[d];
                int nj = now[1] + dc[d];

                if (0 <= ni && ni < N && 0 <= nj && nj < M) {
                    if (miro[ni][nj] != 0 && !v[ni][nj]) {
                        queue.add(new int[] {ni, nj});
//                        v[ni][nj] = v[now[0]][now[1]] + 1;
                        v[ni][nj] = true;
                        miro[ni][nj] = miro[now[0]][now[1]] + 1;
                    }
                }
            }
        }
    }
}
