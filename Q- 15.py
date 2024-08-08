# Given two rectangles,
# find if the given two rectangles overlap or not.
# A rectangle is denoted by providing the x and y coordinates of two points:
# the left top corner and the right bottom corner of the rectangle.
# Two rectangles sharing a side are considered overlapping.
# (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).

def over_lap(l1,r1,l2,r2):
    if ( r1[0]>l2[0] and l1[1]>r2[1] and r1[0]<r2[0] ):
        return ("the rectangles overlap")
    elif ( r1[0]>l2[0] and l1[1]<l2[1] and r1[1]<l2[1]):
        return ("the rectangles overlap")
    elif ( r1[0]>r2[0] and r1[1]<r2[1] and l1[1]>r2[1]):
        return ("the rectangles overlap")
    elif ( r1[0]>r2[0] and l1[1]>l2[1] and r1[1]<l2[1]):
        return ("the rectangles overlap")
    else:
        return ("rectangles don't overlap")

print(over_lap([0,2],[1,1],[-2,0],[0,-3]))