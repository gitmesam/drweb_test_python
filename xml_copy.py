import xml.etree.ElementTree as ET
import shutil
import os.path
import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    DEF_PATH = 'F:/OneDrive/Python/drweb_test_python-master/file_list.xml'
    parser.add_argument('path', nargs='?', default=DEF_PATH)
    return parser


class FileCopier:
    def __init__(self, path: str):
        self.config_path = path
        self.tree = ET.parse(self.config_path)
        self.root = self.tree.getroot()

    def run_copy(self):
        for files in self.root:
            name = files.get("name")
            inputPath = files.find("inputPath").text
            outputPath = files.find("outputPath").text
            if not os.path.exists(outputPath):
                os.mkdir(outputPath)
            try:
                shutil.copy(inputPath+name, outputPath+name)
            except IOError as err:
                print(f"ERROR! The {name} is not copied. {err}")
            else:
                print(f"OK! The {name} copied from {inputPath} to {outputPath}")


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    try:
        copier=FileCopier(namespace.path)
    except  IOError:
        print('ERROR - Config file not found!')
    else:
        copier.run_copy()
    finally:
        print('Job done!')

        
