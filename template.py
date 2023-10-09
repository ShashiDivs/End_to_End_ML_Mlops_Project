import os,sys
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(messagse)s:')


projec_name = "mlproject"



list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{projec_name}/components/__init__.py",
    f"src/{projec_name}/utlis/__init__.py",
    f"src/{projec_name}/utils/common.py",
    f"src/{projec_name}/config/__init__.py",
    f"src/{projec_name}/config/configuration.py",
    f"src/{projec_name}/pipeline/__init__.py",
    f"src/{projec_name}/entity/__init__.py",
    f"src/{projec_name}/entity/config_entity.py",
    f"src/{projec_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w"):
            pass
            logging.info(f"creating empty file :{filepath}")

    else:
        logging.info(f"{filename} is already exists")



























