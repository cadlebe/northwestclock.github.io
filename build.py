import os.path
import subprocess

app_name = "northwest-clock"
version = "0_2_6"
directory_name = app_name + "-" + version
dist_path = "dist/" + directory_name
work_path = "build/" + directory_name

print(work_path)

if os.path.isdir('dist/nwclock-0_2_6'):
    print("Version exists!")
else:
    subprocess.Popen(['pyinstaller', 'src/clock.py',
                      '--add-data=LICENSE:.',
                      '--add-data=README.md:.',
                      '--add-data=northwest-clock.service:.',
                      '--distpath=' + dist_path,
                      '--workpath=' + work_path,
                      '--clean',
                      '--name=' + app_name])
