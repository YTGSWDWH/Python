from part import Interval
def isRectangleOverlap(rec1, rec2):
    zoom_1 = Interval(rec1[0],rec1[2],lower_closed=False,upper_closed=False)
    zoom_2 = Interval(rec1[1],rec1[3],lower_closed=False,upper_closed=False)
    zoom_3 = Interval(rec2[0],rec2[2],lower_closed=False,upper_closed=False)
    zoom_4 = Interval(rec2[1],rec2[3],lower_closed=False,upper_closed=False)
    return zoom_1.overlaps(zoom_3) and zoom_2.overlaps(zoom_4)

rec1 = [5,15,8,18]
rec2 = [0,3,7,9]
print(isRectangleOverlap(rec1,rec2))