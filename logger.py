"""
A Logging module desined to improve the ease of use for the logging module
"""




class Logger:
	"""
	A base class created to utilize the logging module

	The main functions in order are:
	debug, info, warning, error, critical

	These give various output messages and settings can be changed in order to only show messages above a specific urgency

	Debug is used for just outputting values for testing

	Info is used to inform the user of something

	Warning is used if something is incorrect but will still function

	Error is used in the event of an error

	Critical is used in the event of something very bad or critical for the program to function (such as internet access)

	(If intellisense is desired you need to use loggerName.log.exampleCommand for instance Logger().log.info("This is how we do it :)"))
	"""
	logFormat='[%(asctime)s] [%(funcName)s on line %(lineno)s] [%(levelname)s] %(message)s'
	import logging
	DEBUG=logging.DEBUG
	INFO=logging.INFO
	WARNING=logging.WARNING
	ERROR=logging.ERROR
	CRITICAL=logging.CRITICAL
	def __init__(self,logLevel=logging.NOTSET,fileLoc:str='newfile.log') -> None:
		
		pass
		self.logLevel=logLevel
		log_format = self.logging.Formatter(self.logFormat)
		self.logging.basicConfig(filename=fileLoc,format=self.logFormat,filemode='w')
		self.log=self.logging.getLogger(__name__)

		# writing to stdout (console)
		from sys import stdout
		handler = self.logging.StreamHandler(stdout)
		handler.setLevel(self.logLevel)
		handler.setFormatter(log_format)
		self.log.addHandler(handler)

	def __getattr__(self,__name:str)->any:
		print(__name)
		pass
		# if(self.__dict__.keys)
		# print(list(self.__dict__['log'].__dict__.keys()))
		# print(self.log.)
		return self.log.__getattribute__(__name)



		if(__name in list(self.__dict__['log'].__dict__.keys()) or True):
			return self.log.__getattribute__(__name)
			return self.log.__dict__[__name]
		else:
			raise KeyError(f"Variable {__name} not found in object")


if(__name__=="__main__"):

	# Create and configure logger
	Logger.logging.basicConfig(filename="newfile.log",format=Logger.logFormat,filemode='w')

	# Creating an object
	logger = Logger.logging.getLogger()

	# Setting the threshold of logger to DEBUG
	logger.setLevel(Logger.logging.NOTSET)

	# Test messages
	logger.debug("Harmless debug Message")
	logger.info("Just an information")
	logger.warning("Its a Warning")
	logger.error("Did you try to divide by zero")
	logger.critical("Internet is down")



	logger=Logger()
	logger.log.info('hi')
	logger.info('hi')
	def test():
		logger.info('hi')
	test()
	# logging.