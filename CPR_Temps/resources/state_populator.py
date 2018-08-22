import openpyxl


def state_populator():
    workbook = openpyxl.load_workbook('resources/us_states.xlsx')
    sheet = workbook.get_sheet_by_name('Sheet1')
    states_list = []
    for state in range(1, 51):
        sv = sheet['A{}'.format(state)].value
        states_list.append(sv)

    return states_list
