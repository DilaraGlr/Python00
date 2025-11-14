import time

time_second = time.time()
temps_struct = time.localtime(time_second)
date = time.strftime("%b %d %Y", temps_struct)

print(f"Seconds since  January 1, 1970: {time_second:,.4f} or {time_second:.2e} in scientific notation")
print(date)