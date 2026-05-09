def input_data(n=None, dtype=float):
    data = []
    i = 0
    while True:
        if i==n: return data
        inp = input(f'Enter element {i+1}: ')
        if not inp and n is None: return data
        data.append(dtype(inp))
        i += 1

def input_table(r=None, c=None, dtype=float, ragged=False):
    print('Row 1:')
    row1 = input_data(c, dtype=dtype)
    table = [row1]
    c_new = c if ragged else len(row1)
    while True:
        try:
            if len(table)==r: return table
            print(f'Row {len(table)+1}:')
            row = input_data(c_new, dtype=dtype)
            if not row and r is None: return table
            table.append(row)
        except ValueError as e:
            if r is c is None: return table
            else: raise e