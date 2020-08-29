import seaborn as sns
import matplotlib as plt
import pandas as pd

tips = sns.load_dataset("tips")
sns.set(style = "whitegrid")

# dtypes: category(4), float64(2), int64(1) // Non-Null count : 0
tips.info()

# tipsCount = sns.countplot(x="day", data = tips)

# totalAndTips = sns.regplot(x="total_bill", y="tip", data = tips)

# summarys = sns.boxplot(x="day", y="total_bill", data = tips)

# oawnd = sns.barplot(x="day", y='tip', hue = "time" ,data = tips)

# tips_d = tips[["total_bill", "tip", "sex", "size"]]
# tips_d.info()

# tipsss = sns.pairplot(data = tips_d, hue = "sex")

plt.pyplot.show()