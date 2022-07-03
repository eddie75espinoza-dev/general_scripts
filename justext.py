
my_str = 'La alegría es el ingrediente principal en el compuesto de la salud'
large = 29

def just_text(my_str, large):
    n = 0
    lst_word = []
    result = []
    for x in my_str[:].split(): 
        n += len(x)    
        if n < large:
            lst_word.append(x)
        else:
            result.append(' '.join(lst_word))
        print(result, x)        
    n, lst_word = 0, []
    result = []
    
just_text(my_str, large)