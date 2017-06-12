/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * @param head a ListNode
     * @param val an integer
     * @return a ListNode
     */
    ListNode *removeElements(ListNode *head, int val) {
        // Write your code here
        while(head != NULL and head->val == val) head = head->next;
        ListNode* p = head;
        while(p != NULL and p->next != NULL){
            if(p->next->val == val) p->next = p->next->next;
            else p = p->next;
        }
        return head;
    }
};