
import sys
a = 11
try:
 if a == 10:
    print('test passed')
 else:
    raise ValueError
except ValueError:
    print('test case failed')
    sys.exit(420)
