from statistics import mean
import numpy as np
import matplotlib.pylab as plt

from matplotlib import style

style.use("fivethirtyeight")
#dtype important later
xs = np.array([1,2,3,4,5,6],dtype=np.float64)
ys = np.array([5,4,6,5,6,7],dtype=np.float64)

plt.scatter(xs,ys)
plt.show()


def best_fit_slope(xs,ys):
    m = (mean(xs)*mean(ys)-mean(xs*ys))/(mean(xs)**2.-mean(xs**2.))
    return m

m=best_fit_slope(xs,ys)
print(m)

########################PEMDAS
plt.scatter(xs,ys)
plt.plot(xs,m*xs,color='C1')
plt.show()


b=mean(ys)-m*mean(xs)

plt.scatter(xs,ys)
plt.plot(xs,m*xs+b,color='C1')
plt.show()

def best_fit_slope_and_intercept(xs,ys):
        m = (mean(xs)*mean(ys)-mean(xs*ys))/(mean(xs)**2.-mean(xs**2.))
        b=mean(ys)-m*mean(xs)
        return m,b


m,b=best_fit_slope_and_intercept(xs,ys)

plt.scatter(xs,ys)
plt.plot(xs,m*xs+b,color='C1')
plt.show()

regression_line=[(m*x)+b for x in xs]

print(m,b)



predicted_x=8

predicted_y=m*predicted_x+b

plt.scatter(xs,ys)
plt.plot(xs,m*xs+b,color='C1')
plt.scatter(predicted_x,predicted_y, color='C2')
plt.show()
