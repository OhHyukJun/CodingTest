import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        List<Integer> answerList = new ArrayList<>();
        if(answerList.size() == 0){
                answerList.add(arr[0]);
            }
        for(int i=1;i<arr.length;i++){
            if(arr[i] != arr[i-1]){
                answerList.add(arr[i]);
            }
        }
        answer = answerList.stream().mapToInt(i->i).toArray();
        //System.out.println(answerList);
        return answer;
    }
}