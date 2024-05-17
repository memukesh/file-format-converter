import sys
import os

print(os.environ.get("HOST"))
args= sys.argv
print(f'hello {args}')