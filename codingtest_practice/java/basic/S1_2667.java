import java.io.*;
import java.util.*;

public class S1_2667 {
    static int N, cnt, res;
    static int[][] v;
    static int[][] apt;

    static List<Integer> ans;

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in)
        );

        N = Integer.parseInt(br.readLine());
        apt = new int[N][N];
        v = new int[N][N];
        res = 0;

        ans = new ArrayList<>();

        cnt = 1;

        for (int i=0; i<N; i++) {
            String line = br.readLine();
            char[] charArray = line.toCharArray();
            for (int j=0; j<N; j++) {
                apt[i][j] = Integer.parseInt(String.valueOf(charArray[j]));
            }
        }

        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (apt[i][j] == 1 && v[i][j] == 0) {
                    bfs(i, j);
                }
            }
        }
        sb.append(cnt-1);
        sb.append("\n");

        Collections.sort(ans);
        for (int i=0; i<ans.size(); i++) {
            sb.append(ans.get(i));
            sb.append('\n');
        }

        System.out.println(sb);
    }

    private static void bfs(int r, int c) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {r, c});
        v[r][c] = cnt;
        res = 1;

        while (!queue.isEmpty()) {
            int now[] = queue.poll();

            for (int d=0; d<4; d++) {
                int nr = now[0] + dr[d];
                int nc = now[1] + dc[d];

                if (0<=nr && nr<N && 0<=nc && nc<N) {
                    if (apt[nr][nc] == 1 && v[nr][nc] == 0) {
                        v[nr][nc] = cnt;
                        queue.offer(new int[] {nr, nc});
                        res += 1;
                    }
                }
            }
        }
        cnt += 1;
        ans.add(res);
    }
}