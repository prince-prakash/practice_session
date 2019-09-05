class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = student(m1, m2)
        return m3
    def __lt__(self, other):
        m1 = self.m1 + other.m2
        m2 = self.m2 + other.m2
        if m1 < m2:
            return True
        else:
            return False

s1 = student(26, 60)
s2 = student(30, 55)
s3 = s1 + s2
print(s3.m1, s3.m2)
if s1 < s2:
    print("wins")
else:
    print("lose")