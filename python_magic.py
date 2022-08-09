import schedule
import time
import shutil


def job():
    print('Copying file for Backup')
    src = 'C:/Users/MoTech/Desktop/Pelcon/backup.txt'
    dst = 'C:/Users/MoTech/Desktop/'
    shutil.copy2(src, dst)
   

schedule.every(5).seconds.do(job)


while True:
    schedule.run_pending()
    #time.sleep(1)

