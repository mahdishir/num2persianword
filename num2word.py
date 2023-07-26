import arabic_reshaper
from bidi.algorithm import get_display
def convert(result):
        reshaped_text = arabic_reshaper.reshape(result)
        converted = get_display(reshaped_text)
        return converted


def english_to_farsi_numbers(input_str):
    farsi_digits = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹'
    }

    farsi_numbers = {
        0: 'صفر',
        1: 'یک',
        2: 'دو',
        3: 'سه',
        4: 'چهار',
        5: 'پنج',
        6: 'شش',
        7: 'هفت',
        8: 'هشت',
        9: 'نه',
        10: 'ده',
        11: 'یازده',
        12: 'دوازده',
        13: 'سیزده',
        14: 'چهارده',
        15: 'پانزده',
        16: 'شانزده',
        17: 'هفده',
        18: 'هجده',
        19: 'نوزده',
        20: 'بیست',
        30: 'سی',
        40: 'چهل',
        50: 'پنجاه',
        60: 'شصت',
        70: 'هفتاد',
        80: 'هشتاد',
        90: 'نود',
        100: 'صد',
        200: 'دویست',
        300: 'سیصد',
        400: 'چهارصد',
        500: 'پانصد',
        600: 'ششصد',
        700: 'هفتصد',
        800: 'هشتصد',
        900: 'نهصد'
    }

    def to_farsi(number):
        if number in farsi_numbers:
            return farsi_numbers[number]
        elif number < 100:
            tens = (number // 10) * 10
            ones = number % 10
            return farsi_numbers[tens] + (' و ' + farsi_numbers[ones] if ones > 0 else '')
        elif number < 1000:
            hundreds = number // 100
            remaining = number % 100
            return farsi_numbers[hundreds] + (' صد و ' + to_farsi(remaining) if remaining > 0 else ' صد')
        elif number < 1000000:
            thousands = number // 1000
            remaining = number % 1000
            return to_farsi(thousands) + (' هزار و ' + to_farsi(remaining) if remaining > 0 else ' هزار')
        elif number < 1000000000:
            millions = number // 1000000
            remaining = number % 1000000
            return to_farsi(millions) + (' میلیون و ' + to_farsi(remaining) if remaining > 0 else ' میلیون')
        elif number < 1000000000000:
            billions = number // 1000000000
            remaining = number % 1000000000
            return to_farsi(billions) + (' میلیارد و ' + to_farsi(remaining) if remaining > 0 else ' میلیارد')
        else:
            trillions = number // 1000000000000
            remaining = number % 1000000000000
            return to_farsi(trillions) + (' تریلیارد و ' + to_farsi(remaining) if remaining > 0 else ' تریلیارد')

    try:
        number = int(input_str)
        farsi_str = to_farsi(number)
        return farsi_str
    except ValueError:
        return "ورودی نامعتبر است."

if __name__ == "__main__":
    input_str = input(convert( ":عدد را وارد کنید:"))
    result = english_to_farsi_numbers(input_str)
    print(convert(":نتیجه:"), convert(result))

