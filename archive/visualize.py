import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

plt.style.use('ggplot')
plt.rcParams.update({'font.size':15})

x = np.random.normal(size = 1000)

plt.hist(x)
plt.show()