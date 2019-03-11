from scipy.interpolate import spline, splprep, splev
from pylab import *
from scipy.misc import comb
from rdp import rdp

class CreateTraj(object):
    def __init__(self,data):
        self.data = data
        self.getPoint(self.data)


    def bernstein_poly(self,i, n, t):
        """
         The Bernstein polynomial of n, i as a function of t
        """
        return comb(n, i) * (t ** (n - i)) * (1 - t) ** i

    def bezier_curve(self,points, nTimes=100):
        """
           Given a set of control points, return the
           bezier curve defined by the control points.

           points should be a list of lists, or list of tuples
           such as [ [1,1],
                     [2,3],
                     [4,5], ..[Xn, Yn] ]
            nTimes is the number of time steps, defaults to https://www.google.com.tw/search?q=variational+autoencoder+structure&client=ubuntu&channel=fs&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjju8SdssrYAhUJpZQKHcazA8kQ_AUICigB&biw=1855&bih=1100#imgrc=x0anCIslp0hNIM:1000

            See http://processingjs.nihongoresources.com/bezierinfo/
        """
        nPoints = len(points)
        xPoints = np.array([p[0] for p in points])
        yPoints = np.array([p[1] for p in points])

        t = np.linspace(0.0, 1.0, nTimes)

        polynomial_array = np.array([self.bernstein_poly(i, nPoints - 1, t) for i in range(0, nPoints)])

        xvals = np.dot(xPoints, polynomial_array)
        yvals = np.dot(yPoints, polynomial_array)

        return xvals, yvals

    def getPoint(self,data):
        rdata = rdp(data, epsilon=1.5)
        nx, ny = self.bezier_curve(rdata)
        x = np.array(nx)
        y = np.array(ny)

        point = np.column_stack([x,y])
        point = point.reshape((100,2))

        return point

