l = []

with open ('nyc_weather.csv','r') as f:
    next(f)
    for line in f:
        t = line.strip().split(",")
        l.append(int(t[1]))
print(l)

avg = sum(l[0:7]) / len(l[0:7])
print(avg)

print(max(l[:10]))

d = {}
with open("poem.txt", "r") as file:
    for line in file:
        tem = line.strip('').split(" ")
        for elm in tem:
            if elm in d.keys():
                d[elm] += 1
            else:
                d[elm] = 1

print(d)