// # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// # You may assume that each input would have exactly one solution, and you may not use the same element twice.

// # You can return the answer in any order.

// # Example 1:

// # Input: nums = [2,7,11,15], target = 9
// # Output: [0,1]
// # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
// # Example 2:

// # Input: nums = [3,2,4], target = 6
// # Output: [1,2]
// # Example 3:

// # Input: nums = [3,3], target = 6
// # Output: [0,1]
// # ================================================================================================
import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // int[] b={0,0};
        // for ( int i =0;i<nums.length;i++){
        //     int valu = target - nums[i];
        //     for(int j = i+1; j<nums.length;j++){
        //         if (valu == nums[j]){
        //             b[0] = i;
        //             b[1] =j;
        //             return b;
        //         } 
        //     }   
        // }
        // return b;

        int[] b={0,0};
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i<nums.length; i++){
            int valu = target - nums[i];
            if(map.containsKey(valu)){
                int[] a ={map.get(valu), i};
                return a;
            }
            else{
                map.put(nums[i],i);
            }
        }
        return b;
    }
}
class Main{

    public static void main(String args[]) {
        Solution s = new Solution();
        int[] nums = new int[]{5,6,7,4,2,3};
        int target = 9;
        int[] a = s.twoSum(nums, target);
        System.out.println(a[0] );
        System.out.println(a[1]);
        
    }
}
