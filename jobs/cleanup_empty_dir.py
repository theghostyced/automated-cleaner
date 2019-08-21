from datetime import datetime
myFile = open('job.txt', 'a') 
myFile.write('\nAccessed on ' + str(datetime.now()))