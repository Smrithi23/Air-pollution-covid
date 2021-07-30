import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def Correlation(city):
    dataframe = pd.read_csv('./data/' + city.lower() + '.csv')
    dataframe.drop(['Date', 'Confirmed', 'Recovered', 'Deceased'], axis=1, inplace=True)
    dataframe.drop([dataframe.columns[0]], axis=1, inplace=True)

    # Store heatmap object in a variable to easily access it when you want to include more features (such as title).
    # Set the range of values to be displayed on the colormap from -1 to 1, and set the annotation to True to display the correlation values on the heatmap.
    heatmap = sns.heatmap(dataframe.corr(), vmin=0, vmax=1, annot=True, cmap='YlGnBu')
    # Give a title to the heatmap. Pad defines the distance of the title from the top of the heatmap.
    heatmap.set_title(city + ' Correlation Heatmap', fontdict={'fontsize':12}, pad=12);

    # save heatmap as .png file
    # dpi - sets the resolution of the saved image in dots/inches
    # bbox_inches - when set to 'tight' - does not allow the labels to be cropped
    plt.savefig('./heatmap/' + city + ' Heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()