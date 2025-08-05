import os
import shutil
from SteamPathFinder import get_steam_path, get_app_path, get_game_path

satisfactory_path = get_game_path(get_steam_path(), '526870', 'Satisfactory')
if not os.path.exists(satisfactory_path):
    print("Satisfactory not found: " + satisfactory_path)
    exit(-1)
mods_folder = os.path.join(satisfactory_path, 'FactoryGame/Mods')
if not os.path.exists(mods_folder):
    print("Satisfactory SMM mod folder not found: " + mods_folder)
    exit(-1)

mod = os.path.join(mods_folder, 'DAlternativeBalance')
if os.path.exists(mod):
    print('Reinstalling...')
    shutil.rmtree(mod)

shutil.copytree('src', mod)