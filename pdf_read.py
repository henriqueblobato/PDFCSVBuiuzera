from pprint import pprint

import tabula

file_path = 'RelatoriodeVencimento.pdf'

tables = tabula.read_pdf(file_path, pages='all')

dict_ = {}
for t in tables:
    columns = t.columns
    values = t.values.tolist()[0]
    for i in range(len(columns)):
        dict_[columns[i]] = values[i]
pprint(dict_)
