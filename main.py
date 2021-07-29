from LogExplorer import LogExplorerApp
import json, os

config_filename = './cfg.json'

if __name__ == '__main__':

    if os.path.exists(config_filename):
        with open(config_filename) as f:
            config = json.load(f)
        app = LogExplorerApp(config)
        app.mainloop()
    else:
        raise FileNotFoundError("configuration file not found!")
