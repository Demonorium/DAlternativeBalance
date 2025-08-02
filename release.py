import os
import shutil
import zipfile

MOD_ID = 'DAlternativeBalance.zip'

if os.path.exists('build'):
    shutil.rmtree('build')
    
os.mkdir('build')
windows_dir = os.path.join('build', 'Windows')
windows_server_dir = os.path.join('build', 'WindowsServer')
linux_server_dir = os.path.join('build', 'LinuxServer')

shutil.copytree('src', windows_dir)
shutil.copytree('src', windows_server_dir)
shutil.copytree('src', linux_server_dir)

with zipfile.ZipFile(os.path.join('build', MOD_ID), 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk('src'):
        for file in files:
            file_path = os.path.join(root, file)
            
            zipf.write(file_path, os.path.relpath(file_path, 'src'))
        
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            zipf.write(dir_path, os.path.relpath(dir_path, 'src'))
