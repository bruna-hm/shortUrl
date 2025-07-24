import random
import string

def encurtar_url(tamanho=3):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))

    