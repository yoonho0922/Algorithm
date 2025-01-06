package algorithm;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Interview215 {

    public int findKthLargest(int[] nums, int k) {

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int num : nums) {
            pq.offer(num);

            if(pq.size() > k) pq.poll();
        }

        return pq.poll();
    }
}
