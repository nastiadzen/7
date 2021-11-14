import numpy as np
import matplotlib.pyplot as plt
y=lambda x:np.sin(x)
z=plt.subplots()
x=np.linspace(0, 5)
plt.plot(x, y(x**(1/2)*np.sin(10*x)), color='c')
plt.show()