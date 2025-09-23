# box plot shows quartiles and extremes
rolls = np.random.randint(1, 7, 1000) + np.random.randint(1, 7, 1000)
fig1, ax1 = plt.subplots()
ax1.set_title("Rolls")
ax1.boxplot(rolls)
plt.show()

# violinplot adds histogram, doesn't show quantiles, just extremes
fig1, ax1 = plt.subplots()
ax1.set_title("Rolls")
ax1.violinplot(rolls)
plt.show()

# basic line graph
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(101)
y=x**2
plt.title("A Parabola")
plt.plot(x,y)
plt.show()

# double line graph with legend
plt.plot(np.arange(10), color="blue", label="number of toppings")
plt.plot(np.arange(10), np.arange(10) ** 2, color="orange", label="price of pie")
plt.legend(loc="upper left")
plt.show()

# basic scatter plot
x = np.random.randint(1, 20, (10, ))
y = np.random.randint(10, 35, (10, ))
print(x)
print(y)
plt.scatter(x, y)
plt.show()

# to add labels, use annotate
labels = (chr(i) for i in range(65, 75))
plt.scatter(x, y)
for x1, y1, label in zip(x, y, labels): # zip generates a tuple iterator
    plt.annotate(label, xy=(x1+0.3, y1-0.2)) # slight offset so that the labels aren't right on the point
plt.show()

# Setting up a bar graph

attitudes = ("Great", "OK", "Poor") # bar categories
num_votes = [5, 3, 12] # counts for each bar
# could also store the categories and counts in a dictionary
x = np.arange(len(attitudes)) # the x values (based on number of labels)
plt.bar(x, num_votes, align='center', color='#aaddff') # create the bar chart; can use any RGB color in Hex
plt.xticks(x, attitudes) # set up the ticks for the categories
plt.ylim(0, 14) # set up the y axis limits
plt.ylabel('Votes') # x and y axis labels
plt.xlabel('Attitude')
plt.title('What do you think of this graph?') # overall title
plt.show()

# basic pie chart
edible_pies = ['pecan', 'chocolate', 'apple', 'blueberry']
sizes = [10.2, 7.3, 4, 3]
plt.pie(sizes, labels=edible_pies, autopct=lambda x:f'{round(x,2)}%')
plt.axis('equal')
plt.show()

# basic subplot use
plt.subplot(2, 2, 1) # top left
plt.plot(np.arange(10), 'k:') # k stands for black

plt.subplot(2, 2, 2) # top right
plt.pie((1, 2, 3))
plt.axis('equal')

plt.subplot(2, 2, 3) # bottom left
plt.bar(np.arange(4), (5, 7, 1, 2))

plt.subplot(2, 2, 4) # bottom right
plt.plot(np.arange(10) ** 2, color="#ffaa00")
plt.show()


