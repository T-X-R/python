import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
def rainbow(a,b,c,d):
    x, y = np.mgrid[a : b : 20j, c : d : 20j]
    z = 50 * np.sin(x + y)
    ax = plt.subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap=plt.cm.rainbow)
    plt.axis('off')
    plt.show()



rainbow(-1,1,-1,1)




# rainbow(-2,2,-2,2)
