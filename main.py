import matplotlib.pyplot as plt
import numpy as np


# Outer lip (left)
y = np.linspace(-17, 17, 1000)
x1 = (y**2 + 300)/90

# Inner lip layer-1 (left)
x2 = (y**2 + 650)/75

# Inner lip layer-2 (left)
x3 = (y**2 + 800)/75

# Inner lip layer-2 (right)
x4 = (y**2 - 1400)/-75

# Inner lip layer-1 (right)
x5 = (y**2 - 1550)/-75

# Outer lip (right)
x6 = (y**2 - 2300)/-90

# Clitoris
x_clit = np.linspace(13, 15.536, 10**4)
y_clit_1 = 15 + ((117.36*x_clit - 4*x_clit**2 - 857.84)**(1/2))/2
y_clit_2 = 15 - ((117.36*x_clit - 4*x_clit**2 - 857.84)**(1/2))/2

# Urethra
x_urethra = np.linspace(14.495, 14.835, 10**3)
y_urethra_1 = 9 + ((117.36*x_urethra - 4*x_urethra**2 - 860.71)**(1/2))/2
y_urethra_2 = 9 - ((117.36*x_urethra - 4*x_urethra**2 - 860.71)**(1/2))/2

# Vagina
x_vag = np.linspace(12.089, 17.247, 10**5)
y_vag = -((x_vag - 14.67)**2 + 14)/2

fig = plt.figure(figsize=(6.2, 7))

# Plotting the lips
plt.plot(x1, y)
plt.plot(x2, y)
plt.plot(x3, y)
plt.plot(x4, y)
plt.plot(x5, y)
plt.plot(x6, y)

# Plotting the clitoris
plt.plot(x_clit, y_clit_1)
plt.plot(x_clit, y_clit_2)

# Plotting the pee-hole
plt.plot(x_urethra, y_urethra_1)
plt.plot(x_urethra, y_urethra_2)

# Plotting the holy grail
plt.plot(x_vag, y_vag)


plt.show()
