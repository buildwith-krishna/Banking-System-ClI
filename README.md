<div align="center">

# 🏦 Banking System CLI

### *Basic banking operations right from the terminal.*

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Windows-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Phase%202%20Started-orange?style=for-the-badge)
![Built On](https://img.shields.io/badge/Built%20On-Android%20Phone-red?style=for-the-badge&logo=android)

<br/>

> **A terminal-based banking system built in Python.**
> Create an account with password protection, log in, and perform banking operations with JSON data persistence.

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
✅ Phase 1 Done — Account model and basic logic
✅ Phase 2 Started — Menu system and storage integration
🔜 Next Step — Refine banking operations (deposit/withdrawal) within menu
```

---

## ✨ Features

| Status | Feature |
|--------|---------|
| ✅ Done | Account class created using OOP |
| ✅ Done | Stores account number and balance |
| ✅ Done | **New:** Password protection for accounts |
| ✅ Done | **New:** Multi-choice menu system in `main.py` |
| ✅ Done | **New:** Account creation flow |
| ✅ Done | **New:** Login system with password verification |
| ✅ Done | **New:** Connected `storage.py` with `main.py` |
| ✅ Done | **New:** Automatic data saving in `Banking_data.json` |
| ✅ Done | Empty input validation |
| ✅ Done | Number-only validation for choices |
| ✅ Done | JSON load and save helpers |
| 📋 Planned | Connect deposit/withdrawal logic in menu |
| 📋 Planned | Account lookup by account number |
| 📋 Planned | Balance enquiry feature |

---

## 📁 Project Structure

```
Banking_System_CLI/
│
├── 📄 main.py        ← Main entry point with menu & auth logic
├── 📄 model.py       ← Account class (OOP structure)
├── 📄 storage.py     ← JSON read/write operations
├── 📄 config.py      ← Constants and configuration
└── 📄 README.md      ← Project documentation
```

---

## 🗃️ Data Storage

The project uses JSON for persistent storage.

Data file name is stored in `config.py`:

```python
FILE_NAME = "Banking_data.json"
```

Current storage flow:
1. `load()` reads existing accounts from `Banking_data.json`.
2. New accounts are added to the dictionary.
3. `save(data)` writes the updated dictionary back to the file.

---

## ▶️ How to Run

**Clone the repo:**
```bash
git clone https://github.com/buildwith-krishna/Banking-System-CLI.git
cd Banking-System-CLI
```

**Run the app:**
```bash
python main.py
```

**Requirements:**
```
Python 3.x
No external libraries needed — pure standard library
```

---

## 🧪 Example Flow

```text
#<<--Banking System CLI-->>#
 1. Log in to your account
 2. Create a new account
 3. Exit

Enter choice: 2
Enter account number: 101
Enter password: securepassword123
Account created successfully
```

---

## 🗺️ Roadmap

```
Phase 1 — Basic CLI Banking System
    ✅ Account class
    ✅ Deposit money (basic)
    ✅ Withdraw money (basic)
    ✅ Input validation
    ✅ JSON storage helper functions

Phase 2 — Proper CLI Structure
    ✅ Shift running code to main.py
    ✅ Add menu system (Login/Create Account)
    ✅ Password protection for accounts
    ✅ Connect storage.py with main flow
    📋 Connect deposit/withdrawal within account menu

Phase 3 — Data Persistence & Refinement
    ✅ Save account data in Banking_data.json
    ✅ Load old account data on app start
    📋 Refine OOP integration in main menu
    📋 Search account by account number
    📋 Check balance anytime

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
