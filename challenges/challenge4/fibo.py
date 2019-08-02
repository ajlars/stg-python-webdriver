from challenges.challenge4.numberToText import convert_to_text


def fibonacci(n):
    fibo = None
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    fibo = a
    return f'{fibo} - {convert_to_text(fibo)}'

# This one caused memory issues - for example, grabbing order 62 just hung indefinitely.
# def fibcalc(n):
#     if n <= 1:
#         return n
#     else:
#         return fibcalc(n-1) + fibcalc(n-2)