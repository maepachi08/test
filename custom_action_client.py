import sys
sys.path.append("./lib/")
import aws_familiar 

file   = 'action.json'
object = aws_familiar.CustomAction(file)

if object.is_exists():
    print('CustomAction: found.')

else:
    print('CustomAction: not found.')
    object.create()
    

