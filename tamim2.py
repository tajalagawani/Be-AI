
            settings.html

# Python Script 

import os

if not os.path.exists('myproject'):
    os.mkdir('myproject')

os.chdir('myproject')

# create the sub-directories
os.mkdir('static')
os.mkdir('templates')

# create files for the root directory
with open('main.py', 'w') as f:
    f.write('# main.py')

with open('config.py', 'w') as f:
    f.write('# config.py')

with open('database.py', 'w') as f:
    f.write('# database.py')

# create files in 'static' directory
os.chdir('static')

with open('styles.css', 'w') as f:
    f.write('/* styles.css */')

with open('main.js', 'w') as f:
    f.write('// main.js')

# create files in 'templates' directory
os.chdir('../templates')

with open('index.html', 'w') as f:
    f.write('<!-- index.html -->')

with open('login.html', 'w') as f:
    f.write('<!-- login.html -->')

with open('register.html', 'w') as f:
    f.write('<!-- register.html -->')

with open('profile.html', 'w') as f:
    f.write('<!-- profile.html -->')

with open('feed.html', 'w') as f:
    f.write('<!-- feed.html -->')

with open('post.html', 'w') as f:
    f.write('<!-- post.html -->')

with open('settings.html', 'w') as f:
    f.write('<!-- settings.html -->')