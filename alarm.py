from datetime import datetime
import time
import os
 
# Set alarm time in HH:MM:SS format
alarm_time = input("Enter alarm time (HH:MM:SS): ")
 
print(f"Alarm set for {alarm_time}")
 
while True:
current_time = datetime.now().strftime("%H:%M:%S")
 
if current_time == alarm_time:
print("⏰ Alarm! Wake up!")
 
# Windows beep sound
for _ in range(5):
os.system("echo \a")
time.sleep(1)
 
break
 
time.sleep(1)
Windows version using winsound

For a louder alarm on Windows:

Python
from datetime import datetime
import time
import winsound
 
alarm_time = input("Enter alarm time (HH:MM:SS): ")
 
print(f"Alarm set for {alarm_time}")
 
while True:
current_time = datetime.now().strftime("%H:%M:%S")
 
if current_time == alarm_time:
print("⏰ Alarm!")
 
for _ in range(10):
winsound.Beep(1000, 1000) # 1000 Hz for 1 second
 
break
 
time.sleep(1)
