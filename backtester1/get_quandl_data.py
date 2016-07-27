# download_quandl_data.py

import quandl

def get_data(quandl_code, sampling_frequency, start_date=0, end_date=0):
    """Download data from quandl and return the resulting DataFrame.

    Arguments:
    quandl_code        --
    start_date         --
    end_date           --
    sampling_frequency --
    """
    if start_date == 0 and end_date != 0:
        data = quandl.get(quandl_code, end_date=end_date,
                          collapse=sampling_frequency)
    elif start_date != 0 and end_date == 0:
        data = quandl.get(quandl_code, start_date=start_date,
                          collapse=sampling_frequency)
    elif start_date == 0 and end_date == 0:
        data = quandl.get(quandl_code, collapse=sampling_frequency)
    else:   
        data = quandl.get(quandl_code, start_date=start_date, end_date=end_date,
                      collapse=sampling_frequency)
    return data

def save_data(data, file_name):
    """Save DataFrame containing data from quandl as csv-file with the
    specified name.

    Arguments:
    data      --
    file_name --
    """
    pass


my_data = get_data("GOOG/NYSE_SPY", "daily", "2001-12-31", "2005-12-31")

print(my_data.tail())

    
