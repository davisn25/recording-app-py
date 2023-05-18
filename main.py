import os

directories = os.listdir('recordings')

def show_directories(dirs):
    index = 1
    for d in dirs:
        print(str(index) + ". " + d)
        index += 1
    print("")

print("Welcome to the Recordings program\n"
      "Open directory")
show_directories(directories)
select_directory = input("Select directory ")
selected_directory = (directories[int(select_directory) - 1])
print(selected_directory + " selected")

recordings_path = 'recordings/' + str(selected_directory) + "/"
recordings = os.listdir(recordings_path)
if not recordings:
    print("Nothing here!")
else:
    print("Recordings")
    show_directories(os.listdir(recordings_path))

action = input("_")

command = "".join([action[i] for i in range(0, action.index(" "))])
file = "".join(action[i] for i in range(action.index(" ") +1, len(action)))


try:
    if command == "rm" or command == "remove":
        os.remove(recordings_path + file)
    elif command == "record":
        os.system("arecord --format=cd " + recordings_path + "file.wav")
    elif command == "cd":
        recordings_path = file
    elif command == "play":
        os.system("play " + file)
    else:
        print("That's not a command")
except FileNotFoundError or NotADirectoryError:
    print("File not found")

print(recordings_path)