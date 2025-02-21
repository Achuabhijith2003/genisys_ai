import core
import time



def main():
    core.speaker.speak("Genisys is Starting")
    time.sleep(4)
    core.speaker.speak("Pleses wait for a moment")
    while True:
        state,command= core.listener.listen()
        if state:
            print(command)
            if command == "exit":
                core.speaker.speak("exiting")
                break
            else:
                result = core.ai.agent(prompt=command)
                print(result)
                core.speaker.speak(result)
        else:
            print(command)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Programe Terminated")
        
        