/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if(head==null)
    {
        return null;
    }
    //step 1 : create a new node for each nod ein the original list and interweave them
    Node current = head;
    while(current!=null)
    {
        Node copy = new Node(current.val);
        copy.next=current.next;
        current.next=copy;
        current=copy.next;
    }
   
   //step2 : set the random pointers for new nodes.

   current=head;
   while(current!=null)
   {
    Node copy = current.next;
    copy.random = (current.random!=null) ? current.random.next : null;
    current = copy.next;
   }

   //step 3 : separate the original and copy list

Node original = head;
Node copyHead = head.next;
Node copy = copyHead;
while(original!=null)
{
    original.next = copy.next;
    original=original.next;

    if(original!=null)
    {
        copy.next = original.next;
        copy = copy.next;
    }
}
copy.next=null;

return copyHead;


    }
}
