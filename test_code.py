
import sys
a = 10
try:
 if a == 10:
    print('test passed')
 else:
    raise ValueError
except ValueError:
    print('test case failed')
    sys.exit(420)
