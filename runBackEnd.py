import average
import createMask
import time
import os, sys
init=time.time()
class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

with HiddenPrints():
    average.average()
    createMask.createMask()

print("Completed in {} seconds".format(round(time.time()-init)))