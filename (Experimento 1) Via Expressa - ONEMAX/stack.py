class stack(object):
	"""docstring for stack"""
	def __init__(self):
		self.pilha = []

	def desempilhar(self):
		if not self.p_vazia():
			self.pilha.pop( -1 )

	def empilhar(self, valor):
		self.pilha.append(valor)

	def p_vazia(self):
		return (len(self.pilha) == 0)

	def topo(self):
		return self.pilha[-1]