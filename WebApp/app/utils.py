from calendar import timegm
from datetime import datetime
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
import sys


def get_current_epoch():
    return int(datetime.now().timestamp())

def datetime_to_epoch(time):
    timestamp = datetime.strptime(str(time), TIME_FORMAT)
    epoch = int(timestamp.timestamp())
    return epoch

def epoch_to_datetime(time: int):
    t = datetime.fromtimestamp(time)
    return t.strftime(TIME_FORMAT)


def get_time(epoch: int):
    t = datetime.fromtimestamp(epoch)
    return t.time()


def get_hour(epoch: int):
    t = datetime.fromtimestamp(epoch)
    return t.hour


def get_minute(epoch: int):
    t = datetime.fromtimestamp(epoch)
    return t.minute


def get_date(epoch: int):
    t = datetime.fromtimestamp(epoch)
    return t.date()

def print_to_stderr(text: str):
    print(text, file=sys.stderr)
