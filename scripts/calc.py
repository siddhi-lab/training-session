import sys

cap_obatined = sys.argv[1]

print("cap obtained in bytes:", cap_obatined)

cap_GB = int(cap_obatined * 1e-9)

print("cap in GB:",  cap_GB)
