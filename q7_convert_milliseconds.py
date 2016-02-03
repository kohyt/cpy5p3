# q7_convert_milliseconds.py
# 1s = 1000ms

def convert_ms(n):
    seconds = int(n / 1000)
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    print("{0}:{1}:{2}".format(hours, minutes, seconds))

# get input
n = float(input("Enter milliseconds:"))
# display results
convert_ms(n)
