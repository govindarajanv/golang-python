import logging

# Create and configure logger
logging.basicConfig(filename="newfile.log",format="%(levelname)s %(asctime)s %(message)s",filemode="w") 

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
logger.debug("Debug Message")
logger.info("For your information")
logger.warning("Its a Warning")
logger.error("Oops, some error")
logger.critical("Production Outage")
