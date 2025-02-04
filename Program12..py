def poi_pos(r,center,point):
    dist = ((center[0]**2 - point[0]**2) - (center[1]**2 - point[1]**2))**0.5
    if dist > r:
        print("Point lies outside the circle.")
    elif dist == r:
        print("Point lies on the circle.")
    else:
        print("Point lies inside the circle")    

r = int(input("Enter radius: "))
cx = int(input("Enter center x: "))
cy = int(input("Enter center y: "))
px = int(input("Enter point x: "))
py = int(input("Enter point y: "))

poi_pos(r,(cx,cy),(px,py))
