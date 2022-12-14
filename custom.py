import sys
import pre_commit
print("Hello from custom.py")  # Stdout only printed when Failed
try:
    1 / 0
except Exception as e:
    sys.exit(e)
    print("Hello from custom.py v Hello from custom.py Hello from custom.py Hello from custom.py Hello from custom.py Hello from custom.py Hello from custom.py")