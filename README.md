# Convert Pandas Series to Datetime.Date

#### Video Demo: [Insert Your Video URL Here]
#### Description

The "Convert Pandas Series to Datetime.Date" project provides a straightforward solution for converting a Pandas Series containing string representations of dates into the more versatile `datetime.date` format. This functionality is crucial in data science, economics, and statistics, where working with accurate and standardized date formats is essential.

**Key Features:**
- Converts various date formats to `datetime.date`.
- Handles multiple compatible formats or lets you specify the format.
- Detects and suggests compatible date formats.

**Use Cases:**
1. **Data Cleaning:** Ensure consistency in date formats for datasets, facilitating downstream analysis.
2. **Time Series Analysis:** Proper date formatting is critical for time-based insights and predictions.
3. **Data Integration:** Streamline data integration from diverse sources with different date representations.

**Why It Matters:**
Inaccurate or inconsistent date formats can lead to errors in analysis and misinterpretation of data. This project simplifies the process of standardizing dates, contributing to more reliable and meaningful data-driven insights.

Explore the demo and integrate this tool into your data processing pipeline for improved date handling and analysis!


## Features

- Converts a Pandas Series with string values to datetime.date.
- Useful for datasets and timeseries in data science, economics, and statistics.

## Supported Date Formats

- 'dd-mm-yyyy'
- 'dd/mm/yyyy'
- 'mm-dd-yyyy'
- 'mm/dd/yyyy'
- 'yyyy-mm-dd'
- 'yyyy/mm/dd'
- 'dd-mm-yy'
- 'dd/mm/yy'
- 'mm-dd-yy'
- 'mm/dd/yy'

## Examples

```python
# input
date_series = pd.Series(['04/03/00', '05/10/00', '04/01/01', '05/10/01', '06/04/02', '11/05/03', '01/01/06', '09/10/09', '05/10/11'])

# convert
convert_series_to_date(date_series, format='dd/mm/yy')
```

- Output:
```
pd.Series([datetime.date(2000, 3, 4),
 datetime.date(2000, 10, 5),
 datetime.date(2001, 1, 4),
 datetime.date(2001, 10, 5),
 datetime.date(2002, 4, 6),
 datetime.date(2003, 5, 11),
 datetime.date(2006, 1, 1),
 datetime.date(2009, 10, 9),
 datetime.date(2011, 10, 5)])
```
or
```
0    2000-03-04
1    2000-10-05
2    2001-01-04
3    2001-10-05
4    2002-04-06
5    2003-05-11
6    2006-01-01
7    2009-10-09
8    2011-10-05
Name: Standardized_dates, dtype: object
```

## How to Use

1. **Clone the repository to your local machine:**

    ```bash
    git clone https://github.com/Edamas/pandas_string_to_datetime.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your-repository
    ```

3. **Run the main script:**

    ```bash
    python project.py
    ```

4. **Enjoy the standardized dates output!**


## Author

- **Name:** Elysio Damasceno da Silva Neto
- **Date:** 17th december, 2023
- **City:** São Paulo
- **State:** São Paulo
- **Country:** Brazil
