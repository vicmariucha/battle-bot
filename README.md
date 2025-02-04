# Battle Bot 🤖⚔️

Developed by me in 2021 during my participation in the summer virtual camp by iDTech "Python: Arcade Games and IA". Battle Bot is a Python-based project that simulates automated combat between bots. The primary objective is to create a system where bots engage in battles, making decisions based on random choices to simulate unpredictability in combat scenarios.

## 📌 Features

- **Automated combat system**: Bots engage in battles without human intervention.
- **Randomized decision-making**: Bots make random choices to determine their actions during combat.
- **Modular design**: The project is organized into distinct modules for better readability and maintenance.

## 🛠️ Technologies 

- **Python**: Core programming language for the project's implementation.

## 🗂️ Project Structure

The project comprises the following modules:

1. **Arena.py**: Defines the `Arena` class, which manages the combat environment where bots battle. It handles the sequence of turns and determines the outcome of the battle.

2. **BattleBot.py**: Contains the `BattleBot` class, representing the bots participating in the battle. Each bot has attributes like name, health, and methods to attack and take damage.

3. **MrKnowItAll.py**: Introduces the `MrKnowItAll` class, a specialized type of `BattleBot`. This bot has enhanced decision-making capabilities, potentially using more sophisticated strategies in combat.

4. **main.py**: The entry point of the application. It initializes the bots and the arena, then starts the battle simulation.

## 🎮 How it works

- **Initialization**: Two bots are created, either standard `BattleBot` instances or specialized bots like `MrKnowItAll`.
- **Combat simulation**: The `Arena` manages the battle, where bots take turns attacking each other. The actions during each turn are determined randomly, simulating unpredictable combat scenarios.
- **Victory conditions**: The battle continues until one bot's health is depleted. The bot with the remaining health is declared the winner.

## 🚀 How to run the project

1. **Clone this repository**:
   ```sh
   git clone https://github.com/vicmariucha/battle-bot.git
   ```
2. **Navigate to the project directory**:
   ```sh
   cd battle-bot
   ```
3. **Run the main script**:
   ```sh
   python main.py
   ```

## 📷 Demonstration
![Battle bot](https://cdn.discordapp.com/attachments/1089566799714078840/1336362220497535026/image.png?ex=67a387cd&is=67a2364d&hm=5cac9626d2595f4941efa7fd7e70af0c379fdd07f8b3f244c38f49c80290d32f&)
![Battle bot](https://cdn.discordapp.com/attachments/1089566799714078840/1336362314978426942/image.png?ex=67a387e4&is=67a23664&hm=4998fdc98541046a61344da3185146d43cdc56a119a934427c80ae3f1429de20&)
![Battle bot](https://cdn.discordapp.com/attachments/1089566799714078840/1336362757024645192/image.png?ex=67a3884d&is=67a236cd&hm=7d1cde88bdc3c49e8b357d6bfc6c7dd8d8a2326e79e9c263bae4626ab996edbd&)

## 📝 License
This project was created for educational purposes. Feel free to use and modify it as needed.

📩 If you have any questions or suggestions, feel free to reach out!

---

🤖 "A bot never sleeps... But it also never levels up on its own!" 😆
