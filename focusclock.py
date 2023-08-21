import time
import winsound

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up! Take a break.")
    frequency = 1000  # Frequency of the beep sound in Hertz
    duration = 2000   # Duration of the beep sound in milliseconds
    winsound.Beep(frequency, duration)

if __name__ == "__main__":
    focus_time = int(input("Enter focus time in minutes: "))
    focus_timer(focus_time)
