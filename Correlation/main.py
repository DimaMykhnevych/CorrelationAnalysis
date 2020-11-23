import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
sns.set()
data = pd.read_csv("Fish.csv")
data.head()


def show_plot():
    # logged_hum = np.log(data["Humidity"]);
    # plt.scatter(logged_hum, data["Temperature"])
    plt.scatter(data["Weight"], data["Length1"])
    plt.xlabel("Length", size=14)
    plt.ylabel("Weight", size=14)
    plt.show()


def calculate_correlation():
    data["xy"] = data["Weight"] * data["Length1"]
    data["x2"] = data["Weight"] ** 2
    data["y2"] = data["Length1"] ** 2
    sum_x = sum(data["Weight"])
    sum_y = sum(data["Length1"])
    sum_xy = sum(data["xy"])
    sum_xx = sum(data["x2"])
    sum_yy = sum(data["y2"])
    n = data["Length1"].count()
    r = (n * sum_xy - sum_x * sum_y) / np.sqrt(((n * sum_xx - sum_x ** 2) * (n * sum_yy - sum_y ** 2)))
    return r


def calculate_t():
    r = calculate_correlation()
    df = data["Length1"].count() * 2 - 2
    print("Степени свободы: ", df)
    t = (r * (df ** 0.5))//(1 - r**2)
    return t


def main():
    corel = calculate_correlation()
    print("Correlation coefficient: ", corel)
    t = calculate_t()
    print("t: ", t)
    print(t, ">1.968. Нулевую теорию отбрасываем")
    show_plot()


if __name__ == "__main__":
    main()
