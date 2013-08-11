#!/user/bin/env python

import os
import tools.conf_tools as conf

configs = conf.Config_file('gif_page_roller_config.yaml')
print configs.read('find_extensions')

def get_image_names(directory):
    """
    
    """
    pass

