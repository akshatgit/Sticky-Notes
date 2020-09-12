import os, fnmatch
class Crawler():
    '''
        Class to scan a particular directory for python and HTML files. 
    '''

    def __init__(self, **kwargs):

        self.scan_directory = kwargs.get("directory")

        self.code_files = {
            "Python": list(),
            "HTML": list()
        }

        self.patterns = {
            "Python" : "*.py",
            "HTML" : "*.html"
        }
        self._getCodeFiles()

    def _matchFile(self, path):
        # If file matches the regex, add it to code_filess
        for lang in self.patterns:
            pattern = self.patterns[lang]
            if fnmatch.fnmatch(path, pattern):
                self.code_files[lang].append(path)

    def _getCodeFiles(self):
        # Scan entire directory 
        for r, d, f in os.walk(self.scan_directory):
            for file_name in f:
                path = os.path.join(r, file_name)
                self._matchFile(path)
    
    def getCodeFiles(self, language="Python"):
        # Return file list for the specific language
        return self.code_files[language]
    
    def getAllCodeFiles(self):
        # Return the entire dictionary containing all code files
        return self.code_files
    pass