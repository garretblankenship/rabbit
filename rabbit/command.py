import click
import subprocess

class Command(object):
	""" Command Class

	Responsible for:
	- Storing a command data
	- Calling a command
	"""
	
	def __init__ (self, data = {}):
		self.data = {}
		# Set to and Hop
		self.data['hop'] = data.get('hop')
		self.data['to'] = data.get('to')
		# Set Description
		self.data['description'] = data.get('description')
		if self.data['description'] is None:
			self.data['description'] = self.generateDescription()
		self.name = self.getName()
		self.groups = self.getGroups()
		self.clickObject = self.setClickObject()

	def generateDescription(self):
		""" Generates a basic description based on the commands properties """
		toCommand = self.data.get('to')
		if toCommand:
			return 'Alias for: ' + self.data.get('to');
		return ''

	def isValid(self):
		""" Checks if this command is valid """
		if self.data.get('hop') is None:
			return False
		if self.data.get('to') is None:
			return False
		return True

	def getGroups(self):
		hop = self.data.get('hop')
		if hop is None:
			return []
		segmented = hop.split(' ')
		return segmented[:-1]

	def getName(self):
		hop = self.data.get('hop')
		if hop is None:
			return []
		segmented = hop.split(' ')
		return segmented[-1]

	def setClickObject(self):
		context = {
			'allow_extra_args': True,
			'allow_interspersed_args': True,
		}
		callback = click.pass_context(self.run)
		commandObj = click.command(
			name = self.getName(), 
			help = self.data.get('description'), 
			context_settings = context
		)(callback)
		
		return commandObj

	def getClickObject(self):
		return self.clickObject


	# Needs Implementation & Tests
	def run(self, context):
		""" Runs the given command """
		print(self.clickObject.params)
		toCommand = self.data.get('to')
		extraArgs = ' '.join(context.args)
		runCommand = '{0} {1}'.format(toCommand, extraArgs)
		subprocess.call(runCommand, shell=True);