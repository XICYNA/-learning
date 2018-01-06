# -*- coding: utf-8 -*-
import random,hashlib

def get_md5(password):
	return hashlib.md5(password.encode('utf-8')).hexdigest()

class User(object):
	def __init__(self, username, password):
		self.username = username
		self.salt = ''.join([chr(random.randint(48,122)) for i in range(20)])
		self.password = get_md5(password + self.salt)

db = {
	'michael': User('michael', '123456'),
	'bob': User('bob', 'abc999'),
	'alice': User('alice', 'alice2008')
}

def login(username,password):
	user = db[username]
	return user.password == get_md5(password + user.salt)

# 测试
assert login('michael','123456')
assert login('bob', 'abc999')
assert login('alice','alice2008')
assert not login('michael', '1')
assert not login('bob', 'asdas')
print('ok')

#################### another algorithm ############

# _*_ coding: utf-8 _*_

import hmac, random

def get_md5(key, s):
	return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
	def __init__(self, username, password):
		self.username = username
		self.key = ''.join([chr(random.randint(48,122)) for i in range(20)])
		self.password = get_md5(self.key, password)


db = {
	'michael': User('michael', '123'),
	'alice': User('alice', '321'),
	'bob': User('bob','111')
}

def login(username,password):
	user = db[username]
	return get_md5(user.key,password) == user.password


### 测试

assert login('michael', '123')
assert login('alice', '321')
assert login('bob', '111')
assert not login('michael', '321')
assert not login('bob', '123')

print('ok')
