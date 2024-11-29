class Solution:
    def minChanges(self, s: str) -> int:
        current_char = s[0]
        consecutive_count = 0
        min_changes_required = 0
        current_partition = ""
        s_list = list(s)
        pos = 0
        
        for char in s:
            current_partition += char
            if char == current_char:
                consecutive_count += 1
                continue
                
            print(f"Partition: {current_partition}")
            
            if consecutive_count % 2 == 0:
                consecutive_count = 1
            else:
                consecutive_count = 0
                min_changes_required += 1
                if pos > 0:
                    s_list[pos-1] = '1' if s_list[pos-1] == '0' else '0'
            current_char = char
            current_partition = char
            pos += len(current_partition) - 1
            
        print(f"Final partition: {current_partition}")
        print(f"String after changes: {''.join(s_list)}")
        return min_changes_required
