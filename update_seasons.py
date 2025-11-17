import json
import glob

# Additional season mappings
additional_seasons = {
    # BHETA-DECIMA
    "IMP-SCT": "BHETA-DECIMA",  # Scout Squad
    "CHAOS-NC": "BHETA-DECIMA",  # Nemesis Claw
    "AEL-MND": "BHETA-DECIMA",  # Mandrakes
    "TYR-BBRO": "BHETA-DECIMA",  # Brood Brothers
    "VOT-HKY": "BHETA-DECIMA",  # Hernkyn Yaegirs
    
    # Volkus
    "IMP-TEMPAQ": "Volkus",  # Tempestus Aquilons
    "TAU-VESP": "Volkus",  # Vespid Stingwings
    "CHAOS-PM": "Volkus",  # Plague Marines
    "IMP-AOD": "Volkus",  # Angels Of Death
    "IMP-RAT": "Volkus",  # Ratlings
    "ORK-WK": "Volkus",  # Wrecka Krew
    "CHAOS-GORE": "Volkus",  # Goremongers
    "IMP-SANC": "Volkus",  # Sanctifiers
    "IMP-BC": "Volkus",  # Battleclade
    "TYR-RAV": "Volkus",  # Raveners
    
    # Tomb world
    "IMP-DW": "Tomb world",  # Deathwatch
    "NEC-CAN": "Tomb world",  # Canoptek Circle
}

files = glob.glob('en/teams/*.json') + glob.glob('es/teams/*.json')

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    killteam_id = data.get('killteamId')
    
    if killteam_id in additional_seasons:
        # Update the season value
        data['season'] = additional_seasons[killteam_id]
        
        # Write back with proper formatting
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

print(f'Updated seasons for {len(additional_seasons)} teams in {len(files)} files')

