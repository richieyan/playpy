# coding: utf-8
#singleton pattern

class Singleton(object):
	"""decorate for singleton"""
	def __init__(self, cls):
		self._cls = cls
	def Instance(self):
		try:
			return self._instance
		except AttributeError:
			self._instance = self._cls()
			return self._instance
	def __call__(self):
		raise TypeError('Singletons must be accessed through Instance()')
	def __instancecheck__(self,inst):
		print '........'

@Singleton
class A:
	"""docstring for A"""
	def __init__(self):
		pass
	def display(self):
		return id(self)

if __name__ == '__main__':
	s1 = A.Instance()
	s2 = A.Instance()
	print(s1,s1.display())
	print(s2,s2.display())
	print(s1 is s2)











