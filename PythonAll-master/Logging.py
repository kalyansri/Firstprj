import logging

LOG_FORMAT="%(Levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="C:\\Users\\Va185060\\Desktop\\Knowledge\\ss.log",
                    level=logging.DEBUG,format=LOG_FORMAT)
logger=logging.getLogger()


#Test message
logger.info("this is info")
logger.debug("this is debug")
logger.warning("this is warn")
logger.error("this is error")


logger.critical("thi is critical")