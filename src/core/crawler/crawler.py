import os
import json
from src.core.util.conf.config import ConfigReader
class Crawler():
    '''
        Class to scan a particular directory for python and HTML files. 
    '''

    def __init__(self, **kwargs):

        self.scan_directory = kwargs.get("directory")

        self.code_files = dict()

        self.language_config = ConfigReader().getConfig()["Lang-extensions"]
        self.language_patterns = dict()

        # Read Language extensions
        self._import_config()

        # Scan Directory
        self._getCodeFiles()

    def _import_config(self):

        # Import Language extensions and create a mapping. for e.g. {".py": "Python"}
        for lang in self.language_config:
            lang_name = lang["name"]
            if "extensions" in lang:
                extensions = lang["extensions"]
            else:
                continue
            for extension in extensions:
                self.language_patterns[extension] = lang_name
        return


    def _addCodeFile(self, file_path, lang_name):

        # Add file to detected code language list
        if lang_name in self.code_files:
            self.code_files[lang_name].append(file_path)
        else:
            self.code_files[lang_name] = [file_path]
        return

    def _matchFile(self, file_path):

        # If file matches the regex, add it to code_filess
        file_extension = "." + file_path.split(".")[-1]
        if file_extension in self.language_patterns:
            lang_name = self.language_patterns[file_extension]
            self._addCodeFile(file_path, lang_name)

    def _getCodeFiles(self):

        # Scan entire directory 
        for r, d, f in os.walk(self.scan_directory):
            for file_name in f:
                file_path = os.path.join(r, file_name)
                self._matchFile(file_path)
    
    def getCodeFiles(self, language="Python"):

        # Return file list for the specific language
        return self.code_files[language]
    
    def getAllCodeFiles(self):

        # Return the entire dictionary containing all code files
        return self.code_files
    
    def getAllCodeLang(self):

        # Return all detected code types
        return self.code_files.keys()
    pass

# for testing
if __name__ == "__main__":
    test = Crawler(directory=".")
    test.getAllCodeLang()
    print(test.getCodeFiles("JSON"))