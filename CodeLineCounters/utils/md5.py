# coding: utf-8

import hashlib
from setting import config

# 加密
def md5(arg):
    hash = hashlib.md5(config.SALT)

    hash.update(bytes(arg))

    ret = hash.hexdigest()

    return ret
