import re
import sys
import inflect
from datetime import date, datetime

class Age:
    def __init__(self, user_date):
        if not self.check_valid(user_date):
            sys.exit("Invalid Format")

        self.user_date = user_date

    def calc_min(self):
        i_value = datetime.timestamp(datetime.strptime(self.user_date, '%Y-%m-%d'))
        today_value = datetime.timestamp(datetime.strptime(str(date.today()), '%Y-%m-%d'))
        return int((today_value - i_value) / 60)

    def __str__(self):
        p = inflect.engine()
        minutes = p.number_to_words(self.calc_min())
        minutes = re.sub(r"\band\b", "", minutes)
        minutes = " ".join(minutes.split())
        return minutes.capitalize() + " minutes"

    @staticmethod
    def check_valid(date_str):
        return bool(re.match(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$", date_str))

def main():
    user_date = input("Date of Birth: ")
    user = Age(user_date)
    print(user)

if __name__ == "__main__":
    main()
