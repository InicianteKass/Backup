import os
import zipfile
 
fantasy_zip = zipfile.ZipFile('LOG\LOGS.zip', 'w')
 
for folder, subfolders, files in os.walk('LOG'):
 
    for file in files:
        if file.endswith('.txt'):
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'LOG'), compress_type = zipfile.ZIP_DEFLATED)
 
fantasy_zip.close()