# Calculate the angle between the hour hand and minute hand.

def calang(h,m):
    if ( h>12 or m>60 or m<0 or h<0):
        print("invalid value")
    if ( h == 12):
        h = 0
    if (m == 60):
        m = 0
        h += 1
        if (h>12):
            h = h - 12
    h_ang = 0.5 * ( 60* h + m)
    m_ang = m * 6
    ang = abs(h_ang - m_ang)
    ang = min(360 - ang , ang)
    return ang

print(calang(3,30))