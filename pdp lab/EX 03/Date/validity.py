class Valid:

    def IsValidTime(self, time):
        hour, minute, second = time.split(':')
        if -1<int(second)<60 and -1<int(minute)<60 and -1<int(hour)<24:
            return True
        else:
            return False
        
    def IsValidDate(self, date):
        day, month, year = date.split('.')
        month = int(month)
        year = int(year)
        day = int(day)
        if 0<year<10000 and 0<month<13:
            if month == 2:
                if (year%400==0 or (year%4==0 and year%100!=0)) and day<30:
                    return True
                elif day<29:
                    return True
                else:
                    return False
            elif (month==4 or month==6 or month==9 or month==11) and day<31:
                return True
            elif (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and day<32:
                return True
            else:
                return False
        else:
            return False