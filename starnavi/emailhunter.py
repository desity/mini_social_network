from pyhunter import PyHunter
hunter = PyHunter('2b2179685a1ae6ad66e87b991a475b66cb7e7593')


def verify_email(email):
    # try:
    #     gibberish = hunter.email_verifier(email)['gibberish']
    #     return gibberish
    # except:
    #     return True
    return False

def deliver(email):
    try:
        print(hunter.email_verifier(email)['result'])
    except:
        print('error')
