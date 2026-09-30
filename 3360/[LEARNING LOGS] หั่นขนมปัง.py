"""[LEARNING LOGS] หั่นขนมปัง"""
# w คู่ m x
# h คู่ n y
w, h, m, n = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
m += 0
n += 0
now = 0
hgap = []
wgap = []

# หา gap ของแนวตั้ง
for i in x:
    gap = i - now
    wgap.append(gap)
    now = i
wgap.append(w - now)

# หา gap ของแนวนอน
now = 0
for k in y:
    gap = k - now
    hgap.append(gap)
    now = k
hgap.append(h - now)

wgap.sort(reverse=True)
hgap.sort(reverse=True)
bw = wgap[:2]
bh = hgap[:2]

biggest = max(bw) * max(bh)
big =  max(bw[1] * bh[0], bw[0] * bh[1])
print(biggest, big)
