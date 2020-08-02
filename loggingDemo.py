import logging

logging.basicConfig(filename="E://test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y  %I:%M:%S: %p',
                    level=logging.DEBUG)

logging.debug("This is debug")
logging.info("This is info")
logging.warning("This is warning")
logging.error("This is an error")
logging.critical("This is a critical error")