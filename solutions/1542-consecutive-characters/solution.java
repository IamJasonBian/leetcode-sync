/*
 * This solution uses the Two Pointers algorithm to find the maximum power of a string.
 * The Two Pointers technique involves using two indices to traverse the string.
 * One pointer marks the start of a sequence of identical characters, while the other
 * traverses the string to find the end of this sequence. The length of the sequence
 * is calculated and the maximum length is updated accordingly.
 */

class Solution {
    public int maxPower(String s) {
        
        // Initialize the maximum power to 1 since the minimum length of a substring is 1
        int maxPower = 1;
        
        // Initialize the current power to 1
        int currentPower = 1;
        
        // Traverse the string starting from the second character
        for (int i = 1; i < s.length(); i++) {
            
            // Check if the current character is the same as the previous one
            if (s.charAt(i) == s.charAt(i - 1)) {
                
                // Increment the current power as the sequence continues
                currentPower++;
            } else {
                
                // Reset the current power to 1 as the sequence breaks
                currentPower = 1;
            }
            
            // Update the maximum power if the current power is greater
            maxPower = Math.max(maxPower, currentPower);
        }
        
        // Return the maximum power found
        return maxPower;
    }
}
