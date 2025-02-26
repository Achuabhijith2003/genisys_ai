import core
import time
from config import config

def main():
    core.speaker.speak("Genisys is Starting")
    time.sleep(4)
    speaker.speak("Please wait for a moment")
    
    sleeping = False  # AI sleep mode flag
    while True:
        state, command = core.listener.listen()
        
        if sleeping:
            print(f"[Sleeping] Received command: {command}")
            if command.lower() == "wake ai":
                speaker.speak("Waking up")
                config.SLEEP_COUNT = 0  # Reset sleep count
                sleeping = False
            continue  # Skip processing when sleeping
        
        if state:
            print(f"[~] input > {command}")
            
            result = core.ai.agent(prompt=command)
            
            if result.startswith("cmd: "):
                cmd2 = result[5:].strip()

                if cmd2 == "exit":
                    print(f"[~] output > Exiting")
                    speaker.speak("Exiting")
                    break

                elif "time" in cmd2:
                    ti = core.real_data.date_time_info()
                    print(f"[~] output > {ti}")
                    speaker.speak(ti)

                elif "weather" in cmd2:
                    location = cmd2.replace("weather ", "").strip()
                    result = core.real_data.get_weather(location=location)
                    print(f"[~] output > {result}")
                    speaker.speak(result)

            else:
                print(f"[~] output > {result}")
                speaker.speak(result)

        else:
            if config.SLEEP_COUNT < config.SLEEP_N:
                print(command)
                speaker.speak(command)
                config.SLEEP_COUNT += 1
            
            if config.SLEEP_COUNT >= config.SLEEP_N:
                speaker.speak("Entering sleep mode. Say 'wake ai' to continue.")
                print(f"[!] Entering sleep mode. Say 'wake ai' to continue.")
                sleeping = True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program Terminated")
