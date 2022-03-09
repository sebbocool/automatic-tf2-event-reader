import os

# P-REC currently not supported

### Fill in before use
events = "" # Change this if your events file is not in your demos folder (default is to not change)
demos = r"C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\tf\demos" # Change if demos folder is at another path

### THIS WILL USE THE TEST FILES, REMOVE # FOR TESTING
#events = ""
#demos = "testdemos"

if events == "":
    event_path = demos + "\_events.txt"
else:
    event_path = events
events = open(event_path, "r")

done_demos = {}
count = 0
total_count = 0

for marks in events:
    try:
        if '"' in marks:
            # Hitta demo, ta ut namn och tick            
            print("Found tick on demo",marks)
            total_count += 1
            demo_name = marks[38:57]
            tick = marks[62:-2]
            print(demo_name,"nästa",tick)

            # Spara namn och tick
            if demo_name in done_demos.keys():
                done_demos[demo_name] = done_demos[demo_name] + "_" + tick
            else:
                done_demos[demo_name] = tick

    except FileNotFoundError:
        print("Demo on",demo_name,"not found. Maybe already checked or moved?")

# Byt namn på filer
for new_name in done_demos.keys():
    try:
        print("hej")
        print(demos + "\\" + new_name + ".dem", demos +"\\"+done_demos[new_name] + ".dem")
        print("hej")
        os.rename(demos + "\\" + new_name + ".dem", demos +"\\"+done_demos[new_name] + ".dem")
    except FileNotFoundError:
        print("RENAME: Demo on",new_name,"not found. Maybe already checked or moved?")

events.close()
