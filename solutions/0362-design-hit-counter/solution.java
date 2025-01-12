class HitCounter {
    private Queue<Integer> hits; 
    public HitCounter() {
        this.hits = new LinkedList<Integer>();
    }
    


    public void hit(int timestamp) {
        this.hits.add(timestamp);
    }
    


    public int getHits(int timestamp) {
        while (!this.hits.isEmpty()) {
            int diff = timestamp - this.hits.peek();
            if (diff >= 300) this.hits.remove();
            else break;
        }
        return this.hits.size();
    }
}
