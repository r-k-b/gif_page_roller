#!/user/bin/env/python

"""
Configuration tools (loading, getting / setting options etc)

Only for YAML files at the moment.

Be sure to call :func:`use_config_file` before trying to get options.

"""

import yaml
import os

class Config_file(object):
    """
    Change the currently active configuration to `filepath`.
    Won't be checked until options are read or set.
    """
    def __init__(self, file_path):
        self.conf_file = file_path
    
    def read(self, option_name, default_value = NotImplemented):
        """
        Open the active config file and return the value from the supplied 
        `option_name`.
        If the option name is not found in the file and `default_value` is 
        supplied, return `default_value`.
        
        :raises IOError: When the config file can't be read at all.
        """
        with open(self.conf_file) as f:
            data = yaml.safe_load(f)
            try:
                result = data[option_name]
            except TypeError:
                if default_value is not NotImplemented:
                    return default_value
                else:
                    raise KeyError('Option <{o}> not found in option file <{f}>.'\
                                   .format(o = option_name, f = self.conf_file))
            else:
                return result
    