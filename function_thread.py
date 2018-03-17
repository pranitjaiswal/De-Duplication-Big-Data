import threading


class FunctionThread(threading.Thread):
	def __init__(self, function_name):
		threading.Thread.__init__(self)
		self.function_name = function_name

	def run(self):
		self.function_name()
