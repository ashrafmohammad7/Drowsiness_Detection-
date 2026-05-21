import os
import shutil
import random

SOURCE_FOLDER = "mrlEyes_2018_01"
DEST_FOLDER = "dataset"

MAX_IMAGES_PER_CLASS = 1000
TRAIN_RATIO = 0.8

open_images = []
closed_images = []

# Create required folders
for folder in ["train/open", "train/closed", "test/open", "test/closed"]:
    os.makedirs(os.path.join(DEST_FOLDER, folder), exist_ok=True)

# Walk through all subfolders
for root, dirs, files in os.walk(SOURCE_FOLDER):
    for file in files:
        if file.endswith(".png"):
            full_path = os.path.join(root, file)

            if "_1_" in file:   # open eye
                open_images.append(full_path)
            elif "_0_" in file: # closed eye
                closed_images.append(full_path)

# Pick only 20 each
open_images = random.sample(open_images, min(MAX_IMAGES_PER_CLASS, len(open_images)))
closed_images = random.sample(closed_images, min(MAX_IMAGES_PER_CLASS, len(closed_images)))

def split_and_copy(images, label):
    split_index = int(len(images) * TRAIN_RATIO)

    train_files = images[:split_index]
    test_files = images[split_index:]

    for file in train_files:
        shutil.copy(file, os.path.join(DEST_FOLDER, "train", label))

    for file in test_files:
        shutil.copy(file, os.path.join(DEST_FOLDER, "test", label))

split_and_copy(open_images, "open")
split_and_copy(closed_images, "closed")

print("Dataset prepared successfully!")