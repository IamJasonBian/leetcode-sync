from collections import Counter

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_counts = Counter(ages)
        total_requests = 0
        
        for age_x, count_x in age_counts.items():
            for age_y, count_y in age_counts.items():
                if self.canSendRequest(age_x, age_y):
                    total_requests += count_x * count_y
                    if age_x == age_y:
                        total_requests -= count_x  # Exclude self-requests
        
        return total_requests
    
    def canSendRequest(self, age_x: int, age_y: int) -> bool:
        return not (age_y <= 0.5 * age_x + 7 or age_y > age_x or (age_y > 100 and age_x < 100))
