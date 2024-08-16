import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        //int[] answer = {};
        int time = 0;
        int count = 0;
        int n = progresses.length;
        List<Integer> list = new ArrayList<>();
        while(n > 0){
            if(progresses[0]+speeds[0]*time>=100){
                count += 1;
                for(int i=1;i<n;i++){
                    progresses[i-1] = progresses[i];
                    speeds[i-1] = speeds[i];
                }
                n-=1;
            }
            else {
                if(count!=0){
                    list.add(count);
                    count = 0;
                }
                time+=1;
            }
            
        }
        list.add(count);
        int[] answer = {};
        for(int i=0;i<list.size();i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
}