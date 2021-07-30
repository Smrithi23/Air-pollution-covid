import numpy as np
from matplotlib import pyplot
from pandas import read_csv, DataFrame, concat
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.metrics import r2_score
 
# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
    # drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg

def LSTM_Model(city):

    # load dataset
    dataset = read_csv('./data/' + city.lower() + '.csv', header=0, index_col=0)
    dataset.drop(['Date', 'Recovered', 'Deceased'], axis=1, inplace=True)
    values = dataset.values

    # ensure all data is float
    values = values.astype('float32')

    # normalize features
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(values)

    # frame as supervised learning
    reframed = series_to_supervised(scaled, 1, 1)

    # drop columns we don't want to predict
    reframed.drop(reframed.columns[[8, 9,10,11,12,13]], axis=1, inplace=True)
    
    # split into train and test sets
    values = reframed.values
    n_train_hours = 237
    train = values[:n_train_hours, :]
    test = values[n_train_hours:, :]

    # split into input and outputs
    train_X, train_y = train[:, :-1], train[:, -1]
    test_X, test_y = test[:, :-1], test[:, -1]

    # reshape input to be 3D [samples, timesteps, features]
    train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
    test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
    
    # design network
    model = Sequential()
    model.add(LSTM(4, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam', metrics=['mean_absolute_error'])

    # fit network
    model.fit(train_X, train_y, epochs=100, batch_size=1, verbose=2)
    model.summary()

    # make a prediction
    yhat = model.predict(test_X)
    training_values = model.predict(train_X)

    trainScore = r2_score(train_y, training_values)
    testScore = r2_score(test_y, yhat)
    print("Train Score: ", trainScore.round(3))
    print("Test Score: ", testScore.round(3))

    # rescale values
    yhat = yhat * dataset.values[-1, 0]
    training_values = training_values * dataset.values[-1, 0]

    # reshape
    yhat = yhat.reshape([128])
    training_values = training_values.reshape([237])

    # predicted plot
    predicted_plot = values[:, -1] * dataset.values[-1, 0]

    # training plot
    training_plot = np.zeros(len(dataset))
    training_plot[:] = np.nan
    training_plot[:237] = training_values

    # testing plot
    testing_plot = np.zeros(len(dataset)-1)
    testing_plot[:] = np.nan
    testing_plot[237:len(dataset)-1] = yhat

    # plot using matplotlib
    pyplot.plot(predicted_plot, label='predicted plot')
    pyplot.plot(training_plot, label='training plot')
    pyplot.plot(testing_plot, label='testing plot')
    pyplot.title(city)
    pyplot.legend()
    pyplot.savefig('./LSTM/' + city + ' LSTM.png', dpi=300, bbox_inches='tight')
    pyplot.show()