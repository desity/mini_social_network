import clearbit
clearbit.key = 'sk_4954afaf33522aa87e737e31b494ccf2'

def clearbit_def(email):
    person = clearbit.Person.find(email=email, stream=True)
    if person == None:
        return None
    else:
        return person['name']['fullName']
