#!/usr/bin/env python3

import json

def savefile(filepath, difftrack=None):
    """
    Function to save game files. Writes into filepath.
    :param filepath: file to save game data in
    :param difftrack: data to save in difftrack format
    :return: None
    """

    if not difftrack:
        print("Warning: no data given to save. Exitting.")

    with open(filepath, 'w', encoding='utf8') as f:
        f.write(json.dumps({'name': "$NAME",
                            'crates_x': 3,
                            'crates_y': 3,
                            'initial_color': "#000000",
                            'updates': difftrack},
                           indent=2, ensure_ascii=False))
    return
