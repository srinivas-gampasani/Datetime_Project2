'''

from datetime import datetime

class MyDatetime:
    def _init_(self, year=None, month=None, day=None, hour=0, minute=0, second=0):
        if year is None:
            current_time = datetime.utcnow()
            self.date = current_time
        else:
            self.date = datetime(year, month, day, hour, minute, second)
    
    @classmethod
    def from_iso_format(cls, iso_string):
        return cls(*map(int, iso_string.split('-')))
    
    def iso_format(self):
        return self.date.strftime('%Y-%m-%dT%H:%M:%SZ')
    
    def human_readable_format(Self):
        return Self.date.strftime('%Y-%m-%d %H:%M:%S')
    
    @staticmethod
    def validate_date(year, month, day):
        try:
            datetime(year, month, day)
            return True
        except ValueError:
            return False
        
    @classmethod
    def date_difference(cls, date1, date2):
        if date1 > date2:
            date1, date2 = date2, date1
        difference = date2 - date1
        return difference.days
    
    @staticmethod
    def weekday_calculator(year, month, day):
        return datetime(year, month, day).strftime('%A')
    

'''
from datetime import datetime

class MyDatetime:
    def __init__(self, year=None, month=None, day=None, hour=0, minute=0, second=0):
        if year is None:
            current_time = datetime.utcnow()
            self.date = current_time
        else:
            self.date = datetime(year, month, day, hour, minute, second)

    @classmethod
    def from_iso_format(cls, iso_string):
        date_parts = iso_string.split('T')[0].split('-')
        time_parts = iso_string.split('T')[1].rstrip('Z').split(':')
        return cls(*map(int, date_parts + time_parts))

    def iso_format(self):
        return self.date.strftime('%Y-%m-%dT%H:%M:%SZ')

    def human_readable_format(self):
        return self.date.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def validate_date(year, month, day):
        try:
            datetime(year, month, day)
            return True
        except ValueError:
            return False

    @classmethod
    def date_difference(cls, date1, date2):
        if date1 > date2:
            date1, date2 = date2, date1
        difference = date2 - date1
        return difference.days

    @staticmethod
    def weekday_calculation(year, month, day):
        calculated_weekday = datetime(year, month, day).strftime('%A')
        print(f"Calculated weekday: {calculated_weekday}")
        return calculated_weekday

   