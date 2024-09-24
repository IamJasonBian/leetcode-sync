class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (head == nullptr) return nullptr;
        
        ListNode *slow = head;
        ListNode *fast = head;

        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                while (fast != head) {
                    head = head->next;
                    fast = fast->next;
                }
                return head;
            }
        }
        return nullptr;
    }
};
