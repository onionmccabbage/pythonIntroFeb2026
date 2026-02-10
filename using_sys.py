# Python knows about its environment, called 'sys' for system

import sys

print( sys.platform )
print( sys.version_info )

# We may add places to the path sp Python will also look there when importing
sys.path.append('D:/pythonIntroFeb2026/assets')

# we can check the places that Python will look when we import stuff
print( sys.path ) # sys.path is a list