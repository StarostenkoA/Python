li=['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
k=1
for i in li:
    print(f"{k} - {i} - {i[k-1]}")
    k += 1
