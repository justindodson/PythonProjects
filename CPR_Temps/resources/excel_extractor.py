import openpyxl
from resources.date_processor import process_date


class ExcelData:

    def __init__(self, class_size, exel_file_name, counter=1, ):
        self.class_size = class_size
        self.counter = counter
        self.wb = openpyxl.load_workbook(exel_file_name)
        self.sheet = self.wb.get_sheet_by_name('Sheet1')

    # returns a dictionary of students as a key and a list of all the data in their
    # corresponding row as the value.
    def extract_data(self):
        values = {}
        while self.class_size >= self.counter:
            student_info = self.row_data_group((self.counter + 2))
            values['Student {}'.format(self.counter)] = student_info
            self.counter += 1
        return values

    # Method to put each row's data into a list to be returned.
    def row_data_group(self, row_number):
        column_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
        data_list = []
        for col in column_list:
            data_list.append(self.sheet[col+str(row_number)])
        return data_list

    # this method will return the String value of a specific cell.
    def extract_cell_data(self, col_name, row_number):
        name = None
        try:
            if row_number > 2:
                name = self.sheet['{}{}'.format(col_name, row_number)]
            return name.value
        except ValueError:
            raise Exception("You cannot enter data from the top 2 rows. Must start at row 3!")

    # This method is used to create a student. The method takes a row number
    # and creates a list of that row's location data. It then iterates over the data list
    # and removes any 'None' values and appends all the text values of the
    # location values to a new list. The date cells are processed to a better format
    # and then an ExcelStudent object is created and returned with the list values
    def create_student(self, row_number):
        row_data = self.row_data_group(row_number)
        student_data = []
        for cell in row_data:
            if cell.value is None:
                cell = ""
                student_data.append(cell)
            else:
                student_data.append(cell.value)

        student = (student_data[0], student_data[1], student_data[2],
                   student_data[3], student_data[4], student_data[5],
                   student_data[6], student_data[7])

        return student
