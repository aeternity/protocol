import shutil

def pre_build(**kwargs):
  shutil.copy('./README.md', './specification')
