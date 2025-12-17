import pandas as pd
import numpy as np
import os

class VideoGameDatabase:
    """Generate and manage video game database"""
    
    def __init__(self, data_dir='data'):
        self.data_dir = data_dir
        self.csv_path = os.path.join(data_dir, 'video_games.csv')
        
        # Ensure data directory exists
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def generate_database(self):
        """Generate video game dataset and save to CSV"""
        np.random.seed(42)
        
        # Real game names from the industry
        real_game_names = [
            'The Legend of Zelda: Breath of the Wild', 'Super Mario Odyssey', 'Mario Kart 8 Deluxe',
            'Animal Crossing: New Horizons', 'Splatoon 3', 'Elden Ring', 'Baldur\'s Gate 3',
            'Cyberpunk 2077', 'The Witcher 3', 'Red Dead Redemption 2', 'Grand Theft Auto V',
            'Minecraft', 'Fortnite', 'Call of Duty: Modern Warfare', 'Valorant',
            'Counter-Strike 2', 'Dota 2', 'League of Legends', 'Overwatch 2', 'Apex Legends',
            'Halo Infinite', 'Xbox Game Pass', 'Starfield', 'Palworld', 'Dragon\'s Dogma 2',
            'Street Fighter 6', 'Final Fantasy XVI', 'Final Fantasy VII Remake', 'Kingdom Hearts III',
            'Monster Hunter: World', 'Dark Souls 3', 'Bloodborne', 'Sekiro: Shadows Die Twice',
            'Horizon Zero Dawn', 'God of War Ragnarök', 'Spider-Man 2', 'Ghost of Tsushima',
            'The Last of Us Part II', 'Uncharted 4', 'Death Stranding', 'Cyberpunk 2077',
            'Starfield', 'Fallout 4', 'Skyrim', 'Oblivion', 'Morrowind',
            'Team Fortress 2', 'Portal 2', 'Half-Life 3', 'Left 4 Dead 2', 'Dying Light 2',
            'Resident Evil 4 Remake', 'Silent Hill 2 Remake', 'Outlast 3', 'Amnesia Collection',
            'Subnautica', 'No Man\'s Sky', 'Star Citizen', 'Kerbal Space Program', 'Microsoft Flight Sim',
            'NASCAR Heat 5', 'F1 24', 'Gran Turismo 7', 'Forza Motorsport 8', 'Need for Speed Unbound',
            'FIFA 24', 'NBA 2K24', 'Madden NFL 24', 'WWE 2K24', 'PGA Tour 2K24',
            'Tetris Effect', 'Puyo Puyo Tetris', 'Bejeweled 3', 'Candy Crush Saga', 'Portal Knights',
            'The Sims 4', 'Cities Skylines 2', 'Planet Coaster 2', 'Two Point Hospital', 'Farming Simulator 23',
            'Deus Ex: Mankind Divided', 'Splinter Cell Remake', 'Hitman 3', 'Dishonored 2', 'Prey',
            'Outer Wilds', 'A Short Hike', 'Unpacking', 'Return of the Obra Dinn', 'Gris',
            'Hollow Knight', 'Dead Cells', 'Risk of Rain 2', 'Hades', 'Celeste',
            'Cuphead', 'Spiritfarer', 'Disco Elysium', 'Persona 5 Royal', 'Fire Emblem: Three Houses',
            'Diablo IV', 'Path of Exile 2', 'Lost Ark', 'World of Warcraft', 'Final Fantasy XIV',
            'Elder Scrolls Online', 'Guild Wars 2', 'New World', 'Albion Online', 'RuneScape 3',
            'Pokémon Scarlet & Violet', 'Pokémon Legends Arceus', 'Pokémon Sword & Shield', 'Pokémon Legends Legends',
            'Metroid Prime Remastered', 'Metroid Dread', 'Castlevania: Nocturne', 'Mega Man 11', 'Contra: Operation Galuga',
            'Starcraft II', 'Total War: Warhammer III', 'Age of Empires IV', 'Company of Heroes 3', 'They Are Billions',
            'XCOM 2', 'Civilization VI', 'Crusader Kings III', 'Stellaris', 'Europa Universalis IV',
            'Warcraft III Reforged', 'Command & Conquer Remastered', 'Red Alert 4', 'Tiberium Alliances', 'Act of War',
            'Death\'s Door', 'Salt and Sanctuary', 'Blasphemous', 'Limbo', 'Inside',
            'Journey', 'Abzu', 'Flower', 'Kena: Bridge of Spirits', 'A Plague Tale',
            'Heavy Rain', 'Detroit: Become Human', 'Quantum Break', 'Alan Wake', 'Control',
            'Psychonauts 2', 'Ghostrunner', 'Slime Rancher', 'Grounded', 'No Man\'s Sky',
            'Stardew Valley', 'Slime Rancher 2', 'Core Keeper', 'Roots of Pacha', 'Everspace 2',
            'Star Wars Jedi: Survivor', 'Star Wars Jedi: Fallen Order', 'Star Wars Battlefront 2', 'Star Wars: The Old Republic',
            'Warhammer 40K Darktide', 'Warhammer Vermintide 2', 'Warhammer 40K Space Marine 2', 'Warhammer Age of Sigmar',
            'Back 4 Blood', 'Killing Floor 2', 'Deep Rock Galactic', 'Helldivers 2', 'Gunfire Reborn',
            'Sea of Thieves', 'Skull and Bones', 'Pirate101', 'Naval Action', 'Windbound',
            'It Takes Two', 'A Way Out', 'Overcooked 2', 'Moving Out', 'Unravel 2',
            'Jackbox Party Packs', 'Among Us', 'Fall Guys', 'Stumble Guys', 'Gartic Phone',
            'VRChat', 'Beat Saber', 'Half-Life Alyx', 'The Lab', 'Pavlov VR',
            'Silent Hill Village', 'Resident Evil 8', 'Evil Within 2', 'Alibi', 'Phasmophobia',
            'Inscryption', 'Slay the Spire', 'Monster Train', 'Hades II', 'Peglin',
            'Vampire Survivors', 'Magic Survival', 'Brotato', 'Halls of Torment', 'Eatventure',
            'Hi-Fi Rush', 'Crypt of the NecroDancer', 'Audica', 'Frets on Fire', 'Guitar Hero Live',
            'Rock Band 4', 'Just Dance 2024', 'Dance Central', 'Zumba Fitness', 'Ring Fit Adventure',
            'Switch Sports', 'Wii Sports Resort', 'Kinect Sports', 'PlayStation Move Sports', 'VR Sports',
            'Lies of P', 'Homunculus', 'Salt and Sacrifice', 'Furi', 'Crosscode',
            'ULTRAKILL', 'Dusk', 'Project Warlock', 'Ion Maiden', 'Prodeus',
            'Retro City Rampage', 'Hotline Miami', 'Papers Please', 'Return of the Obra Dinn', 'Outer Wilds',
            'Noita', 'Spelunky 2', 'Caveblazers', 'Juiced 2', 'OutRun 2',
            'Burnout Revenge', 'Burnout Paradise', 'Split Second', 'Motorstorm', 'Wipeout HD',
            'F-Zero GX', 'Ridge Racer', 'Initial D Arcade Stage', 'Daytona USA', 'Cruisin Exotica',
            'Transformers: Fall of Cybertron', 'LEGO Video Games Series', 'Marvel Spider-Man', 'DC Batman Series',
            'Sonic Adventure 2', 'Shadow the Hedgehog', 'Sonic Generations', 'Sonic Frontiers', 'Sonic Mania'
        ]
        
        genres = ['Action', 'RPG', 'Strategy', 'Sports', 'Shooter', 'Adventure', 
                  'Racing', 'Puzzle', 'Simulation', 'Indie', 'Horror', 'Fighting']
        platforms = ['PS5', 'Xbox Series X', 'Nintendo Switch', 'PC', 'PS4', 
                     'Xbox One', 'Mobile', 'VR', 'Steam Deck']
        publishers = ['Sony', 'Microsoft', 'Nintendo', 'Activision Blizzard', 
                      'EA Sports', 'Ubisoft', 'Take-Two', 'Rockstar Games',
                      'Bethesda', 'Epic Games', 'Square Enix', 'Capcom', 'Bandai Namco',
                      'Konami', 'Sega', 'CD Projekt Red', 'FromSoftware', 'Fromsoftware Bandai']
        
        num_games = 1000  # Increased to 1000 games
        
        # Ensure we have enough game names
        game_names = (real_game_names * ((num_games // len(real_game_names)) + 1))[:num_games]
        np.random.shuffle(game_names)
        
        data = {
            'Game_ID': range(1, num_games + 1),
            'Game_Name': game_names,
            'Genre': np.random.choice(genres, num_games),
            'Platform': np.random.choice(platforms, num_games),
            'Publisher': np.random.choice(publishers, num_games),
            'Release_Year': np.random.randint(2010, 2025, num_games),
            'Price_USD': np.random.uniform(5, 70, num_games),
            'Sales_Million': np.random.exponential(5, num_games) + 0.5,
            'Player_Count': np.random.randint(1000, 50000000, num_games),
            'Rating': np.random.uniform(1, 10, num_games),
            'Development_Cost_Million': np.random.uniform(1, 300, num_games),
            'Playtime_Hours': np.random.uniform(2, 200, num_games),
            'Metacritic_Score': np.random.uniform(20, 98, num_games),
            'Copies_Sold_Million': np.random.exponential(3, num_games) + 0.1,
            'Budget_Million': np.random.uniform(5, 250, num_games),
        }
        
        df = pd.DataFrame(data)
        df['Revenue_Million'] = df['Copies_Sold_Million'] * df['Price_USD']
        df['ROI_Percent'] = ((df['Revenue_Million'] - df['Development_Cost_Million']) 
                             / df['Development_Cost_Million'] * 100)
        df['Engagement_Score'] = (df['Rating'] * df['Player_Count'] / 1000000)
        df['Profitability_Grade'] = pd.cut(df['ROI_Percent'], 
                                           bins=[-np.inf, -50, 0, 50, 100, 500, np.inf],
                                           labels=['F', 'D', 'C', 'B', 'A', 'S'])
        
        # Save to CSV
        df.to_csv(self.csv_path, index=False)
        print(f"Database created: {self.csv_path}")
        print(f"Total records: {len(df)}")
        
        return df
    
    def load_database(self):
        """Load database from CSV file"""
        if not os.path.exists(self.csv_path):
            print("Database not found. Creating new database...")
            return self.generate_database()
        
        df = pd.read_csv(self.csv_path)
        print(f"Database loaded: {self.csv_path}")
        print(f"Total records: {len(df)}")
        return df
    
    def get_database_info(self):
        """Get database information"""
        df = self.load_database()
        
        info = f"""
DATABASE INFORMATION:
=====================================
Location: {self.csv_path}
Total Games: {len(df)}
Columns: {len(df.columns)}
File Size: {os.path.getsize(self.csv_path) / 1024:.2f} KB

COLUMN NAMES:
{', '.join(df.columns.tolist())}

STATISTICAL SUMMARY:
{df.describe()}
"""
        return info
