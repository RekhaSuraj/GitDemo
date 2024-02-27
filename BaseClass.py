import inspect
import logging
import inspect

class BaseClass:
    def get_logger(self):
        # To make sure actual calling function name is logged and not this baseclass when writing logs
        loggerName = inspect.stack()[1][3]
        logger_obj = logging.getLogger(loggerName)
        filehandler_obj = logging.FileHandler("logfile.log")
        formatter_obj = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler_obj.setFormatter(formatter_obj)

        logger_obj.addHandler(filehandler_obj)

        logger_obj.setLevel(logging.DEBUG)
        return logger_obj
