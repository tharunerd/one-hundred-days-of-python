actions to consider :

1. move the turtle with keypress
2. create and move the cars
3. detect the collision of turtle with car
4. detect when turtle reaches the other side
5. create scoreboard

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
git clone https://github.com/tharunerd/one-hundred-days-of-python.git
cd day_23
python main.py
