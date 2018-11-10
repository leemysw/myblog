import hashlib
import random
import string


def hash_code(s, salt='mysite'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def make_confirm_code():
    code = ''
    words = ''.join((string.ascii_letters, string.digits))
    for i in range(5):
        code += random.choice(words)

    return code
