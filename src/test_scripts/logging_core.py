import logging

# Let us Create an object
logging.getLogger().addHandler(logging.StreamHandler())
logger = logging.getLogger('__name__')
# Now we are going to Set the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)