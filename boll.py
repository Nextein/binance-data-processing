def bollinger_bands(price, window_size, num_of_std):
    rolling_mean = price.rolling(window=window_size).mean()
    rolling_std = price.rolling(window=window_size).std()
    upper_band = rolling_mean + (rolling_std * num_of_std)
    lower_band = rolling_mean - (rolling_std * num_of_std)

    return rolling_mean, upper_band, lower_band

def main():
    price_series = get_data(ticker, dates)  # it is a Pandas series...

    rolling_avg_price, upper_band, lower_band = bollinger_bands(price_series, 20, 2)

    do_other_processing(rolling_avg_price, upper_band, lower_band)