
import pandas
from pprint import pprint
excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='Лист1',
usecols=['title', 'grade','price','image'])
winms = excel_data_df
print('Excel Sheet to Dict:', winms.to_dict(orient='record'))
