from datetime import datetime , timedelta

class Difference:

    def difference_with_current(self, date):
        try:
            current_date = datetime.now().date()
            input_date = datetime.strptime(date, '%d.%m.%Y').date()
            return (current_date - input_date).days
        except ValueError:
            return None
        
    def difference(self, date_str1,date_str2):
        try:
            date1 = datetime.strptime(date_str1 , '%d.%m.%Y').date()
            date2 = datetime.strptime(date_str2 , '%d.%m.%Y').date()
            return (date1 - date2).days
        except ValueError:
            return None
        
    def days_after(self, days):
        try:
            current_date = datetime.now().date()
            future_date = current_date + timedelta(days = days)
            return future_date.strftime('%d.%m.%Y')
        except ValueError:
            return None
        
    def days_before(self, days):
        try:
            current_date = datetime.now().date()
            past_date = current_date - timedelta(days = days)
            return past_date.strftime('%d.%m.%Y')
        except ValueError:
            return None
        
    def month_after(self, months):
        try:
            current_date = datetime.now().date()
            future_date = current_date + timedelta(days = months * 30)
            return future_date.strftime('%d.%m.%Y')
        except ValueError:
            return None
    
    def month_before(self, months):
        try:
            current_date = datetime.now().date()
            past_date = current_date - timedelta(days = months * 30)
            return past_date.strftime('%d.%m.%Y')
        except ValueError:
            return None