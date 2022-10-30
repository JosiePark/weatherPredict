import matplotlib.pyplot as plt
import pandas as pd

def ARIMA_predict_plot(model_fit, train_df, test_df, fitted_col, model_type = 'ARIMA'):

    if model_type == 'ARIMA':
        predicted = model_fit.forecast(len(test_df))  # 95% conf
        conf = model_fit.get_forecast(len(test_df)).conf_int(0.05)
    elif model_type == 'auto_arima':
        predicted, conf = model_fit.predict(len(test_df),return_conf_int=True,alpha=0.05)  # 95% conf

    # Make as pandas series
    fc_series = pd.Series(predicted, index=test_df.index)
    lower_series = pd.Series(conf[:, 0], index=test_df.index)
    upper_series = pd.Series(conf[:, 1], index=test_df.index)

    # Plot
    plt.figure(figsize=(12,5), dpi=100)
    plt.plot(train_df[fitted_col], label='training')
    plt.plot(test_df[fitted_col], label='actual')
    plt.plot(fc_series, label='forecast')
    plt.fill_between(lower_series.index, lower_series, upper_series, 
                    color='k', alpha=.15)
    plt.title('Forecast vs Actuals')
    plt.legend(loc='upper left', fontsize=8)
    plt.show()

    return