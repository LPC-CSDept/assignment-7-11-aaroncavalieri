import numpy as np
import matplotlib.pyplot as plt

Math = [100, 90]
English = [90, 80]
Physics = [80, 80]
Computer = [80, 90]
x = np.arange(2) 
width = 0.2
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']

fig, ax = plt.subplots()
bar1 = ax.bar(x-width*1.5, Math, width)
bar2 = ax.bar(x-width*0.5, English, width)
bar3 = ax.bar(x+width*1.5, Physics, width)
bar4 = ax.bar(x+width*0.5, Computer, width)

ax.set_title("Grouped graph for scores")
ax.bar_label(bar1, padding=3)
ax.bar_label(bar2, padding=3)
ax.bar_label(bar3, padding=3)
ax.bar_label(bar4, padding=3)
ax.legend(labels)
ax.set_xticks(x, names)


fig.savefig('A11.png')
