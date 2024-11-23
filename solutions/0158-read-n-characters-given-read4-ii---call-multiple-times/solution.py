from collections import deque
class Solution:
    def __init__(self):
        self.storage = deque() 
    
    def read(self, buf: List[str], n: int) -> int:
        while len(self.storage) < n:
            temp_buf = [""] * 4 
            num_bytes_recvd = read4(temp_buf)

            if num_bytes_recvd == 0:
                break

            for i in range(num_bytes_recvd):
                self.storage.append(temp_buf[i])

        if n <= len(self.storage):
            for i in range(n):
                buf[i] = self.storage.popleft()            
            return n
        else:
            count = 0
            while len(self.storage) > 0:
                buf[count] = self.storage.popleft()
                count+=1

            return count
