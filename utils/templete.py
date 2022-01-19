import io
import sys
import time
_INPUT = """\
2
1 2 3
aaa
"""
StartTime = time.time()
sys.stdin = io.StringIO(_INPUT)
#____________________________________________

#____________________________________________
print ("[Sec]"+str(time.time() - StartTime))