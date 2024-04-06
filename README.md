# RapidFire-Cheat-Detection
This Python tool, powered by [demoparser](https://github.com/LaihoE/demoparser), is designed to detect rapid fire cheats in Counter-Strike 2 demo files.

### Usage
1. Install demoparser: `pip install demoparser2`
2. Download [detect_cheaters.py](https://github.com/arber-hakaj/RapidFire-Cheat-Detection/blob/main/detect_cheaters.py)
3. Execute the script by providing the path to the CS2 demo file: `python detect_cheaters.py <demo_file_path>`

Example:  
```bash
$ python detect_cheaters.py demo1.dem 
Cheaters: [('76561198891443722', 'Double G Grandson btc'), ('76561198361014165', 'Kanye West Fan')]
