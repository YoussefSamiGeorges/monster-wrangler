# Monster Wrangler

A fast-paced 2D monster catching game built with Pygame where you play as a knight who must catch specific colored monsters while avoiding the others.


![image](https://github.com/user-attachments/assets/fa0f0cbb-fb37-4b9c-a037-e2a329ef40df)

![image](https://github.com/user-attachments/assets/ea5db031-35de-4966-93af-f1925b443f83)


## 🎮 Game Overview

Monster Wrangler is an arcade-style game where players control a knight character who must catch specific colored monsters indicated at the top of the screen. The game gets progressively more difficult with each round as more monsters appear. Be careful! Catching the wrong monster will cost you a life.

## 🔧 Requirements

- Python 3.x
- Pygame

## 📥 Installation

1. Clone the repository:
   ```
   git clone https://github.com/[your-username]/monster-wrangler.git
   ```

2. Navigate to the project directory:
   ```
   cd monster-wrangler
   ```

3. Install Pygame (if not already installed):
   ```
   pip install pygame
   ```

## 🚀 How to Play

1. Run the game:
   ```
   python main.py
   ```

2. Controls:
   - Arrow keys: Move the knight
   - Space: Use warp ability (teleports you to safety)
   - Space: Start new game (when on title screen or game over screen)

3. Gameplay:
   - Look at the "Current Catch" display to see which monster type to catch
   - Control your knight to touch the correct monster
   - Avoid touching the wrong monsters
   - Each round gets harder with more monsters
   - You have limited warps and lives, use them wisely!

## ⚙️ Game Mechanics

- **Scoring**: 100 points × current round number for each correctly caught monster
- **Lives**: Start with 5 lives, lose one when catching the wrong monster
- **Warps**: Start with 3 warps, use them to escape tight situations
- **Rounds**: Each round has more monsters than the previous one
- **Game Over**: Occurs when all lives are lost

## 🎨 Assets

- Custom font: Abrushow.ttf
- Monster sprites (blue_monster.png, yellow_monster.png, green_monster.png, purple_monster.png)
- Knight sprite (knight.png)

## 🔍 Code Structure

The game is built with Pygame and uses a class-based structure:

- `Monster` class: Manages monster behavior and movement
- `Player` class: Handles player input and movement
- `game()` function: Controls game flow and logic
- Main loop: Handles the title screen and game initialization
