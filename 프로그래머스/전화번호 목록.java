import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        Arrays.sort(nums);
        List<Integer> num_list = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            if(!num_list.contains(nums[i]))
                num_list.add(nums[i]);
        }
        if(num_list.size()>=nums.length/2){
            answer = nums.length/2;
        }
        else{
            answer = num_list.size();
        }
        //System.out.println(num_list);
        return answer;
    }
}
