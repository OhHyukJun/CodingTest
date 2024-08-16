import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        List<Integer> list = new ArrayList<>();
        for(int i=0;i<commands.length;i++){
            List<Integer> command = new ArrayList<>();
            for(int j=0;j<commands[i].length;j++){
                command.add(commands[i][j]);
            }
            int[] subArray = Arrays.copyOfRange(array,command.get(0)-1,command.get(1));
            Arrays.sort(subArray);
            list.add(subArray[command.get(2)-1]);
            //System.out.println(list);
        }
        for(int i=0;i<list.size();i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
}