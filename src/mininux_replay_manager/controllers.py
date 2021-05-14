import shutil, os


def move_replay(replay_data_path, user_data_path, replay_name):
    shutil.copyfile(os.path.join(replay_data_path, replay_name), os.path.join(user_data_path, "collect.vff"))


def rename_replay(replay_data_path, replay_name, new_replay_name):
    shutil.move(os.path.join(replay_data_path, replay_name), os.path.join(replay_data_path, new_replay_name))


def delete_replay(replay_data_path, replay_name):
    os.remove(os.path.join(replay_data_path, replay_name))
