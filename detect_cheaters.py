import sys
from demoparser2 import DemoParser

# Parse the 'player_hurt' event
parser = DemoParser(sys.argv[1])
df_player_hurt = parser.parse_event("player_hurt")

# Parse player information
df_player = parser.parse_player_info()
players = {str(row["steamid"]): row["name"] for _, row in df_player.iterrows()}

# Weapon names and the weapon cycle time in ticks
weapons = {
    # snipers
    "awp": 70,
    "scar20": 16,
    "g3sg1": 16,
    "ssg08": 60,
    # rifles
    "ak47": 6,
    # pistols
    "usp_silencer": 10,
    "glock": 9,
    "p250": 9,
    "elite": 7,
    "fiveseven": 9,
    "deagle": 14,
    "revolver": 32,
}

cheaters = []

print(players.items())
# Detect potential cheaters
for attacker_steamid, attacker_name in players.items():
    found_cheater = False

    # Filter player_hurt events for the current attacker
    df = df_player_hurt[(df_player_hurt["attacker_steamid"] == attacker_steamid) & (df_player_hurt["weapon"].isin(weapons.keys()))]

    for weapon_name, weapon_tick_cycle in weapons.items():
        if found_cheater:
            break
        # Filter events for the current weapon
        weapon_df = df[df["weapon"] == weapon_name]
        weapon_df = weapon_df.reset_index()

        print(weapon_name)
        for index, row in weapon_df.iterrows():
            if index == len(weapon_df) - 1:
                break

            # Calculate ticks between shots
            tick_between_shots = weapon_df.iloc[index + 1]['tick'] - row['tick']

            # Check for Rapid Fire
            if 1 <= tick_between_shots < weapon_tick_cycle:
                found_cheater = True
                cheaters.append((attacker_steamid, attacker_name))
                break

print(f"Cheaters: {cheaters}")
