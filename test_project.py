from project import convert_series_to_date, _get_compatible_formats, _convert_to_datetime
import datetime
import pandas as pd

def main():
    test_convert_series_to_date()
    

def test_convert_series_to_date():
    array = ['20/06/02', '29/08/04', '04/08/09', '11/10/33', '13/04/34', '08/11/47', '02/02/65', '11/03/83', '08/05/98']
    date_series = pd.Series(array)
    standardized_dates = convert_series_to_date(date_series, format=None)
    assert list(standardized_dates) == [
        datetime.date(2002, 6, 20),
        datetime.date(2004, 8, 29),
        datetime.date(2009, 8, 4),
        datetime.date(2033, 10, 11),
        datetime.date(2034, 4, 13),
        datetime.date(2047, 11, 8),
        datetime.date(2065, 2, 2),
        datetime.date(1983, 3, 11),
        datetime.date(1998, 5, 8)]

    # multiple compatible date formats (can't decide without specification)
    array = ['04/03/00', '05/10/00', '04/01/01', '05/10/01', '06/04/02', '11/05/03', '01/01/06', '09/10/09', '05/10/11']
    date_series = pd.Series(array)
    standardized_dates = convert_series_to_date(date_series, format=None)
    assert list(standardized_dates) == [
        '04/03/00', 
        '05/10/00', 
        '04/01/01', 
        '05/10/01', 
        '06/04/02', 
        '11/05/03', 
        '01/01/06', 
        '09/10/09', 
        '05/10/11']
    
    # multiple compatible date formats (specified in function call)
    array = ['04/03/00', '05/10/00', '04/01/01', '05/10/01', '06/04/02', '11/05/03', '01/01/06', '09/10/09', '05/10/11']
    date_series = pd.Series(array)
    standardized_dates = convert_series_to_date(date_series, format='dd/mm/yy')
    assert list(standardized_dates) == [datetime.date(2000, 3, 4),
        datetime.date(2000, 10, 5),
        datetime.date(2001, 1, 4),
        datetime.date(2001, 10, 5),
        datetime.date(2002, 4, 6),
        datetime.date(2003, 5, 11),
        datetime.date(2006, 1, 1),
        datetime.date(2009, 10, 9),
        datetime.date(2011, 10, 5)]
    
    # None value in array
    array = [None, 
        '05/10/00', 
        '04/01/01', 
        '05/10/01', 
        '06/04/02', 
        None, 
        '01/01/06', 
        '09/10/09', 
        None]
    date_series = pd.Series(array)
    standardized_dates = convert_series_to_date(date_series, format=None)
    assert list(standardized_dates) == [None, 
        '05/10/00', 
        '04/01/01', 
        '05/10/01', 
        '06/04/02', 
        None, 
        '01/01/06', 
        '09/10/09', 
        None]

    
    # None value in array
    array = [None, 
        '05/10/00', 
        '04/01/01', 
        '05/10/01', 
        '06/04/02', 
        None, 
        '01/01/06', 
        '09/10/09', 
        None]
    date_series = pd.Series(array)
    standardized_dates = convert_series_to_date(date_series, format=None)
    assert list(standardized_dates) == [None, 
        '05/10/00', 
        '04/01/01', 
        '05/10/01', 
        '06/04/02', 
        None, 
        '01/01/06', 
        '09/10/09', 
        None]


def test_get_compatible_formats():
    array = ['20/06/02', '29/08/04', '04/08/09', '11/10/33', '13/04/34', '08/11/47', '02/02/65', '11/03/83', '08/05/98']
    date_series = pd.Series(array)
    status, compatible_formats = _get_compatible_formats(date_series)
    assert status == True
    assert compatible_formats == 'dd/mm/yy'
                            
    array = ['04/03/00', '05/10/00', '04/01/01', '05/10/01', '06/04/02', '11/05/03', '01/01/06', '09/10/09', '05/10/11']
    date_series = pd.Series(array)
    status, compatible_formats = _get_compatible_formats(date_series)
    assert status == False
    assert compatible_formats == ['dd/mm/yy', 'mm/dd/yy']


def test_convert_to_datetime():
    array = ['20/06/02', '29/08/04', '04/08/09', '11/10/33', '13/04/34', '08/11/47', '02/02/65', '11/03/83', '08/05/98']
    date_series = pd.Series(array)
    
    array = ['04/03/00', '05/10/00', '04/01/01', '05/10/01', '06/04/02', '11/05/03', '01/01/06', '09/10/09', '05/10/11']
    date_series = pd.Series(array)    
    converted = _convert_to_datetime(date_series, pandas_format='%d/%m/%y')
    assert list(converted) == [
        datetime.date(2000, 3, 4),
        datetime.date(2000, 10, 5),
        datetime.date(2001, 1, 4),
        datetime.date(2001, 10, 5),
        datetime.date(2002, 4, 6),
        datetime.date(2003, 5, 11),
        datetime.date(2006, 1, 1),
        datetime.date(2009, 10, 9),
        datetime.date(2011, 10, 5)]


if __name__ == '__main__':
    main()
