class Node{
    int val;
    int key;
    int freq;
    Node next;
    Node prev;
    Node(){}
    Node(int key,int val){
        this.key=key;
        this.val=val;
        this.freq=1;
    }
    
}
class LFUCache {
    
    int maxCapacity;
    int freq;
    Map<Integer,Node>keyMap=new HashMap<>();
    Map<Integer,DoublyList>freqMap=new HashMap<>();
    int curCapacity = 0;
    public LFUCache(int maxCapacity) {
      this.maxCapacity=maxCapacity;
    }
    public Node getNode(int key){
        if(!keyMap.containsKey(key)){
            return null;
        }
        Node curNode=keyMap.get(key);
        DoublyList list=freqMap.get(curNode.freq);
        list.deleteNode(key);
        curNode.freq++;
        if(!freqMap.containsKey(curNode.freq)){
            freqMap.put(curNode.freq,new DoublyList());
        }
        freqMap.get(curNode.freq).addNode(curNode);
        return curNode;
    }
    
    public int get(int key) {
        if(!keyMap.containsKey(key)){
            return -1;
        }
        Node curNode=getNode(key);
        return curNode.val;
    }
    
    public void put(int key, int value) {
        if(maxCapacity==0){
            return;
        }
        if(keyMap.containsKey(key)){
            Node curNode=getNode(key);
            curNode.val=value;
        }
        else{
            if(curCapacity==maxCapacity){
                int lowestFreq=Integer.MAX_VALUE;
                for(Integer freq:freqMap.keySet()){
                    if(freqMap.get(freq).map.isEmpty())
                        continue;
                    lowestFreq=Math.min(lowestFreq,freq);
                }
                DoublyList list=freqMap.get(lowestFreq);
                Node curNode=list.deleteHead();
                keyMap.remove(curNode.key);
                curCapacity--;
            }
            int curFreq=1;
            Node curNode=new Node(key,value);
            keyMap.put(key,curNode);
            if(!freqMap.containsKey(curFreq)){
                freqMap.put(curFreq,new DoublyList());
            }
            freqMap.get(curFreq).addNode(curNode);
            curCapacity++;
        }
    }
}
class DoublyList{
    Map<Integer,Node>map=new HashMap<>();
    Node head,tail;

    public DoublyList(){
        head=new Node();
        tail=new Node();
        head.next=tail;
        tail.prev=head;
    }
    public void addNode(Node curNode){
        Node tailPrev=tail.prev;
        tailPrev.next=curNode;
        curNode.prev=tailPrev;
        tail.prev=curNode;
        curNode.next=tail;
        map.put(curNode.key,curNode);
    }
    public Node deleteNode(int key){
        if(!map.containsKey(key))
            return null;

        Node curNode=map.get(key);
        Node prevNode=curNode.prev;
        Node nextNode=curNode.next;
        prevNode.next=nextNode;
        nextNode.prev=prevNode;
        map.remove(key);
        return curNode;
    }
    public Node deleteHead(){
        if(head.next==tail){
            return null;
        }
        Node firstNode=head.next;
       return deleteNode(firstNode.key);
    }
}

