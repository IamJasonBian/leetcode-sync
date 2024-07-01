import java.util.PriorityQueue;
import java.util.Collections;

public class MedianFinder {

    private PriorityQueue<Integer> minHeap; // Stores the larger half of numbers
    private PriorityQueue<Integer> maxHeap; // Stores the smaller half of numbers

    public MedianFinder() {
        minHeap = new PriorityQueue<>(); // Min heap
        maxHeap = new PriorityQueue<>(Collections.reverseOrder()); // Max heap
    }
    
    public void addNum(int num) {
        // Decide which heap to add the number to based on its relation to the current median
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.offer(num);
        } else {
            minHeap.offer(num);
        }
        
        // Balance the heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.offer(maxHeap.poll());
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.offer(minHeap.poll());
        }
    }
    
    public double findMedian() {
        if (maxHeap.isEmpty()) {
            throw new IllegalStateException("No elements added yet.");
        }
        
        if (maxHeap.size() == minHeap.size()) {
            return ((double) maxHeap.peek() + minHeap.peek()) / 2;
        } else {
            return maxHeap.peek();
        }
    }
}

