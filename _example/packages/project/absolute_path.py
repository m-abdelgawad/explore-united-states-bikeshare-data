import os


def get_abs_path():
    return os.path.abspath(__file__ + "/../../..")


if __name__ == "__main__":
    print(get_abs_path())
