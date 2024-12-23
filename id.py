import requests
import xml.etree.ElementTree as ET

def scrape_steam_profile(steam_id):
    url = f"https://steamcommunity.com/id/{steam_id}/games?xml=1"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
        return
    
    root = ET.fromstring(response.text)
    
    steam_id64 = root.find('steamID64').text
    steam_id = root.find('steamID').text
    games = []
    app_ids = []
    
    for game in root.findall('.//game'):
        app_id = game.find('appID').text
        name = game.find('name').text
        
        hours_on_record = game.find('hoursOnRecord')
        if hours_on_record is not None:
            hours_on_record = hours_on_record.text
        else:
            hours_on_record = "N/A"
        
        games.append({
            'name': name,
            'app_id': app_id,
            'hours_on_record': hours_on_record
        })
        
        app_ids.append(int(app_id))
    
    print(f"Steam Games Dumper")
    print(f"Made by Cr0mb\n")
    print(f"Steam ID: {steam_id} (SteamID64: {steam_id64})")
    print(f"Total number of games owned: {len(games)}\n\n")
    
    games.sort(key=lambda game: game['name'])
    
    for game in games:
        print(f"Game: {game['name']} | App ID: {game['app_id']} | Hours on Record: {game['hours_on_record']}")
    
    app_ids.sort()
    
    print("\nList of App IDs from Least to Greatest:")
    print(", ".join(str(app_id) for app_id in app_ids))

steam_id = "Cr0mbs_Space"
scrape_steam_profile(steam_id)
