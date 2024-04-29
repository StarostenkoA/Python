string=input("enter str:")
set1 = set(string)
print(f"count unique chars={len(set1)}")

set2 = set(string.split())
print(f"count unique words={len(set2)}")

from collections import Counter
c = Counter(string)
print(f"most common {c.most_common(1)[0][0]}")
