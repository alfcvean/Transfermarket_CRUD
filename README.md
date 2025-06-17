# Transfermarket_CRUD

Transfermarket_CRUD is a terminal-based Python application that simulates a European football transfer market system. It provides CRUD (Create, Read, Update, Delete) operations and additional features like player transfer and recycle bin management. This project is designed with two user roles: Admin and Guest, each with different access levels.

Features
✅ General Features (Accessible by Admin and Guest)
•	View Player List – Displays all players in a table format.
•	Search Player – Search for players by position and maximum price.

🔐 Admin-Only Features
•	Add Player – Add a new player with complete details.
•	Update Player – Modify an existing player’s information.
•	Delete Player – Remove a player and move them to the recycle bin.
•	Buy Player – Simulate bidding and purchasing a player.
•	Recycle Bin – View deleted players and restore them if needed.

🔒 Login System
•	Users must log in before accessing the system.
•	Two available roles:
o	Admin: Full access (username: admin, password: admin123)
o	Guest: Limited access (username: guest, password: guest123)

## Data Structure
The player data is stored in a dictionary format containing:
•	players_id
•	name
•	age
•	position
•	price
•	contract_expire
•	club
•	country
A separate recycle_bin list stores deleted players temporarily, allowing for restoration.

## How to Run
1.	Clone the repository:
 	git clone https://github.com/your-username/Transfermarket_CRUD.git
  cd Transfermarket_CRUD
2.	Make sure you have Python installed (preferably Python 3.8+).
3.	Install the required package:
 	pip install tabulate
4.	Run the script:
 	python transfermarket.py

## Example Screenshot
![image](https://github.com/user-attachments/assets/215924fd-09a7-4ca0-9e12-19228ef20904)
