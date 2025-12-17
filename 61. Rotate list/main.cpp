/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        int n=1;
        ListNode* tr=head;
        
        while(tr&&tr->next!=nullptr)
        {
            tr=tr->next;
            n++;
        }      
        k=k%n;
        if(head!=nullptr)
        {
            for(int i = 0;i<k;i++)
            {
                ListNode *temp = head;
                if(temp->next == nullptr)
                {
                    return head;
                }
                else
                {
                    while(temp->next->next!=nullptr)
                    {
                        temp=temp->next;
                    }
                    ListNode *tempx = temp->next;
                    temp->next=NULL;
                    tempx->next=head;
                    head = tempx;
                }
            }
        }
        return head;
    }
};
