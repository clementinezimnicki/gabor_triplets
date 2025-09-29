import os
import json

# Set the folder where your PNGs are located
folder_path = "img"

# List all .png files in the folder
imgGabor = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.png')]

# Optionally sort the files (if they follow a numerical order)
imgGabor.sort()

# Save the list to a JSON file
with open("imgGabor.json", "w") as json_file:
    json.dump({"imgGabor": imgGabor}, json_file, indent=4)