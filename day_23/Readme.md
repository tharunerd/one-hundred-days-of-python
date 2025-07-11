
# 🐢 Turtle Crossing Game

Inspired by the classic game **Frogger**, the goal is to guide a turtle across a busy road while avoiding fast-moving cars. The game gets more challenging with each level.

---

## 📂 Project Structure

```

turtle-crossing/
│
├── main.py           # Game loop and core logic
├── player.py         # Player (turtle) class and movement
├── car\_manager.py    # Cars: creation, movement, and difficulty scaling
├── scoreboard.py     # Score/level display and game over message

````

---

## ✅ Tasks Breakdown

### 1. 🎮 Screen Setup
- Created a `Screen` object with:
  - Size: 600×600
  - Background color: white
  - Title: "Turtle Crossing"
- Used `screen.tracer(0)` for manual screen refresh control

---

### 2. 🐢 Player Class (`player.py`)
- Inherits from `turtle.Turtle`
- Represents the user-controlled turtle
- Tasks:
  - Initialized at the bottom center of the screen
  - Moves up on pressing the **Up** key
  - Detects if the turtle has successfully crossed to the top
  - Resets to start position after level completion

---

### 3. 🚗 Car Manager (`car_manager.py`)
- Manages all the cars in the game
- Tasks:
  - Randomly generates cars from the right side of the screen
  - Cars move leftward across the screen
  - Cars appear at random y-positions
  - Detects collision with the player
  - Increases speed as levels increase

---

### 4. 📈 Scoreboard (`scoreboard.py`)
- Tracks and displays the current level
- Tasks:
  - Displays "Level: X" at the top-left corner
  - Increments level when the turtle reaches the finish line
  - Displays "GAME OVER" when the turtle hits a car

---

### 5. 🔁 Game Loop (`main.py`)
- Runs the core game logic
- Tasks:
  - Calls `screen.update()` to refresh screen
  - Calls `time.sleep()` to control game speed
  - Continuously creates and moves cars
  - Listens for user input to move the player
  - Detects:
    - Collision between turtle and car → ends game
    - Turtle reaching top → resets position, increases level and car speed

---

## 🧾 How to Run

### Requirements
- Python 3.x installed  
(Download: https://www.python.org/downloads/)

### Instructions
```bash
cd turtle-crossing-game
python main.py
````

> Press the **Up Arrow** key to move the turtle.

---

## 🚀 Future Ideas

* Add lives or retries
* Track and save high score
* Add sound effects
* Add animation or smoother car transitions

---
---

Feel free to star ⭐ the repo, fork it, or suggest improvements!

```
