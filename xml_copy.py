import xml.etree.ElementTree as ET
import shutil

tree = ET.parse('F:/OneDrive/Python/DrWeb_Test/file_list.xml')
root = tree.getroot()


for files in root:
    name = files.get("name")
    input_path = files.find("input_path").text
    output_path = files.find("output_path").text
    try:
        shutil.move(input_path+name, output_path+name)
        print("File "+name+" moved to "+output_path)
    except IOError:
        print('IOError')
