class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        remain = {}
        for st in students:
            remain[st] = 1 + remain.get(st, 0)
        
        i = 0 # sandwiche
        q = collections.deque(students)
        while q:
            sw = sandwiches[i]
            if sw not in remain or remain[sw] == 0:
                break
            
            st = q.popleft()
            if sw == st:
                remain[st] -= 1
                i +=1
            else:
                q.append(st)
        
        return len(q)
        