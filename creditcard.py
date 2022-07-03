# Valid = 4541230050459092
def validate(card_number):
    def digits_of(n):
        return[int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-1::-2]
    check_sum = 0
    check_sum += sum(odd_digits)
    for d in even_digits:
        check_sum += sum(digits_of(d*2))
    return check_sum % 10

if validate(input("Enter card number: \n")) == 0:
    print("Credit card is valid".center(30))
else:
    print("Credit card is not valid".center(30))
