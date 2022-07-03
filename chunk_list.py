general_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one','twenty-two', 'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven', 'twenty-eight','twenty-nine', 'thirty', 'thirty-one', 'thirty-two', 'thirty-three', 'thirty-four', 'thirty-five']

def chunks(lst, n, d=0):
    for i in range(d, len(lst), n):
        yield lst[d:i+n]

print(next(chunks(general_list, 5)))    # ['one', 'two', 'three', 'four', 'five']
print(next(chunks(general_list, 3, 7))) # ['eight', 'nine', 'ten']
print(next(chunks(general_list, 8, 3))) # ['four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven']
print(next(chunks(general_list, len(general_list))))    # All list