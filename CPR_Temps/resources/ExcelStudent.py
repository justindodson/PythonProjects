# student class used when performing a batch creation from an Excel document template.
class ExcelStudent:

    # constructor to create the student object with all needed parameters
    def __init__(self, f_name, l_name, site_name, address1, address2, city, state, zipcode ):
        self.f_name = f_name
        self.l_name = l_name
        self.site_name = site_name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode
