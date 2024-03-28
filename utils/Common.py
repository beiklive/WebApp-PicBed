from enum import Enum

class StatusCode(Enum):
    # Status codes
    STATUS_OK = 0
    STATUS_ERROR = 1
    STATUS_NACK = 2
    STATUS_ACK = 3


class CommandCode(Enum):
    # Command codes
    CMD_TEST = 0
    CMD_SETTING = 1
    CMD_DOWNLOAD = 2
    CMD_UPLOAD = 3
    CMD_DELETE = 4
    CMD_RENAME = 5
    CMD_MOVE = 6
    CMD_COPY = 7
    CMD_NEW_FOLDER = 8
    CMD_GET_FOLDER = 9
    CMD_GET_FILE = 10
    CMD_GET_FILE_INFO = 11
    CMD_GET_FOLDER_INFO = 12
    CMD_GET_FILE_LIST = 13
    CMD_GET_FOLDER_LIST = 14
    