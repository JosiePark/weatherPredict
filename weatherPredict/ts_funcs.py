from statsmodels.tsa.stattools import adfuller

def stationary_test(df, col):
    result = adfuller(df[col])
    print('ADF Statistic: {}'.format(result[0]))
    print('p-value: {}'.format(result[1]))
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t{}: {}'.format(key, value))

    return