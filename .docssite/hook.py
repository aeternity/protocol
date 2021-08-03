import os
import shutil

def pre_build(**kwargs):
  source_folders = ['channels', 'consensus', 'contracts', 'generalized_accounts', 'node', 'oracles', 'sync']
  dest = 'docs'
  shutil.copy('../README.md', dest)
  shutil.copy('../AENS.md', dest)
  shutil.copy('../GOSSIP.md', dest)
  shutil.copy('../serializations.md', dest)
  shutil.copy('../STRATUM.md', dest)
  for source in source_folders:
    from_path = '../' + source
    to_path = dest + "/" + source
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)
