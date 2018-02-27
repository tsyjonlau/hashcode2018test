def get_opposite_cell(cell):
    return 0 if cell == 1 else 0

def is_valid(pizza, x, y, min):
    t_cnt = 0
    m_cnt = 0
    #print(x[0])
    #print(x[1])
    #print(y[0])
    #print(y[1])
    for i in range(x[0], x[1]):
        #print("row")
        #print(i)
        for j in range(y[0], y[1]):
            #print("col")
            #print(j)
            t_cnt = t_cnt + 1 if pizza[i][j] == 0 else t_cnt
            m_cnt = m_cnt + 1 if pizza[i][j] == 1 else m_cnt
    return t_cnt >= min and m_cnt >= min
 
def fill_checked(checked, x, y):
    for i in range(x[0], x[1]):
        for j in range(y[0], y[1]):
            checked[i][j] = 1
    return checked

def search_slice(x2, y2, x, y, pizza, checked, infos):
    row_size = infos['row']
    col_size = infos['column']
    wanted_cell = get_opposite_cell(pizza[x][y])
    max_cells = infos['max']

    while x2 is not x:
        while y2 is not y:
            if x2 < row_size and y2 < col_size and x2 * y2 <= max_cells:
                if pizza[x2][y2] == wanted_cell and is_valid(pizza, (x, x2), (y, y2), infos['min']):
                    checked = fill_checked(checked, (x, x2), (y, y2))
                    return (x, x2, y, y2)
            y2 = y2 - 1
        x2 = x2 - 1
    return None
            

def run(infos, pizza):
    output = {
        'size': 0,
        'slices': []
    }
    # tomate = 0
    # mush = 1

    checked = [[0 for x in range(infos['column'])] for y in range(infos['row'])]

    x = 0
    y = 0
    for x in range(infos['row']):
        for y in range(infos['column']):
            if checked[x][y] == 0:
                x2 = x + infos['max']
                y2 = y + infos['max']
                coords = search_slice(x2, y2, x, y, pizza, checked, infos)
                if coords is not None: 
                    output['slices'].append(coords)
    return output

def fill_slice(checked, result, infos):
    y = 0
    for y in range(0, infos['row']):
	    x = 0
	    for x in range(0, infos['column']):
		    if checked[y][x] == 0:
			    result['slice'].append(tuple((y,x,y,x)))
		    x += 1
	    y += 1
    return result
