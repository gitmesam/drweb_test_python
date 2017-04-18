import xml.etree.ElementTree as ET
import shutil
import os.path

filelist = 'F:/OneDrive/Python/DrWeb_Test/file_list+.xml'

try:
    tree = ET.parse(filelist)
    root = tree.getroot()

    for files in root:
        name = files.get("name")
        input_path = files.find("input_path").text
        output_path = files.find("output_path").text

        if os.path.exists(output_path) == 0:
            try:
                os.mkdir(output_path)
            except:
                print("\""+name+"\" - ERROR! Can\'t find output path: \""+output_path+"\"")
        else:
            if os.path.exists(input_path+name):
                try:
                    shutil.move(input_path+name, output_path+name)
                except:
                    print("Unknown Error")
                else:
                    print("\""+name+"\" - OK")
            
            else:
                print("\""+name+"\" - ERROR! File not found in \""+input_path+"\"")

    print("The job is done!")

except:
    print("Can\'t open configuration file.")
