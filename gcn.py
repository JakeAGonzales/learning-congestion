import os
import pickle

def load_pickle(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

def load_pickle_files(folder_path):
    env_data = None
    problem_data = []
    solution_data = []

    # List all files in the folder
    files = os.listdir(folder_path)

    # Loop through each file
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        # Skip if it's not a file
        if not os.path.isfile(file_path):
            continue

        if file_name == 'env.pickle':
            env_data = load_pickle(file_path)
        elif file_name.startswith('problem_') and file_name.endswith('.pickle'):
            problem_data.append(load_pickle(file_path))
        elif file_name.startswith('solution_') and file_name.endswith('.pickle'):
            solution_data.append(load_pickle(file_path))

    return env_data, problem_data, solution_data


data_dir = '/Users/jakegonzales/Documents/Amazon/code/mapf/data/train'
folders = os.listdir(data_dir)

all_folders_data = []
for folder in folders:
    folder_path = os.path.join(data_dir, folder)

    # Skip non-directory entries
    if not os.path.isdir(folder_path):
        continue

    folder_data = load_pickle_files(folder_path)
    all_folders_data.append(folder_data)


#data_folders = [data_dir + '/fold1', data_dir + '/fold2', data_dir + '/fold3']
