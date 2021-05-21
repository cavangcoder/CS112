# Code demo
# Code tìm và liệt kê tập điểm của bao lồi theo chiều kim đồng hồ

def ccw(a,b,c) :                                    # ccw < 0 : theo chiều kim đồng hồ              
    ans1 = (a[0] - b[0]) * (a[1] + b[1])
    ans2 = (b[0] - c[0]) * (b[1] + c[1])
    ans3 = (c[0] - a[0]) * (c[1] + a[1])
    return ans1 + ans2 + ans3

n = int(input())
points = []

for i in range(n) :
    x,y = map(int,input().split())
    points.append((x,y))

points.sort()

clockwise = []                                      # Stack chứa các phần tử liệt kê theo chiều kim đồng hồ
anticlockwise = []                                  # Stack chứa các phần tử liệt kê ngược chiều kim đồng hồ

for point in points :
    
    while (len(clockwise) > 1 and ccw(clockwise[-2],clockwise[-1],point) >= 0) :
        clockwise.pop()

    while (len(anticlockwise) > 1 and ccw(anticlockwise[-2],anticlockwise[-1],point) <= 0) :
        anticlockwise.pop()

    clockwise.append(point)    
    anticlockwise.append(point)

convex_hull = anticlockwise.copy()

if len(clockwise) > 2 :                              # Kết nối 2 nửa bao lồi
    convex_hull = convex_hull + clockwise[-2:0:-1]

area = 0
convex_hull.append(convex_hull[0])                   # Mượn thêm đỉnh cuối vào bao lồi để tính diện tích

for i in range(len(convex_hull)-1) :
    area += (convex_hull[i][0] - convex_hull[i+1][0]) * (convex_hull[i][1] + convex_hull[i+1][1])

convex_hull.pop()

print(len(convex_hull))
print(area//2,end = '')

if area % 2 == 0 :
    print (".0")
else :
    print (".5")

for x,y in convex_hull :
    print(x,y)