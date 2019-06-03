import os.path
import subprocess

app_name = "northwest-clock"
version = "v0_2_10"
directory_name = app_name + "-" + version
dist_path = "dist/" + directory_name
work_path = "build/" + directory_name

print(work_path)

if os.path.isdir(dist_path):
    print("Version exists!")
else:
    subprocess.Popen(['pyinstaller', 'src/clock.py',
                      '-F',
                      '--add-data=LICENSE:.',
                      '--add-data=README.md:.',
                      '--add-data=northwest-clock.service:.',
                      '--distpath=' + dist_path,
                      '--workpath=' + work_path,
                      '--clean',
                      '--name=' + app_name])
