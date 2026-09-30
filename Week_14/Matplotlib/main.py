# import matplotlib.pyplot as plt

# ages = [21, 24, 35, 34, 27, 56, 31, 45, 35, 40, 42]

# plt.figure(figsize=(6, 4))

# plt.hist(ages, bins=5)

# plt.title("Customer Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("No. of Customers")

# plt.show()

# =================================
# import matplotlib.pyplot as plt
# import seaborn as sns

# ages = [21, 24, 35, 34, 27, 56, 31, 45, 35, 40, 42]

# plt.figure(figsize=(6, 4))

# sns.histplot(ages, bins=5, kde=True)

# plt.title("Customer Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("No. of Customers")

# plt.show()

# ===============BOX PLOT==========================
# import matplotlib.pyplot  as plt

# sal =[25000, 26000, 28000,35000 , 40000, 45000, 60000, 32000]
# plt.boxplot(sal)
# plt.show()

# ==================================================
#frequency plot
# import matplotlib.pyplot as plt
# ages =[21,24,35,34,27,56,31,45,35,40,42,50,34,23,35,43,21]

# plt.figure(figsize=(6,4)) #(width , height)

# plt.hist(ages,bins = 4,edgecolor='green') #this change based on our plot

# plt.title('customers Age distribution')
# plt.xlabel('Age')
# plt.ylabel('No of customers')

# plt.show()

# =========================================
# import matplotlib.pyplot as plt
# import pandas as pd
# country =['ind','usa','china','ind','russia','usa','ind','ind','ind']
# s = pd.Series(country)
# result = s.value_counts()
# print(result.index)
# print(result.values)
# print(s)
# plt.barh(result.index, result.values)
# plt.show()

# ==========PIE CHART============
# import matplotlib.pyplot as plt

# channel =['insta','fb','yt','google','whatsapp']
# leads =[40 , 20 , 10, 30 , 10]

# plt.pie(leads, labels=channel, autopct="%1.2f%%", explode=(0,0.1,0,0,0.1), startangle=45)
# plt.show()

# ================Line Chart==================
# import matplotlib.pyplot as plt
# ages =[21,24,35,34,27,56,31,45,35,40,42,50,34,23,35,43,21]

# plt.plot(ages, color = 'b', marker='*', markeredgecolor='red', linewidth=0.7)
# plt.show()

# =================================================
# import matplotlib.pyplot as plt
# import seaborn as sns
# exp = [1,2,3,4,5,6,7,8,9]
# sal =[20,30,120,50,60,70,80,90,100]

# # plt.scatter(exp,sal)
# # plt.plot(exp,sal,marker='*')
# # plt.show()
# sns.regplot(x = exp,y = sal)
# plt.show()

# ===================================================
# import matplotlib.pyplot as plt

# exp = [1,2,3,4,5,6,7,8,9]
# sal =[20,30,40,50,60,70,80,90,100]
# performance = [600,50,65,45,270,74,90,89,90]
# #plt.scatter(exp,sal)
# # plt.plot(exp,sal,marker='*')
# plt.scatter(exp,sal,s = performance )

# plt.show()

# ====================================================
# import matplotlib.pyplot as plt

# dept =['it','DS','fin'] * 2

# sal = [30,40,50] * 2


# plt.bar(dept , sal )
# plt.show()

# =========================================================
import matplotlib.pyplot as plt

#box plot with bivariate analysis:

data =[[45000,50000,35000,78000,64000,53000,27000],[45000,50000,35000,78000,64000,53000,27000],[45000,50000,35000,78000,64000,53000,27000]]


plt.boxplot(data)


plt.xticks([1,2,3],['Hr','IT','FIn'])


plt.xlabel('dept')
plt.ylabel('sal')
plt.show()
