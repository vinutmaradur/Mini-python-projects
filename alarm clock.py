from playsound import playsound
import time 

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elasped = 0
    print(CLEAR)
    while time_elasped < seconds:
        time.sleep(1)
        time_elasped += 1

        time_left = seconds - time_elasped
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in : {minutes_left:02d}:{seconds_left:02d}")
    playsound("alarm.mp3")


minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many minutes to wait: "))
total_seconds = minutes * 60 +seconds
alarm(total_seconds)
