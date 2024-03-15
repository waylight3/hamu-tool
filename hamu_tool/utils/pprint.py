def _pprint(obj : any, max_deep : int = -1) -> list:
    if max_deep == 0:
        return ['...']
    elif type(obj) == list:
        cells = []
        for item in obj:
            cells.append(_pprint(item, min(max_deep - 1, -1)))
        col0_width = len(f'{len(obj)}') + 2
        col1_width = 3
        for cell in cells:
            col1_width = max(col1_width, len(cell[0]) + 2)
        row_heights = []
        for cell in cells:
            row_heights.append(len(cell))
        table_width = col0_width + col1_width + 3
        table_height = sum(row_heights) + len(row_heights) + 1

        result = [[' ' for j in range(table_width)] for i in range(table_height)]

        for i in range(table_width):
            result[0][i] = '-'
        result[0][0] = '+'
        result[0][col0_width + 1] = '+'
        result[0][-1] = '+'

        for i in range(len(cells)):
            base_y = sum(row_heights[:i]) + i + 1
            base_x = col0_width + 3
            for y in range(len(cells[i])):
                for x in range(len(cells[i][y])):
                    result[base_y + y][base_x + x] = cells[i][y][x]
            for y in range(row_heights[i]):
                result[base_y + y][0] = '|'
                result[base_y + y][col0_width + 1] = '|'
                result[base_y + y][-1] = '|'
            for j in range(table_width):
                result[base_y + row_heights[i]][j] = '-'
            result[base_y + row_heights[i]][0] = '+'
            result[base_y + row_heights[i]][col0_width + 1] = '+'
            result[base_y + row_heights[i]][-1] = '+'
            result[base_y][1:col0_width] = f'{i:>{col0_width - 1}}'
        return [''.join(row) for row in result]
    elif type(obj) == dict:
        cells = []
        col0_width = 3
        for key in obj:
            cells.append(_pprint(obj[key], min(max_deep - 1, -1)))
            col0_width = max(col0_width, len(f'{key}') + 2)
        col1_width = 3
        for cell in cells:
            col1_width = max(col1_width, len(cell[0]) + 2)
        row_heights = []
        for cell in cells:
            row_heights.append(len(cell))
        table_width = col0_width + col1_width + 3
        table_height = sum(row_heights) + len(row_heights) + 1

        result = [[' ' for j in range(table_width)] for i in range(table_height)]

        for i in range(table_width):
            result[0][i] = '-'
        result[0][0] = '+'
        result[0][col0_width + 1] = '+'
        result[0][-1] = '+'

        for i in range(len(cells)):
            base_y = sum(row_heights[:i]) + i + 1
            base_x = col0_width + 3
            for y in range(len(cells[i])):
                for x in range(len(cells[i][y])):
                    result[base_y + y][base_x + x] = cells[i][y][x]
            for y in range(row_heights[i]):
                result[base_y + y][0] = '|'
                result[base_y + y][col0_width + 1] = '|'
                result[base_y + y][-1] = '|'
            for j in range(table_width):
                result[base_y + row_heights[i]][j] = '-'
            result[base_y + row_heights[i]][0] = '+'
            result[base_y + row_heights[i]][col0_width + 1] = '+'
            result[base_y + row_heights[i]][-1] = '+'
            result[base_y][1:col0_width] = f'{list(obj.keys())[i]:>{col0_width - 1}}'
        return [''.join(row) for row in result]
    else:
        return [str(obj)]


def pprint(obj : any, max_deep : int = -1) -> None:
    table = _pprint(obj, max_deep)
    text = '\n'.join(table)
    print(text)
