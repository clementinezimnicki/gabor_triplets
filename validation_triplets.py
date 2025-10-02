import os
import random
import json

# Path to your PNG folder
img_folder = "img"

# Get all gabor PNGs (including _255.png and _155.png)
all_images = [
    os.path.join(img_folder, f)
    for f in os.listdir(img_folder)
    if f.endswith(".png") and f.startswith("gabor")
]

# Sanity check
if len(all_images) < 3:
    raise ValueError("Not enough images to create trials (need at least 3).")

# Function to check if a new trial is a duplicate
def is_duplicate(trial, trials_list):
    for t in trials_list:
        if (
            t['head'] == trial['head'] and
            {t['choice_1'], t['choice_2']} == {trial['choice_1'], trial['choice_2']}
        ):
            return True
    return False

# Generate 60 unique trials
num_trials = 60
trials = []
attempts = 0
max_attempts = 10000

while len(trials) < num_trials and attempts < max_attempts:
    head = random.choice(all_images)
    choices = random.sample([img for img in all_images if img != head], 2)

    trial = {
        "head": head,
        "choice_1": choices[0],
        "choice_2": choices[1]
    }

    if not is_duplicate(trial, trials):
        trials.append(trial)

    attempts += 1

if len(trials) < num_trials:
    print(f"Only generated {len(trials)} unique trials after {max_attempts} attempts.")
else:
    print("60 unique trials generated.")

# Save to JSON
with open("validation_trials.json", "w") as f:
    json.dump(trials, f, indent=2)

print("Saved to 'validation_trials.json'")