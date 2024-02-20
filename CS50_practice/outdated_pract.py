# my_dict = {'banana': 3, 'apple': 5, 'orange': 2, 'grape': 8}

# #! Get the keys in alphabetical order
# sorted_keys = sorted(my_dict.keys())

# #! Print the sorted keys
# for key in sorted_keys:
#   print(key, end=" ")

# print("Jay Shree Ram")

# #! get the dic with key in alphabetical order
# sorted_dict = {key: my_dict[key] for key in sorted(my_dict) }

# #! Print the sorted dict
# print(sorted_dict)

def main():
    user_date = get_user_date("Date: ")
    result_date = format_date(user_date)
    # print(result_date)

# list of months:
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

# define get_user_date fn
def get_user_date(promt):
    while True:
        try:
            date_inp = input(promt)
            if date_inp[0].isalpha():
                month, day, year = date_inp.split(" ")
                day = day[0: -1]
                month = month.title()
                if month in months and day <= 31 and len(year) == 4:
                    month = months.index(month) + 1
                    return [year, month, day]
            elif date_inp[0].isdigit():
                month, day, year = date_inp.split("/day")
                month = int(month)
                day = int(day)
                if month <= 12 and day <= 31 and len(year) == 4:
                    return [year, month, day]
        except ValueError or KeyError:
            pass



# define format_date Fn
def format_date(date_list):
    yy = date_list[0]
    mm = date_list[1]
    dd = date_list[2]

    if mm < 10 and dd < 10:
        pass


# call main Fn
    main()
