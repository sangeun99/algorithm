import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Points {
    int x;
    int y;

    public Points(int x, int y) {
        this.x = x;
        this.y = y;
    }

    int getX(){
        return x;
    }

    int getY(){
        return y;
    }
}

public class Main {
    public static int[][] miro;
    public static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        miro = new int[n + 1][m + 1];
        visited = new boolean[n + 1][m + 1];
        for (int i = 0; i <= n; i++) {
            Arrays.fill(visited[i], false);
        }

        for (int i = 1; i <= n; i++) {
            String row = bf.readLine();
            for (int j = 1; j <= m; j++) {
                miro[i][j] = Integer.parseInt(row.substring(j - 1, j));
            }
        }

        int dx[] = {1, 0, -1, 0};
        int dy[] = {0, 1, 0, -1};

        Queue<Points> q = new LinkedList<>();
        q.add(new Points(1, 1));

        while (!q.isEmpty()) {
            Points currPoint = q.poll();
            int currX = currPoint.getX();
            int currY = currPoint.getY();

            if (!visited[currX][currY]){
                visited[currX][currY] = true;
                // 주변 포인트 체크
                for (int i = 0; i < 4; i++){
                    if ((currX + dx[i] > 0) && (currX + dx[i] <= n) && (currY + dy[i] > 0) && (currY + dy[i] <= m)){
                        if ((!visited[currX + dx[i]][currY + dy[i]]) && (miro[currX + dx[i]][currY + dy[i]] != 0)) {
                            q.add(new Points(currX + dx[i], currY + dy[i]));
                            miro[currX + dx[i]][currY + dy[i]] = miro[currX][currY] + 1;
                        }
                    }
                }
            }
        }
        System.out.println(miro[n][m]);
    }
}
