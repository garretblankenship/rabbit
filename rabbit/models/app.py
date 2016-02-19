#!.env/bin/python
from rabbit.models.config import Config
from os.path import expanduser

CONFIG_FILE = "rabbit.yaml"

class App(object):
	""" 
	Base application class.
	Used to setup, configure & run the application.
	"""

	def __init__ (self):
		"""
		Constructor/Init function
		"""
		self.config = Config()
		self.bootstrap()

	def bootstrap(self):
		"""
		Bootstrap the application
		"""
		self.loadHomeConfig()
		self.loadLocalConfig()

	def loadHomeConfig (self):
	  """
	  Load Config From Home Directory
	  """
	  homepath = expanduser('~') + '/' + CONFIG_FILE
	  self.config.load(homepath)

	def loadLocalConfig (self):
	  """
	  Load Config From Local (Current) Directory
	  """
	  localpath = './' + CONFIG_FILE
	  self.config.load(localpath)

		