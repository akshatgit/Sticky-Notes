import json

import json
import os
class ConfigReader():
    '''
    Class to read Configs present in conf dir
    '''

    def __init__(self, **kwargs):
        # Config lists
        self.conf_files = {
            "Lang-extensions": "languages.json"
            }
        self.configs = dict()
        self._load_conf()

    def _load_conf(self):
        conf_dir = os.path.dirname(os.path.realpath(__file__))

        for conf in self.conf_files:
            conf_file = os.path.join(conf_dir, self.conf_files[conf])
            self.configs[conf] = json.loads(open(conf_file).read())

    def getConfig(self):
        return self.configs

    pass