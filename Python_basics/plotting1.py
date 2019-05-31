import numpy as np
import matplotlib.pylab as plt

x=np.linspace(0,10,1000)
y=np.exp(-x/3.)*np.sin(2.*x)


fig=plt.figure(figsize=(15,7))
plt.subplots_adjust(left=.1, bottom=.1, right=.95, top=.95)
ax=fig.add_subplot(111)
ax.plot(x,y,'.',label='Data')
ax.set_title("Invented Data")
ax.set_xlabel("This is $x$")
ax.set_ylabel("This is $y$")
plt.savefig("Test1.pdf")
plt.show()
