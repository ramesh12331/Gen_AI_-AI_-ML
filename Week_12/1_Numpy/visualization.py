import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 11. HISTOGRAM
# ============================================================

age = np.array([
    23, 18, 34, 25, 43,
    27, 34, 32, 19,
    90, 89, 78
])

sns.histplot(age, kde=True)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()


# ============================================================
# 12. BOX PLOT
# ============================================================

age = np.array([
    23, 18, 34, 25, 43,
    27, 34, 32, 19,
    190, 800, 50
])

sns.boxplot(x=age)

plt.title("Age Box Plot")
plt.xlabel("Age")

plt.show()