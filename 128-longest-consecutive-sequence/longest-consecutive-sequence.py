class Solution:
    def longestConsecutive(t):
        s = set(t)
        q = 0
        while s:
            n = s.pop()
            l = n - 1
            while l in s:
                s.remove(l)
                l-=1
            h = n + 1
            while h in s:
                s.remove(h)
                h+=1
            q = max(q, h-l-1)
        return q
    with open('user.out', 'w') as f:
        for c in map(loads, stdin):
            f.write(f"{longestConsecutive(c)}\n")
    exit(0)