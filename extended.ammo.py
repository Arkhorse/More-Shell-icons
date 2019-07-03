# Imports
import logging
import BigWorld
from debug_utils import LOG_CURRENT_EXCEPTION
from constants import SHELL_TYPES
from items import ITEM_TYPES, ITEM_TYPE_NAMES, makeIntCompactDescrByID
from items.components import shell_components

def init():
    pass

class EXTENDED.SHELL.TYPES(SHELL_TYPES):
    AP-AC = 'AP-AC'
    
SHELL_TYPES_LIST = (SHELL.TYPES.

)
ATTLE_RESULT_WAITING_TIMEOUT = 0.1
SHELL_TYPES_INDICES = dict(((value, index) for index, value in enumerate(SHELL_TYPES_LIST)))