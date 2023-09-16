typedef struct node {
    int key;
    struct node *next;
} NODE;

#define HASH_SIZE   65536

NODE *hash[HASH_SIZE];

int hash_init()
{
    memset((void *)hash, 0, sizeof(hash));
    return 0;
}

int hash_add(int key)
{
    NODE *p_new;

    p_new = (NODE *)malloc(sizeof(NODE));
    p_new->key = key;
    
    key %= HASH_SIZE;
    key = abs(key);
    
    p_new->next = hash[key];
    hash[key] = p_new;

    return 0;
}

bool hash_search(int key)
{
    NODE *p_node;
    int key2 = abs(key % HASH_SIZE);

    p_node = hash[key2];
    
    while (p_node) {
    
        if (p_node->key == key) {
            return true;
        }
    
        p_node = p_node->next;
    }
    
    return false;
}

int hash_release()
{
    NODE *p_tmp;
    NODE *p_del;

    for (int i = 0; i < HASH_SIZE; i++) {
        p_tmp = hash[i];
        
        while (p_tmp) {
            p_del = p_tmp;
            p_tmp = p_tmp->next;
            free(p_del);
        }
    }
    
    return 0;
}

int longestConsecutive(int* nums, int numsSize){
    /*
     * Input:
     *  nums, integer array
     *  numsSize, size of array
     */
     
    /*
     * Algorithm:
     *  Brute force? O(N^3)
     *  Hash? the time complexity may be larger than O(N)
     */
     
    int len;
    int max = 0;
    
    /* initialize hash table */
    hash_init();
    
    /* Add all the integers to hash table */
    for (int i = 0; i < numsSize; i++) {
        hash_add(nums[i]);
    }
    
    for (int i = 0; i < numsSize; i++) {
    
        /* Check if this is the first number of a consecutive elements sequence */
        if (hash_search(nums[i] - 1) == false) {
        
            len = 0;
        
            /* Measure the length of sequence */
            for (int j = nums[i]; j <= 1000000000; j++) {
                if (hash_search(j) == false) {
                    break;
                }
                
                len++;
            }
        
            /* Restore the length of longest sequence */
            if (len > max) {
                max = len;
            }
        }
    }
    
    /* Release hash table */
    hash_release();
     
    /*
     * Output:
     *  return the length of the longest consecutive elements sequence.
     */
     
    return max;
}
