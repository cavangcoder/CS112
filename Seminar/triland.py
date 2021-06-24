def ccw(a,b,c) :
    ans1 = (a[0] - b[0]) * (a[1] + b[1])
    ans2 = (b[0] - c[0]) * (b[1] + c[1])
    ans3 = (c[0] - a[0]) * (c[1] + a[1])
    return ans1 + ans2 + ans3

# Nhập dữ liệu
n = int(input())

points = []
for i in range(n) :
    x,y = map(int,input().split())
    points.append((x,y))

points.sort(key=lambda tup: (tup[1], tup[0]))

# Tìm bao lồi
left = []
right = []

for point in points :
    
    while (len(left) > 1 and ccw(left[-2],left[-1],point) >= 0) :
        left.pop()

    while (len(right) > 1 and ccw(right[-2],right[-1],point) <= 0) :
        right.pop()

    left.append(point)    
    right.append(point)

convex_hull = right.copy()
if len(left) > 2 : convex_hull = convex_hull + left[-2:0:-1]

ans = 0

n = len(convex_hull)


# Tìm tam giác có diện tích lớn nhất
# Duyệt tăng dần thứ tự các cặp đỉnh (i)(k) có thể
# Do k tăng liên tục trong mỗi lần duyệt một đỉnh i => đỉnh (j) ở giữa (i)(k) cũng sẽ tăng dần
for i in range(n-2) :
    j = i + 1
    for k in range(i+2,n) :
        while ccw(convex_hull[i],convex_hull[j+1],convex_hull[k]) > ccw(convex_hull[i],convex_hull[j],convex_hull[k]) :
            j += 1
        ans = max(ans,ccw(convex_hull[i],convex_hull[j],convex_hull[k]))

print(ans>>1, end ="") #  ans>>1 = ans // 2
if ans % 2 == 0 :
    print(".0")
else :
    print(".5")
