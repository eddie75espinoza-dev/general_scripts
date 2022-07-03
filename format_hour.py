import math
time = 9775

hours, rec = divmod(int(time),3600)

minutes = (time * 60) % 60

seconds = (time*3600) % 60

print("%d:%02d.%02d" % (hours, minutes, seconds))
print(rec)
print(str(int(math.floor(time))) + ':' + str(int((time%(math.floor(time)))*60)) + ':' + str(int(((time%(math.floor(time)))*60) % math.floor(((time%(math.floor(time)))*60))*60)))