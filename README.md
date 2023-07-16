# Analyze_Cv_Dataset

# Dataset requirements

### Data need to be in this format

Dir: ex: /home/name/data

## Include the train and test data.
train: Dir/train/images/ --> include the jpg images.
train: Dir/train/labels/ --> include annotation txt files.

val: Dir/val/images/ --> Include the jpg images.
val: Dir/val/labels/ --> Include the  txt files.

classes: Dir/classes.txt

# Install the data_gradients
> pip install data_gradients

### Using this repo you can analyze your image dataset

> git clone https://github.com/harikrishna7696/Analyze_Cv_Dataset.git

#### Run the data_set_analyzer.py
> python3 dataset_set_analyzer.py --root_dir 'directory where your data available' --title 'Saving the report in Dir'


# Note: Feel free to change the code as you need.
