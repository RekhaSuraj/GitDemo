import logging

def test_loggingDemo():

    logger_obj = logging.getLogger(__name__)
    filehandler_obj = logging.FileHandler("logfile.log")
    formatter_obj = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    filehandler_obj.setFormatter(formatter_obj)

    logger_obj.addHandler(filehandler_obj)

    logger_obj.setLevel(logging.DEBUG)
    logger_obj.debug("A debug statement is executed")
    logger_obj.info("Information statement")
    logger_obj.warning("Something is in warning mode")
    logger_obj.error("A Major error has happened")
    logger_obj.critical("Critical issue")
