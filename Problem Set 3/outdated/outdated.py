def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            date = input("Date: ").strip()
            month, day, year = date.split("/")
            if month.isnumeric() and day.isnumeric() and year.isnumeric():
                day = int(day)
                month = int(month)
                year= int(year)
                if month <= 12 and day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break
                else:
                    continue
            else:
                continue
        except ValueError:
            m, d, y = date.split(" ")

            if m in months and ',' in d:
                d= int(d.replace(',',""))
                if 0 <= d <= 31:
                    print(f"{y:04}-{months.index(m)+1:02}-{d:02}")
                    break
                else:
                    continue
            else:
                pass


main()
