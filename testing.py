import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)

plt.plot(x, np.sin(x))
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin(x)')
plt.show()

