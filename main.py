import matplotlib.pyplot as plt
import pandas



filename = "Fruit Prices 2020.csv"
Fruit_df = pandas.read_csv(filename)
avg_weight_by_fruit_type = Fruit_df.groupby("Form")["RetailPrice"].mean()
avg_weight_by_fruit_type.plot(kind="bar", x="form", y = "price in dollars", rot=45)

plt.show()
