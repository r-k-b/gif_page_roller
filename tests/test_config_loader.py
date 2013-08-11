#!/usr/bin/env python

import unittest
import tools.conf_tools as conf_tools

class Test_config_loader(unittest.TestCase):
    #.. TODO: implement these tests!
    
    def test_good_option_found(self):
        config = conf_tools.Config_file(r'testdata\valid.yaml')
        try:
            optionvalue = config.read('count_to_three')
        except Exception as e:
            raise e
        self.assertEqual(optionvalue, ['one', 'two', 'three'])
    
    def test_bad_option_found(self):
        return NotImplemented
    
    def test_no_config_file_exists(self):
        return NotImplemented
    
    def test_config_file_is_not_valid_YAML(self):
        return NotImplemented


if __name__ == '__main__':
    unittest.main()