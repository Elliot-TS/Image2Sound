import numpy as np

#*****************************************************************************80
#
## D2XY converts a 1D Hilbert coordinate to a 2D Cartesian coordinate.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 January 2016
#
#  Parameters:
#
#    Input, integer M, the index of the Hilbert curve.
#    The number of cells is N=2^M.
#    0 < M.
#
#    Input, numpy array D, the Hilbert coordinates of each cell.
#    0 <= D < N * N.
#
#    Output, numpy matrix X, Y, the Cartesian coordinates of the cell.
#    0 <= X, Y < N.
#
def d2xy (m, d):
    n = 2 ** m

    x = np.zeros(d.size, dtype=int)
    y = np.zeros(d.size, dtype=int)

    t = np.copy(d)
    s = 1

    while (s < n):

        rx = ( ( t // 2 ) % 2 )
        ry = np.copy(t)
        ry[rx != 0] ^= rx[rx != 0]
        ry %= 2

        x, y = rot(s, x, y, rx, ry)

        x = x + s * rx
        y = y + s * ry
        t = t // 4

        s = s * 2
    return x, y

#*****************************************************************************80
#
## ROT rotates and flips a quadrant appropriately.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 January 2016
#
#  Parameters:
#
#    Input, integer N, the length of a side of the square.
#    N must be a power of 2.
#
#    Input/output, integer X, Y, the coordinates of a point.
#
#    Input, integer RX, RY, ???
#

def rot (n, x, y, rx, ry):
    # Reflect if needed
    # if ry == 0 and rx = 1, x = n - 1 - x, and y = n - 1 - y
    x[np.logical_and(rx == 1, ry == 0)] = n - 1 - x[np.logical_and(rx == 1, ry == 0)]
    y[np.logical_and(rx == 1, ry == 0)] = n - 1 - y[np.logical_and(rx == 1, ry == 0)]

    # Flip
    t = x[ry == 0]
    x[ry == 0] = y[ry == 0]
    y[ry == 0] = t

    return x, y


def d2xy_test():
    m = 3
    n = 2 ** m

    d = np.arange(n*n);
    #print(d)
    x, y = d2xy(m,d)
    #print(d)
    print(np.array([d,x,y]).transpose())
    return

def rot_test():
    m = 3
    n = 2 ** m
    ry = np.zeros(n)

    for yy in range(0, n):
        x = np.arange(n)
        y = np.repeat(yy, n)
        rx = np.zeros(n)
        x0 = np.copy(x)
        y0 = np.copy(y)
        x0, y0 = rot(n, x0, y0, rx, ry)
        rx = np.repeat(1, n)
        x1 = np.copy(x)
        y1 = np.copy(y)
        x1, y1 = rot( n, x1, y1, rx, ry)
        print(np.array([x,y,x0,y0,x1,y1]).transpose())
    return
