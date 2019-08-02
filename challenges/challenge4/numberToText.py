def convert_to_text(num):
    text_num = ""
    ones_position = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens_position = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands_position = ["thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]
    to_convert = str(num)
    digits = ""
    for char in reversed(to_convert):
        digits = digits + char

    for place, digit in enumerate(digits, start=1):
        if text_num != "" and text_num[0] != " ":
            text_num = " " + text_num
        if place % 3 == 1 and len(digits) > 3 and place > 3:
            text_num = " " + thousands_position[int((place-1) / 3) - 1] + text_num
        if place % 3 == 1:
            if len(digits) > place and digits[place] == "1":
                text_num = tens[int(digit)] + text_num
            else:
                text_num = ones_position[int(digit)] + text_num
        elif place % 3 == 2 and digit != "1":
            text_num = tens_position[int(digit)] + text_num
        elif place % 3 == 0 and digit != "0":
            text_num = ones_position[int(digit)] + " hundred" + text_num

    return text_num
