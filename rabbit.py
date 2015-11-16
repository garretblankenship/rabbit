#!.env/bin/python
import yaml
import subprocess
import os
import sys
import string

config = {
  'fileName': 'rabbit.yaml',
  'searchDepth': 3,
}

class Rabbit(object):
  'Command Line Hopper'

  def run(self, args):
    'Runs the array of arguments'
    subprocess.call(args);

  def read(self, inputFile):
    'Read the given yaml file and return it as a dict'
    stream = file(inputFile, 'r')
    value = yaml.load(stream)
    return value

  def findConfig(self):
    'finds the path to the closest config file'
    fileFound = False
    depth = 0
    while (fileFound == False and depth < config['searchDepth']):
      search = './'
      for index in range(depth):
        search += '../'
      search += config['fileName']
      if os.path.isfile(search):
        fileFound = search
      depth += depth + 1
    return fileFound

  def converStringToArgs(self, inputCall):
    preJoin = string.split(inputCall, " ")
    args = []
    trackingString = False
    thisArg = ''
    for item in preJoin:
      # If tracking an argument
      if trackingString:
        thisArg = " ".join((thisArg, item))
        # If string ends with "
        if item[-1:] == '"':
          args.append(thisArg)
          trackingString = False
      # If not tracking argument
      else:
        # If string begins with "
        if item[:1] == '"':
          trackingString = True
          thisArg = item
        else:
          args.append(item)
    return args

# Command Line Interface Handler
class Cli:
  'A class to handle running the command line tool & parsing command line arguments'
  def __init__(self):
    args = sys.argv
    yamlFile = Rabbit().findConfig()
    if yamlFile == False:
      print "Couldn't find " + config['fileName']
      exit()
    config = Rabbit().read(yamlFile)
    print config
    # Find command in config
    # proxy command
    # run proxied command
    

    
    

if __name__ == "__main__":
  Cli()