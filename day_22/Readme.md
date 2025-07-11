
## ✅ Features and Tasks Breakdown

### 1. 🎮 Game Window Setup
- Used `turtle.Screen()` to create an 800×600 pixel game window
- Set up background color and title
- Disabled automatic screen updates using `tracer(0)` for smoother animation

### 2. 🏓 Paddle Creation
- Built a `Paddle` class inheriting from `turtle.Turtle`
- Created two paddles positioned on the left and right sides of the screen
- Added methods to move paddles up and down

### 3. ⌨️ Paddle Controls
- Bound player controls to keyboard keys:
  - Right Paddle: `Up`, `Down`
  - Left Paddle: `W`, `S`
- Used `screen.listen()` and `screen.onkey()` for control handling

### 4. 🔴 Ball Creation & Movement
- Built a `Ball` class that:
  - Moves diagonally at a constant speed
  - Bounces off top and bottom walls
- Included methods:
  - `.move()`, `.bounce_y()`, `.bounce_x()`, `.reset_position()`

### 5. 💥 Collision Detection
- Detected collision between ball and paddles using distance and position checks
- Implemented ball bouncing logic when hitting a paddle
- Detected wall collisions and reversed Y direction

### 6. 🧠 Scoreboard
- Built a `Scoreboard` class using `turtle`
- Tracked and displayed scores for both players
- Updated score when a player misses the ball
- Centered text and styled font display

### 7. 🔁 Game Loop
- Continuously updated the screen with `screen.update()`
- Introduced delay using `time.sleep()` for smooth motion
- Handled all collisions, movement, and scoring inside the loop

