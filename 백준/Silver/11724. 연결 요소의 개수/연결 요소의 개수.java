import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static ArrayList<Integer>[] graph;
    public static boolean visited[];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        // graph, visited 초기화
        graph = new ArrayList[n + 1];
        visited = new boolean[n + 1];

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < m; i++){
            int s = sc.nextInt();
            int e = sc.nextInt();
            // graph 배열에 넣기
            graph[s].add(e);
            graph[e].add(s);
        }

        int count = 0;
        // DFS 실행하기
        for (int i = 1; i <= n; i++){
            if (!visited[i]) {
                count++;
                DFS(i);
            }
        }
        System.out.println(count);
    }

    // DFS를 돌면서 visited를 T로 바꿔주고 만약 이미 visited가 T라면 방문하지 않음
    private static void DFS(int i) {
        if (visited[i]) return;
        visited[i] = true;
        for (int j = 0; j < graph[i].size(); j++){
            DFS(graph[i].get(j));
        }
    }
}
