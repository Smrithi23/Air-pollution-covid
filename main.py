from air_pollution_time_series import air_pollution_time_series
from correlation import Correlation
from random_forest import Random_Forest
from LSTM import LSTM_Model
from BiLSTM import BiLSTM_Model

cities = ['Bengaluru', 'Chennai', 'Delhi', 'Kolkata', 'Mumbai']

# Plot air pollution data as a time series data for each city
print('>> Air pollution time series for Bengaluru')
air_pollution_time_series('Bengaluru')
print('>> Air pollution time series for Chennai')
air_pollution_time_series('Chennai')
print('>> Air pollution time series for Delhi')
air_pollution_time_series('Delhi')
print('>> Air pollution time series for Kolkata')
air_pollution_time_series('Kolkata')
print('>> Air pollution time series for Mumbai')
air_pollution_time_series('Mumbai')

# Feature selection using correlation coefficient heatmap
print('>> Correlation heatmap for Bengaluru')
Correlation('Bengaluru')
print('>> Correlation heatmap for Chennai')
Correlation('Chennai')
print('>> Correlation heatmap for Delhi')
Correlation('Delhi')
print('>> Correlation heatmap for Kolkata')
Correlation('Kolkata')
print('>> Correlation heatmap for Mumbai')
Correlation('Mumbai')

# Feature selection using random forest classifier
print('>> Feature selection using random forest classifier for Bengaluru')
Random_Forest('Bengaluru')
print('>> Feature selection using random forest classifier for Chennai')
Random_Forest('Chennai')
print('>> Feature selection using random forest classifier for Delhi')
Random_Forest('Delhi')
print('>> Feature selection using random forest classifier for Kolkata')
Random_Forest('Kolkata')
print('>> Feature selection using random forest classifier for Mumbai')
Random_Forest('Mumbai')

# LSTM Model
print('>> LSTM model for Bengaluru')
LSTM_Model('Bengaluru')
print('>> LSTM model for Chennai')
LSTM_Model('Chennai')
print('>> LSTM model for Delhi')
LSTM_Model('Delhi')
print('>> LSTM model for Kolkata')
LSTM_Model('Kolkata')
print('>> LSTM model for Mumbai')
LSTM_Model('Mumbai')

# Bidirectional LSTM
print('>> Bidirectional LSTM model for Bengaluru')
BiLSTM_Model('Bengaluru')
print('>> Bidirectional LSTM model for Chennai')
BiLSTM_Model('Chennai')
print('>> Bidirectional LSTM model for Delhi')
BiLSTM_Model('Delhi')
print('>> Bidirectional LSTM model for Kolkata')
BiLSTM_Model('Kolkata')
print('>> Bidirectional LSTM model for Mumbai')
BiLSTM_Model('Mumbai')
print('>> Completed processing')