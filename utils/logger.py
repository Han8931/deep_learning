import logging
import os, datetime

def get_current_date():
	now = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")

def get_timestamp_id():
	timestamp = str(int(time.time()))
	return timestamp

class ExperimentTracker:
    def __init__(self) -> None:
         pass

    def setup_logger(self, name, log_file, level=logging.INFO):
        """
        name: logger name, ex) 'first logger'
        log_file: save path
        Example---------------------------
        # first file logger
        logger = setup_logger('first_logger', 'first_logfile.log')
        logger.info('This is just info message')
        # second file logger
        super_logger = Setup_Logger('second_logger', 'second_logfile.log')
        super_logger.error('This is an error message')
        ----------------------------------
        """
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger


    def args_logger(self, args, path):
        """
        Print all arguments in argparser using a file operation
        Doesn't use the Python logger
        """
        path_checker(path)
        path = path + f"args_{args.save_model}.txt"

        with open(path, 'w') as f:
            for arg in vars(args):
                m = f"- {arg}: {getattr(args, arg)}\n"
                f.write(m)


    def model_logger(self, path, networks):
        """
        Log a model
        """
        path = path + "network_log.txt"
        with open(path, 'w') as f:
            print(networks, file=f)
            f.write("\n-----------------------------------------------------")
            f.write("\n-----------------------------------------------------")


    def log_path(self, now, path, save_model):
        path_checker(path)
        fname = f"{save_model}_{now.month}_{now.day}.log"
        return path + fname
