import json
import base64
import hmac
import hashlib
import time
import configRead

ERROR_CODE = 401
EXPIRE_CODE = 402

expire = 1800
salt = configRead.ReadElem("Admin", "Passwd")

def tobase64(strs):
    return strs
    # return base64.b64encode(strs.encode('utf-8'))

def frombase64(strs):
    return strs

    # return str(base64.b64decode(strs), 'utf-8')

def get_token():
    first = configRead.ReadElem("Admin", "UserName")

    header = {
        "name": first,
        "exp": int(time.time()) + expire
    }
    header = base64.b64encode(json.dumps(header).encode('utf-8'))
    header = str(header, 'utf-8')
    sign = base64.b64encode(hmac.new(salt.encode('utf-8'), header.encode('utf-8'), digestmod=hashlib.sha256).digest())
    sign = str(sign, 'utf-8')
    return tobase64(header + '.' + sign)

def decode_token(token):
    header, sign = token.split('.')
    second = base64.b64encode(hmac.new(salt.encode('utf-8'), header.encode('utf-8'), digestmod=hashlib.sha256).digest())
    second = str(second, 'utf-8')
    if second == sign:
        return header
    else:
        return ERROR_CODE

def check_token(token):
    if token == '':
        return ERROR_CODE
    token = frombase64(token)
    header = decode_token(token)
    if header != ERROR_CODE:
        header = json.loads(base64.b64decode(header))
        now = int(time.time())
        if header['exp'] > now:
            return get_token()
        else:
            return EXPIRE_CODE
    else:
        return ERROR_CODE



a= get_token()
print(a)
print(check_token(a))