import subprocess
subprocess.call(['python manage.py loaddata', 'locations'])
subprocess.call(['python manage.py loaddata', 'departments'])
subprocess.call(['python manage.py loaddata', 'categories'])
subprocess.call(['python manage.py loaddata', 'elements'])
subprocess.call(['python manage.py loaddata', 'computers'])
