import logging
import os


class CustomLogger:
    # logging.basicConfig(filename='.//Logs//automation.log',%(pathname)s, filemode='w', format='%(asctime)s: %(levelname)s  %(message)s',
    #                     datefmt='%m-%d-%Y %I:%M:%S %p')
    logging.basicConfig(filename='.//Logs//automation.log', filemode='w',
                        format='%(asctime)s: %(levelname)s  %(message)s',
                        datefmt='%m-%d-%Y %I:%M:%S %p')
    logfile = '<your_file_name>.log'
    if (os.path.isfile('.//Logs//autommation.log')):
        os.remove('.//Logs//autommation.log')

    file_handler = logging.FileHandler('.//Logs//autommation.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s [%(process)d]: %(levelname)s:: %(message)s'))

    logger = logging.getLogger('wbs-server-log')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)


    # @staticmethod
    # def loggen(self):
    #     logging.basicConfig(filename='.//Logs//automation.log', filemode='w',
    #                         format='%(asctime)s: %(levelname)s  %(message)s',
    #                         datefmt='%m-%d-%Y %I:%M:%S %p')
        # logger = logging.getLogger('my zpp')
        # logger.setLevel(logging.INFO)
        # return self.logger



# LogGen.loggen().info('oiuygftdrfg bcvncnv  bhd fghlkh')
# l=LogGen()
# l.loggen().info('igbhjbhvgg')
# LogGen.logger.info('kjhgfhgvgyfyfyffy')

# import logging
# logging.basicConfig(filename =".\\Logs\\autombation.log",format='%(pastime)s -  %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p')
# logging.log(1,'eeeeeeee')
# logging.basicConfig()
