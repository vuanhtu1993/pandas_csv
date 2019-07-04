import numpy as np
import pandas

csv = pandas.read_csv('db1.csv')

result = {}

for i in range(5):
    if i == 4:
        result['fifth_col'] = []
    else:
        result[csv.columns[i]] = []

for i, rows in csv.iterrows():
    fifth_col = []
    for j, value in enumerate(rows):
        # fill value for new file
        if j < 4:
            result[rows.index[j]].append(value)
        else:
            if value == 1:
                fifth_col.append(rows.index[j])

    result['fifth_col'].append(fifth_col)

for i in result:
    if i == "fifth_col":
        for j, item in enumerate(result[i]):
            result[i][j] = " ".join(item)

for i in result:
    print(len(result[i]))

print(result)

# exit()

df = pandas.DataFrame(result)
export_csv = df.to_csv(r'result.csv', index=None, header=True)
