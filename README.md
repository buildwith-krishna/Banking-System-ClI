<div align="center">

# 🏦 Banking System CLI

### *Basic banking operations right from the terminal.*

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Windows-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Phase%201%20Started-yellow?style=for-the-badge)
![Built On](https://img.shields.io/badge/Built%20On-Android%20Phone-red?style=for-the-badge&logo=android)

<br/>

> **A simple terminal-based banking system built in Python.**
> Create an account, deposit money, withdraw money, and prepare data storage using JSON.

<br/>

*Built entirely on an Android phone using Termux.* 📱⚡

---

</div>

## 👨‍💻 Author

<table>
  <tr>
    <td align="center">
      <strong>Krishna Pandey</strong><br/>
      <sub>Aspiring Backend Developer | Python | CLI Tools | Termux</sub><br/><br/>
      <a href="https://github.com/buildwith-krishna">🐙 GitHub</a> •
      <a href="https://linkedin.com/in/krishnapandey">💼 LinkedIn</a>
    </td>
  </tr>
</table>

> *"Consistent progress > temporary motivation"* ⭐

---

## 🚧 Project Status

```
✅ Phase 1 Started — Basic account model with deposit and withdrawal
🔜 Next Step — Connect JSON storage with the account flow
```

---

## ✨ Features

| Status | Feature |
|--------|---------|
| ✅ Done | Account class created using OOP |
| ✅ Done | Stores account number, name, and balance |
| ✅ Done | Takes user input from terminal |
| ✅ Done | Empty name validation |
| ✅ Done | Number-only validation for account number and amount |
| ✅ Done | Deposit amount validation |
| ✅ Done | Withdrawal amount validation |
| ✅ Done | Insufficient balance check |
| ✅ Done | Shows updated balance after deposit |
| ✅ Done | Shows updated balance after withdrawal |
| ✅ Done | JSON load helper function |
| ✅ Done | JSON save helper function |
| ✅ Done | Config file for storing data file name |
| 📋 Planned | Move CLI flow into main.py |
| 📋 Planned | Connect storage.py with account operations |
| 📋 Planned | Save account data in Banking_data.json |
| 📋 Planned | Add menu-based banking system |
| 📋 Planned | Account lookup by account number |
| 📋 Planned | Balance enquiry feature |

---

## 📁 Project Structure

```
Banking_System_CLI/
│
├── 📄 main.py        ← Entry point file, currently empty
├── 📄 model.py       ← Account class and current CLI flow
├── 📄 storage.py     ← JSON read/write operations
├── 📄 config.py      ← Constants and configuration
└── 📄 README.md      ← Project documentation
```

---

## 🗃️ Data Storage

The project already has JSON helper functions ready in `storage.py`.

Data file name is stored in `config.py`:

```python
FILE_NAME = "Banking_data.json"
```

Current storage helpers:

```python
load()      # Reads data from JSON file
save(data) # Saves data into JSON file
```

Right now, the storage layer is prepared but not fully connected with the account flow.

---

## ▶️ How to Run

**Clone the repo:**
```bash
git clone https://github.com/buildwith-krishna/Banking-System-ClI.git
cd Banking-System-ClI
```

**Run the current app flow:**
```bash
python model.py
```

**Requirements:**
```
Python 3.x
No external libraries needed — pure standard library
```

---

## 🧪 Example Flow

```text
Enter name : Rahul
Enter account number : 101
Enter amount to deposite : 5000
Enter amount for withdrawl : 1500
5000 INR added successfully.
Total balance : 5000
1500 INR withdrew. total balance : 3500
```

---

## 🗺️ Roadmap

```
Phase 1 — Basic CLI Banking System
    ✅ Account class
    ✅ Deposit money
    ✅ Withdraw money
    ✅ Input validation
    ✅ Basic balance update
    ✅ JSON storage helper functions

Phase 2 — Proper CLI Structure
    📋 Shift running code from model.py to main.py
    📋 Add menu system
    📋 Create multiple accounts
    📋 Search account by account number
    📋 Check balance anytime

Phase 3 — Data Persistence
    📋 Save account data in Banking_data.json
    📋 Load old account data on app start
    📋 Update balance permanently after deposit/withdrawal

Phase 4 — Backend Journey
    📋 FastAPI backend
    📋 SQLite database
    📋 REST endpoints
```

---

## 💡 About This Project

This is not just a banking system.

This is another step in my backend development journey — learning OOP, validation, file handling, JSON storage, and clean project structure one project at a time.

Built on an **Android phone** using **Termux** — no laptop, no fancy setup, just Python and consistency.

---

## 📊 Part of My Journey

This project continues my CLI + Python learning path.

Previous projects:
- 📒 [Notes App CLI](https://github.com/buildwith-krishna/notes-app)
- 🔐 [Password Manager CLI](https://github.com/buildwith-krishna/password-manager-cli)
- 📇 [Contact Book CLI](https://github.com/buildwith-krishna/Contact-book-CLI)
- 💰 [Finance Tracker CLI](https://github.com/buildwith-krishna/Finance-tracker-cli)

---

<div align="center">

**If this project helped or inspired you, drop a ⭐ — it means a lot!**

*Made with 💪 and consistency by Krishna Pandey*

</div>
