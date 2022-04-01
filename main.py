import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('D:\dataset_lab04.csv')

#1
print('Number of rows:',len(df))
print('Number of columns:',len(df.columns))

#2
print('Description of time',df['Time'].describe())
print('Description of Amount',df['Amount'].describe())

#3
print('mean of Time:',df['Time'].mean())
print('mean of V1:',df['V1'].mean())

print('median of V2:',df['V2'].median())
print('median of V3:',df['V3'].median())

print('Standard deviation of V4:',df['V4'].std())
print('Standard deviation of V5:',df['V5'].std())

print('Variance of V6:',df['V6'].var())
print('Variance of V7:',df['V7'].var())


#4

plt.title('Amount and Time')
df.boxplot(column=['Amount','Time'])

print("Amount Information:\n")
print('Q1: ',  df[['Amount']].quantile(0.25))
print('Median: ',  df[['Amount']].median())
print('Q3: ',  df[['Amount']].quantile(0.75))
print("IQR = ",  df[['Amount']].quantile(0.75) - df[['Amount']].quantile(0.25))
print('Average: ',  df[['Amount']].mean())
print('Max: ',  df[['Amount']].max())
print('Min: ',  df['Amount'].min())


print("\nTime Information:\n")
print('Q1: ', df[['Time']].quantile(0.25))
print('Median: ', df[['Time']].median())
print('Q3: ', df[['Time']].quantile(0.75))
print("IQR = ", df[['Time']].quantile(0.75) - df[['Time']].quantile(0.25))
print('Average: ', df[['Time']].mean())
print('Min: ', df[['Time']].min())
print('Max: ', df[['Time']].max())

print("Comment: \n")
print("There are  extreme values in 'Amount' that we can see in the graph,so there is Outliers")
print("But there is no outliers in 'Time'")

#5
df[['Time']].hist(column=['Time'], bins=100)

df[['Amount']].hist(column=['Amount'], bins=100)
print("Time\n")
print("Skewness of Time: ", df.Time.skew())
print("\nComment: Here skewness of Time is between -0.5 to +0.5. So it is fairly symmetrical\n")
print("Kurtosis of Time: ", df[['Time']].kurt())
print("\nComment: As the kurtosis < 3. So it is platykurtic\n")

print("Amount\n")
print("Skewness of Amount: ", df.Amount.skew())
print("\nComment: Here we can see skewness of Amount is greater than 1. So it is highly skewed\n")
print("Kurtosis of Amount: ", df['Amount'].kurt())
print("\nComment: As the kurtosis > 3. So it is leptokurtic\n")

#6
cls_val_0 = df.loc[df['Class'] == 0]
cls_val_1 = df.loc[df['Class'] == 1]

a = (cls_val_0.size * 100) / df.size
b = (cls_val_1.size * 100) / df.size

print("Percentage(%) of 0 = ","%.2f" %a)
print("Percentage(%) of 1 = ","%.2f" % b)

#7
df.hist(by=df['Class'], bins=100)

#8
x = [1, 2]
y = [a, b]
tick_label = ["0%", "1%"]
plt.bar(x, y, tick_label=tick_label, width=0.5, color=['yellow', 'red'])
plt.xlabel("Elements")
plt.ylabel("Frequency of %")

#9
df.hist(column=['Amount'], bins=100)
df.hist(column=['V12'], bins=100)
df.hist(column=['V11'], bins=100)
df.hist(column=['V9'], bins=100)


print("Positive Skew = ", df[['Amount']].skew())
print("Negative Skew = ", df[['V12']].skew())
print("Platykurtic = ", df[['V11']].kurt())
print("Leptokurtic = ", df[['V9']].kurt())


#10
x = df.min().min()
for i in df.columns:
    for j in df.columns:
        if i != j:
            correlation = df[i].corr(df[j])
            if (correlation > x):
                x1 = i
                x2 = j
                x = correlation
print("The Highest Positive Correlation = ","%.5f"%x)
print("It is between ", x1, "and", x2)


#11
df.plot.scatter(x='V7', y='Amount')

#12
n= df.max().max()
for i in df.columns:
    for j in df.columns:
        if i != j:
            correlation = df[i].corr(df[j])
            if (correlation < n):
                n1 = i
                n2 = j
                n = correlation
print("The Highest Negative Correlation = ","%.5f"% n)
print("It's between ", n1, "and", n2)


#13
df.plot.scatter(x='V2', y='Amount')

#14
df.boxplot(column=['Amount'])

#15

cls_val_0 = df[['Amount', 'Class']].query('Class==0')['Amount']
cls_val_1 = df[['Amount', 'Class']].query('Class==1')['Amount']
columns = [cls_val_0, cls_val_1]
fig, ax = plt.subplots()
ax.boxplot(columns)
plt.show()
print("Comment: Yes I find a pattern by considering amount column.")
print("I see there is a negative correlation between them in the box plot.")

plt.show()
