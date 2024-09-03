project('wayland-solver')

# Import Modules
gnome = import('gnome')
i18n = import('i18n')
python = import('python')

# Module objects
py_installation = python.find_installation('python3')

# Make sure Python is installed and found
if not py_installation.found()
    error('No valid python3 binary found')
endif

# Python 3.7 is needed for postponed evalution of annotations
if not py_installation.language_version().version_compare('>= 3.7')
  error('Python 3.7 or newer is required.')
endif

APPLICATION_ID = 'work.idev2580dev.waylandsolver'
PROJECT_RDNN_NAME = APPLICATION_ID


subdir('data')