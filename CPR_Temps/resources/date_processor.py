

"""
Simple date processor to take the datetime object and convert it into
a more usable date format that would be expected on the card.
"""

def process_date(date):
    str_date = str(date)
    year = str_date[:4]
    month = str_date[5:7]
    day = str_date[8:10]
    return ("{}/{}/{}".format(month, day, year))
