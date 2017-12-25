'''
super(type[, object-or-type])
Return the superclass of type. If the second argument is omitted the super object
returned is unbound. If the second argument is an object, isinstance(obj, type) 
must be true. If the second argument is a type, issubclass(type2, type) must be 
true. super() only works for new-style classes.
A typical use for calling a cooperative superclass method is:   
class C(B):
	def meth(self, arg):
    	super(C, self).meth(arg)
'''

# 漩涡鸣人的博客, https://www.cnblogs.com/lovemo1314/archive/2011/05/03/2035005.html

# 使用非绑定的类方法进行修改

class A(object):
	def __init__(self):
		print('enter A')
		print('leave A')
		
# 类B继承A

class B(A):
	def __init__(self):
		print('enter B')
		A.__init__(self)
		print('leave B')
		
#############################下面使用super

class B(A):
	def __init__(self):
		print('enter B')
		super(B,self).__init__()
		print('leave B')
		
