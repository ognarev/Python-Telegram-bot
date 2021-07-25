from forismatic import *

# Return citations from forismatic
def get_citation(lang='ru'):
    f = forismatic.ForismaticPy()
    text = f.get_Quote(lang)
    formated_text = (f"{text[0]} \n {text[1]}")
    #print(formated_text)
    return formated_text 

#get_citation()