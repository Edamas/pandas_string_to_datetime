import pandas as pd

def main():
    date_series = pd.Series(['04/03/00', '05/10/00', '04/01/01', '05/10/01', '06/04/02', '11/05/03', '01/01/06', '09/10/09', '05/10/11'])
    print('Input:')
    for date in date_series:
        print(date)
    print()
    print('Process:')
    standardized_dates = convert_series_to_date(date_series, format='dd/mm/yy')
    for d, dt in zip(date_series, standardized_dates):
        print(type(d), d, '\t ---->\t', dt, type(dt))
    print()
    print('Output:')
    print(standardized_dates)
    
def convert_series_to_date(date_series, format=None):
    """Function to convert the date format in a Pandas Series.
    
    Parameters:
    - date_series (pd.Series): Pandas Series containing dates.
    
    Returns:
    - pd.Series: Pandas Series with datetime dates
    - pd.Series.name = 'Standardized_dates'
    
    Prerequisites:
    All dates in the series must:
    - be compatible with pandas dates (supported formats)
    - respect the calendar dates
    - be consistent in format used for all dates, not change
    - if multiple formats are compatible (day/month, month/day), the format must be specified 
    
    Errors:
    - If an error is found, the same pandas Series is returned
    
    Supported Formats:
    - 'dd-mm-yyyy','dd/mm/yyyy','mm-dd-yyyy','mm/dd/yyyy','yyyy-mm-dd','yyyy/mm/dd','dd-mm-yy','dd/mm/yy','mm-dd-yy','mm/dd/yy'
    
    Examples:
    date_series = pd.Series(['18/08/1927', '30/06/1931', '10/07/2034', '03/10/2040', '10/02/2048'])
    - convert_series_to_date(date_series, format='dd/mm/yyyy')
	>> pd.Series([datetime.date(1946, 4, 29), datetime.date(1955, 4, 21), datetime.date(1978, 6, 18), datetime.date(1984, 4, 28), datetime.date(2022, 6, 30)])
    """
    global supported_formats
    supported_formats = {'dd-mm-yyyy':'%d-%m-%Y', 'dd/mm/yyyy':'%d/%m/%Y', 'mm-dd-yyyy':'%m-%d-%Y', 'mm/dd/yyyy':'%m/%d/%Y',
        'yyyy-mm-dd':'%Y-%m-%d', 'yyyy/mm/dd':'%Y/%m/%d', 'dd-mm-yy':'%d-%m-%y', 'dd/mm/yy':'%d/%m/%y', 'mm-dd-yy':'%m-%d-%y',
        'mm/dd/yy':'%m/%d/%y'}
    if None not in date_series:
        if format is not None:
            return _convert_to_datetime(date_series, supported_formats[format])
        else:
            status, compatible_formats = _get_compatible_formats(date_series)
            if status:
                return _convert_to_datetime(date_series, supported_formats[compatible_formats])
            else:
                if len(compatible_formats) == 0:
                    '''No compatible formats detected in date_series.
                    Check date_series for dates out of the calendar (Eg.: 30/02/2000 or 31/04/2000, 30/30/30).
                    Nothing changed'''
                    return date_series
                else:
                    '''Multiple compatible formats detected in date_series.
                    Specify the correct datetime format from those compatible formats
                    convert_series_to_date(date_series, format=compatible_format)
                    Nothing changed'''
                    return date_series
    else:
        '''None found in date_series. Please use valid dates. Nothing changed'''
        return date_series




def _get_compatible_formats(date_series):
    '''Detect compatible_formats all compatible datetime formats and returns a list.'''
    
    compatible_formats = []
    for readable_format, pandas_format in supported_formats.items():
        if pd.to_datetime(date_series, format=pandas_format, errors='coerce').notnull().all():
            compatible_formats.append(readable_format)
    if len(compatible_formats) == 1:
        status = True
        compatible_format = compatible_formats[0]
        return status, compatible_format
    else:
        status = False
        return status, compatible_formats



def _convert_to_datetime(date_series, pandas_format):
    standardized_dates = pd.to_datetime(date_series, format=pandas_format, errors='coerce').dt.date
    standardized_dates.name = 'Standardized_dates'
    return standardized_dates



if __name__ == '__main__':
    main()