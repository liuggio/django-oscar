from django.db.models import ForeignKey
from django.conf import settings

from oscar.relations import DEFAULT_FOREIGN_KEYS
try:
    FOREIGN_KEYS = settings.FOREIGN_KEYS
except AttributeError:
    FOREIGN_KEYS = {}

class MissingForeignKey(Exception):
    pass

class ConfigurableForeignKey(ForeignKey):
    
    def __init__(self, to_key, **kwargs):
        super(ConfigurableForeignKey, self).__init__(self.look_up_key(to_key), **kwargs)
        
    def look_up_key(self, key):
        """
        Returns the appropriate foreign key string, either from
        the defaults or from the user configured settings
        """
        if FOREIGN_KEYS.has_key(key):
            return FOREIGN_KEYS[key]
        elif DEFAULT_FOREIGN_KEYS.has_key(key):
            return DEFAULT_FOREIGN_KEYS[key]
        else:
            raise MissingForeignKey  
        
        