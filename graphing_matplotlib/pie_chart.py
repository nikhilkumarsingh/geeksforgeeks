import matplotlib.pyplot as plt
 
# defining labels
activities = ['eat', 'sleep', 'work', 'play']
 
# portion covered by each label
slices = [3, 7, 8, 6]
 
# color for each label
colors = ['r', 'm', 'g', 'b']
 
# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors, 
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
        radius = 1.2, autopct = '%1.1f%%')
 
# plotting legend
plt.legend()
 
# showing the plot
plt.show()
