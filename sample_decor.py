def decor(foo):
	def new_foo(*args, **kwargs):
		print('Код до вызова функции')
		result = foo(*args, **kwargs)
		print('Код после вызова функции')
		return result

	return new_foo


def parametrized_decor(parameter):
	def decor(foo):
		def new_foo(*args, **kwargs):
			print('Код до вызова функции')
			result = foo(*args, **kwargs)
			print('Код после вызова функции')
			return result

		return new_foo

	return decor


@parametrized_decor(parameter=None)
def foo():
	pass