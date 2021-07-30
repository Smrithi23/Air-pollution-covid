from pandas import read_csv
from matplotlib import pyplot

def air_pollution_time_series(city):
    # load dataset
    dataset = read_csv('./data/' + city.lower() + '.csv', header=0, index_col=0)
    dataset.drop(['Date', 'Confirmed', 'Recovered', 'Deceased'], axis=1, inplace=True)
    values = dataset.values

    units = ['ug/m3', 'ug/m3', 'ug/m3', 'ppb', 'ug/m3', 'mg/m3']
    # specify columns to plot
    groups = [0, 1, 2, 3, 4, 5]
    i = 1
    # plot each column
    pyplot.rcParams["figure.figsize"] = (6.4, 4.8)
    for group in groups:
        pyplot.subplot(len(groups), 1, i)
        pyplot.plot(values[:, group])
        pyplot.title(dataset.columns[group] + units[group], y=0.5, loc='right', fontsize=7)
        i += 1
    pyplot.suptitle(city)
    pyplot.savefig('./air pollution time series/' + city + ' Air Pollution Time Series.png', dpi=300, bbox_inches='tight')
    pyplot.show()