import datetime

start = datetime.datetime.now()
input("Press enter to stop.")
stop = datetime.datetime.now()
result = (stop - start).total_seconds()

print(result)
