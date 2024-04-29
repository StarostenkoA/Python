string1="1 2 11 22"#input("enter str1 with number:")
string2="1 2 22 33"#input("enter str2 with number:")
string3="1 2 33 44"#input("enter str3 with number:")

set1=set(map(int,string1.split()))
set2=set(map(int,string2.split()))
set3=set(map(int,string3.split()))

res1 = set1.union(set2).union(set3)
print(f"unique {sorted(res1)}")

res2 =set1.intersection(set2).intersection(set3)
print(f"intersection {sorted(res2)}")

print(f"difference {(set1 | set2 | set3) ^ ((set1 & set2) | (set1 & set3) | (set2 & set3)) }")
