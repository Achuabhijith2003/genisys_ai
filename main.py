import core
import time
from config import config

def main():
    core.speaker.speak("Genisys is Starting")
    time.sleep(4)
    core.speaker.speak("Please wait for a moment")
    
    sleeping = False  # AI sleep mode flag
    
    while True:
        state, command = core.listener.listen()
        
        if sleeping:
            print(f"[Sleeping] Received command: {command}")
            if command == "hey wake up":
                core.speaker.speak("Waking up")
                config.SLEEP_COUNT = 0  # Reset sleep count
                sleeping = False
            else:
                print("[Sleeping] Ignoring input...")
            continue  # Skip the rest of the loop when in sleep mode
        
        if state:
            print(f"[~] input > {command}")
            if command == "exit":
                core.speaker.speak("Exiting")
                break
            else:
                result = core.ai.agent(prompt=command)
                print(f"[~] output > {result}")
                core.speaker.speak(result)
        else:
            if config.SLEEP_COUNT < config.SLEEP_N:
                print(command)
                core.speaker.speak(command)
                config.SLEEP_COUNT += 1
            
            if config.SLEEP_COUNT >= config.SLEEP_N:
                core.speaker.speak("Entering sleep mode. Say 'hey wake up' to continue.")
                print(f"[!] Entering sleep mode. Say 'hey wake up' to continue.")
                sleeping = True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program Terminated")
