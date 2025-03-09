import time
print("time():", time.time())

lt = time.localtime()
print("localtime():", f"{lt[2]:02d}.{lt[1]:02d}.{lt[0]} "
                      f"{lt[3]:02d}:{lt[4]:02d}:{lt[5]:02d}")
s = 1_720_000_000
lt = time.localtime(s)
print("localtime():", f"{lt[2]:02d}.{lt[1]:02d}.{lt[0]} "
                      f"{lt[3]:02d}:{lt[4]:02d}:{lt[5]:02d}")

tu = 2024, 8, 24, 12, 35, 20, 0, 0, 0

print("strftime():", time.strftime("%d.%m.%Y %H:%M:%S"))
print("strftime():", time.strftime("%d.%m.%Y %H:%M:%S", tu))
print("strftime():", time.strftime("%d.%m.%Y %H:%M:%S", lt))

print("mktime():", time.mktime(tu))
print("mktime():", time.mktime(lt))
