class MyHashSet {

    private int[] table;
    private final float LOAD_FACTOR = 0.75F;
    private int capacity;
    private int size;

    public MyHashSet() {
        capacity = 6;
        table = new int[capacity];
        Arrays.fill(table, -1);
    }

    public void add(int key) {
        int i = key % capacity;
        while (this.table[i] != -1 && this.table[i] != key) {
            i = (i + 1) % capacity;
        }
        this.table[i] = key;
        if (++this.size > this.capacity * LOAD_FACTOR) {
            resize();
        }
    }

    public void remove(int key) {
        if (!contains(key)) return;
        int i = key % capacity;
        while (this.table[i] != key) {
            i = (++i) % capacity;
        }
        this.table[i] = -1;
        --this.size;
        i = (++i) % capacity;
        while (this.table[i] != -1) {
            int entry = this.table[i];
            this.table[i] = -1;
            --this.size;
            this.add(entry);
            i = (++i) % capacity;
        }
    }

    public boolean contains(int key) {
        int i = key % this.capacity;
        while (this.table[i] != -1) {
            if (this.table[i] == key) {
                return true;
            }
            i = (++i) % this.capacity;
        }
        return false;
    }

    private void resize() {
        int newCapacity = this.capacity * 2;
        int[] oldTable = this.table;
        int[] newTable = new int[newCapacity];
        Arrays.fill(newTable, -1);
        for (int i : oldTable) {
            if (i != -1) {
                int idx = i % newCapacity;
                while (newTable[idx] != -1) {
                    idx = ++idx % newCapacity;
                }
                newTable[idx] = i;
            }
        }
        this.capacity = newCapacity;
        this.table = newTable;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */
