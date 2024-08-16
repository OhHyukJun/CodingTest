class Solution {  
    public int dfs(int depth, int fatigue, int[][] dungeons, boolean[] visited) { 
        int count = depth; // 현재 깊이를 카운트
        for (int i = 0; i < dungeons.length; i++){  
            if (visited[i] || dungeons[i][0] > fatigue) {  
                continue;  
            }  
            visited[i] = true;  
            count = Math.max(count, dfs(depth + 1, fatigue - dungeons[i][1], dungeons, visited));  
            visited[i] = false;  
        }  
        return count; // 최대 깊이를 반환
    }  
    
    public int solution(int k, int[][] dungeons) {  
        boolean[] visited = new boolean[dungeons.length];  
        return dfs(0, k, dungeons, visited); // dfs의 결과를 반환
    }  
}
