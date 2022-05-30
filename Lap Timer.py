import time

starttime=time.time()
lasttime=starttime
lapnum=1

print("Press ENTER key to count laps.\nPress CTRL+C Key combination to Stop")

try:
    while True:
        input()
        laptime=round((time.time() - lasttime), 2)

        totaltime=round((time.time() - starttime), 2)

        print("Lap No."+str(lapnum))
        print("Total time: "+str(totaltime))
        print("Lap time: "+str(laptime))

        print("*"*20)

        lasttime=time.time()
        lapnum+=1

except KeyboardInterrupt:
    print("Done")
