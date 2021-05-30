# ccw < 0 : theo chiều kim đồng hồ
# ccw > 0 : ngược chiều kim đồng hồ
# ccw = 0 : thẳng hàng
def ccw(a,b,c) :   
    ans1 = (a[0] - b[0]) * (a[1] + b[1])
    ans2 = (b[0] - c[0]) * (b[1] + c[1])
    ans3 = (c[0] - a[0]) * (c[1] + a[1])
    return ans1 + ans2 + ans3

n = int(input())

points = []
for i in range(n) :
    x,y = map(int,input().split())
    points.append((x,y))

# Sắp xếp theo trục y, nếu tọa độ y bằng nhau sẽ so sánh đến x
points.sort(key=lambda tup: (tup[1], tup[0])) 

left = []      # đi từ trái qua => theo chiều kim đồng hồ
right = []     # đi từ phải qua => ngược chiều kim đồng hồ 

for point in points :
    
    while (len(left) > 1 and ccw(left[-2],left[-1],point) >= 0) :     # bỏ các đỉnh làm đổi chiều của tập bên trái
        left.pop()

    while (len(right) > 1 and ccw(right[-2],right[-1],point) <= 0) :  # bỏ các đỉnh làm đổi chiều của tập bên phải
        right.pop()

    left.append(point)    
    right.append(point)

# Do đề yêu cầu kết quả phải ngược chiều kim đồng hồ nên ta sẽ kết nối tập bên trái vào tập bên phải
convex_hull = right.copy()
if len(left) > 2 : convex_hull = convex_hull + left[-2:0:-1]

area = 0
convex_hull.append(convex_hull[0])  # Mượn thêm đỉnh đầu tiên vào vị trí cuối cùng để tích diện tích

for i in range(len(convex_hull)-1) :
    area += (convex_hull[i][0] - convex_hull[i+1][0]) * (convex_hull[i][1] + convex_hull[i+1][1])

convex_hull.pop()   # Trả lại đỉnh đã mượn

print(len(convex_hull))
print(abs(area)//2,end='')

if area % 2 == 0 :
    print (".0")
else :
    print (".5")

for x,y in convex_hull :
    print(x,y)