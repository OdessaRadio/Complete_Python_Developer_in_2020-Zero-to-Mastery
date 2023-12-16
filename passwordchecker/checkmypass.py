import requests
import hashlib

# k anonimity
# Idempotence MD5 hash generator
# Linear Probing hash function
# Rehashing
# Double hashing
# Collisions in tables


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/ranfdge/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api')
    return res


def pwned_api_check(password : str):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    print(first5_char, tail)
    response = request_api_data( first5_char )
    
    return response


#request_api_data('123')
pwned_api_check('123')