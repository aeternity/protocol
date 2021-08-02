import os
import shutil

def pre_build(**kwargs):
  source_folders = ['channels', 'consensus', 'contracts', 'generalized_accounts', 'mining', 'node', 'oracles', 'sync']
  dest = '00_mkdocs/docs_root'
  shutil.copy('README.md', dest)
  shutil.copy('AENS.md', dest)
  shutil.copy('GOSSIP.md', dest)
  shutil.copy('serializations.md', dest)
  for source in source_folders:
    to_path = dest + "/" + source
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(source, to_path)
