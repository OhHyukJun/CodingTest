import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int max_height = 0;
        int max_width = 0;
        for(int i=0;i<sizes.length;i++){
            for(int j=0;j<sizes[i].length;j++){
                if(sizes[i][0]>=sizes[i][1]){
                    max_width = Math.max(max_width,sizes[i][0]);
                    max_height = Math.max(max_height,sizes[i][1]);
                }
                else{
                    max_width = Math.max(max_width,sizes[i][1]);
                    max_height = Math.max(max_height,sizes[i][0]);
                }          
            }
        }
        return max_width*max_height;
    }
}