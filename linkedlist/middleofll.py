class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        #size 1 list

        if head.next==None:
            return head
        
        pointer1=head
        pointer2=head
        
        if head.next!=None:
            while pointer2!=None and pointer2.next!=None:
                pointer1=pointer1.next
                pointer2=pointer2.next.next
            
            return pointer1