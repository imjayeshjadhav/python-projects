# 🎲 Roll & Race: Dice Game (Python)

Welcome to **Roll & Race**, a fun, turn-based dice game built in Python!  
Compete against friends or a clever AI in this suspenseful race to the finish.



## 🚀 Game Overview

### 🎯 Objective
Be the **first player** to reach **50 points** to win the game.

### 🎲 Rules
- Players take turns rolling a 6-sided die.
- On each turn, you can **keep rolling** to accumulate a **turn score**.
- **But beware** — if you roll a **1**, your **turn score resets to 0**, and your turn ends immediately.
- You can choose to **hold** at any point to bank your current turn score into your total score.
- The first to hit **50 points** wins!



## 🤖 Game Modes

### 🧑‍🤝‍🧑 Multiplayer Mode (2–4 Players)
Play with 2 to 4 **human players**:
- Each player is prompted on their turn whether they want to roll or hold.
- Scores are tracked individually.
- The game ends when **any player** reaches 50 points.

📄 File: `multiplayer/main.py`



### 🧠 AI Mode (1 Player vs AI)
Challenge a **smart AI** opponent:
- You play against the computer.
- The **AI strategy**: It keeps rolling until its **turn score is 15 or more**, then it holds.
- Win or watch the AI outsmart you!

📄 File: `play_with_ai/main.py`



## 🧪 Sample AI Strategy

> “I’ll keep rolling until I reach 15 or more points in a turn... unless I roll a 1!”



## 🔧 Technologies Used

- 🐍 Python 3.x
- 🎲 `random` — for simulating dice rolls
- ⏱️ `time.sleep()` — to simulate delays for a better user experience


## 💡 Customization Ideas

- Modify the **winning score** (`max_score`) to make the game longer or shorter.
- Change the **AI strategy** to make it harder or easier.
- Add a **graphical interface** using libraries like `tkinter` or `pygame`.



## 📜 License

Feel free to fork, modify, or share this game for **learning or fun**.  
No attribution required, just enjoy and share the joy of Python! 🚀
