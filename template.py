import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s: %(message)s:]')
project_name =  "textSummarizer"
list_of_file = [
    ".github/workflows/.gitkeep"  , # will be used when we will do ci/cd deployment
    f"src/{project_name}/__init__.py", # constructer file
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py", 
    "research/trails.ipynb"

]

for filepath in list_of_file:
    filepath = Path(filepath) # neccasary because in linux we use / and in windows we use \ for path
                            # so to overcome these errors 
                            # path library will see the system first then create path as per system
    filedir,filename = os.path.split(filepath)                        
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating dir :{filedir} for the file {filename}")

    if(not os.path.exists(filepath) or os.path.getsize(filepath)==0): ## getsize is imp bcoz if size !=0 means there is a code in that file
                                                                    # if template.py runs it will create new file and code will be lost
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file : {filepath}")
        
    else:
        logging.info(f"{filename} already exists")
