
import pandas
from pprint import pprint
excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='Лист1',
usecols=['title', 'grade','price','image'])
# print whole sheet data
print('Excel Sheet to Dict:', excel_data_df.to_dict(orient='record'))
