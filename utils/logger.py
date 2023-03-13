import logging
import datetime

now = str(datetime.datetime.now())
timedate = now[:-7]

logging.basicConfig(filename='logs/' + timedate + '.log', level=logging.DEBUG,
                    format='[%(asctime)s] | %(levelname)s | %(message)s')


def log_format(text, level):
    string0 = str(datetime.datetime.now())
    string1 = string0[:-3]
    time = string1.replace(".", ",")
    return "[" + time + "] | " + level + " | " + text


def info(text):
    logging.info(text)


def debug(text):
    logging.debug(text)


def error(text):
    logging.error(text)
