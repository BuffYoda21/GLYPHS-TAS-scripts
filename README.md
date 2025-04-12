This is a collection of TAS (Tool Assisted Speedrun/Superplay) scripts to be used with the game Glyphs.

The game can be downloaded from here: https://vortex-bros.itch.io/glyphs  
The game will also be getting a Steam release in May 2025 here: https://store.steampowered.com/app/3616230/GLYPHS/

These scripts are not for traditional TAS given some quirks of the game (more details below) so they are designed to intergrate with a human user who must "tap in" when the TAS reaches a point it cannot do alone (It will automatically pause the game or open the map to let you know it needs help) 

These scripts were designed to function with version 1.6.5 of Glyphs. They can be used with other versions but there is no garuntee they will work. Significant lag or other preformance discrepencies may affect how the scripts preform. There is also an issue with how the game runs where it is not entirely consistent and the scripts will sometimes fail and get thrown off midway through.

These scripts are entirely just python scripts that send inputs to your keyboard at precise times to move through the game. There is no RNG prediction/control/manipulation involved so anything that has to do with RNG cannot be done by these scripts (ie boss fights). In other words, these scripts are only able to do parkour sections of the game and a user will have to tap in for any combat.

Due to an issue with the game's map scroll speed, different framerates affect how quickly the map scrolls and there is no consistent way to TAS using the map with these scripts so a human user must also tap in for these sections.

Instructions here are shown for Windows opperating systems but scripts should be compatable with any OS given the propper setup.


Prerequisites:
- Python installed (https://www.python.org/downloads/)
- The python keyboard package (on windows in command prompt type "py -m pip install keyboard")
- 

Running:
- Either open the script with python from file explorer or (recomended) in windows command line type (py path/to/your/script.py).
- Additional instructions on how to opperate the script will be shown in the command line.
