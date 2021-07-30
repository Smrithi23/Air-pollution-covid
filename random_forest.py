import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def Random_Forest(city):
    features = ['PM2.5', 'NO', 'NO2', 'NOx', 'SO2', 'CO']

    dataset = pd.read_csv('./data/' + city.lower() + '.csv')
    dataset.drop(['Date', 'Recovered', 'Deceased'], axis=1, inplace=True)

    values = dataset.values
    X = values[:, 2:]
    y = values[:, 1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

    # Create a random forest classifier
    clf = RandomForestClassifier(n_estimators=1000, random_state=0, n_jobs=-1)

    # Train the classifier
    clf.fit(X_train, y_train)

    importance = []
    # Print the name and gini importance of each feature
    for feature in zip(features, clf.feature_importances_):
        print(feature[0], ": ", feature[1])
        importance.append(feature[1].round(4))
    
    # Figure Size
    fig, ax = plt.subplots()
    
    # Horizontal Bar Plot
    ax.barh(features, importance)
    
    # Remove axes splines
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    
    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    
    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)
    
    # Add x, y gridlines
    ax.grid(b = True, color ='grey',linestyle ='-.', linewidth = 0.4, alpha = 0.2)
    
    # Show top values
    ax.invert_yaxis()

    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width(), i.get_y()+0.5,
                str(round((i.get_width()), 4)),
                fontsize = 10, fontweight ='bold',
                color ='grey')
    
    # Add Plot Title
    ax.set_title(city, loc ='left')
    
    # Show Plot
    plt.savefig('./Random Forest/' + city + ' - Feature Relative Importance using Random Forest.png', dpi=300, bbox_inches='tight')
    plt.show()