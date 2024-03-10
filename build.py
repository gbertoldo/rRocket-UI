import os
import shutil

"""
cmd='pyinstaller'
  +' --clean' # Removes previous compilation
  +' --onedir' # Puts the executable and libs in one directory
  #+' --onefile' # Puts the executable and libs in a single file
  +' --windowed' # Windowed application
  +' --icon="./fig/guiduino.ico"' # Adds the application icon
  +' --add-data "./fig/*.png;fig/"' # Adds the figures to the executable
  +' --name guiduino' # Names the executable
  +' main.py' # Start file

  """

shutil.copytree('sim', 'dist/sim', dirs_exist_ok=True) 

cmd='pyinstaller --clean --onefile --windowed --icon="./fig/rRocket.ico" --add-data "./fig/*.png;fig/" --add-data "./fig/*.ico;fig/" --name rRocketUI main.py'

os.system(cmd)

