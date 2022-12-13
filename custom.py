import sys
print("Hello from custom.py")  # Stdout only printed when Failed
try:
    1 / 0
except Exception as e:
    sys.exit(e)