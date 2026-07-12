# 🚀 Python Core to Advanced OOP: Mastery Projects

Welcome to my Python foundational and architectural showcase repository. This repository features four distinct terminal-based applications built progressively to demonstrate a transition from procedural programming and basic data structures to system automation, file manipulation, exception handling and **Object-Oriented Programming (OOP)**.

Each project focuses on real-world logic, clean code architecture, and robust edge-case handling.

---

## 📂 Repository Structure

```text
Python-Core-Projects/
│
├── 01_Inventory_Management/
│   └── inventory_management.py      # CRUD implementation with native structures
│
├── 02_Student_Grading_System/
│   ├── student_grading_system.py    # File handling and exception workflow
│   └── students.txt                 # Flattened database storage file
│
├── 03_Banking_System_OOP/
│   └── banking_system.py            # Advanced Multi-user OOP simulation
│
└── README.md                        # Project documentation

## 🛠️ Detailed Project Breakdown

### 📦 1. Inventory Management System

* **Core Concepts Covered:** `while` loops, conditional flows (`if-elif-else`), Python Dictionaries, Dynamic User Input.
    
* **Architecture:** Implements a stable terminal-based **CRUD (Create, Read, Update, Delete)** engine.
    
* **Key Features:**
    
    * Interactive CLI menu allowing continuous operations.
        
    * Memory-mapped state management using dictionary key-value pairing to keep track of product quantities.
        
    * Graceful data pruning using safe dictionary element deletions via `del`.
        

### 📝 2. Student Grading System with File I/O

* **Core Concepts Covered:** Data Persistence (`with open`), String Parsing & Tokenization (`.strip()`, `.split()`), Casting, Robust Exception Handling (`try-except`).
    
* **Architecture:** Bridges the gap between volatile memory and permanent storage by serializing structural flat-file streams.
    
* **Key Features:**
    
    * **File Persistence:** Appends user records automatically into a flat `.txt` file, maintaining records across system restarts.
        
    * **Data Cleansing:** Parses incoming data streams by removing hidden whitespace / newline characters (`\n`) to safely execute operations.
        
    * **Fail-Safe Crash Guard:** Intercepts potential runtime failures (like missing physical files using `FileNotFoundError`) ensuring continuous operation.
        

### 🏛️ 3. Central Banking & ATM Simulator (OOP Architecture)

* **Core Concepts Covered:** Object-Oriented Design (OOP), Constructors (`__init__`), Instance Scope & Context Binding (`self`), In-Memory Complex Dictionary Mappings.
    
* **Architecture:** An industry-standard simulation modeled around real-world business items. Instead of primitive data tracking, this engine maps string keys directly to functional **Account Instances (Objects)** inside an encapsulated virtual database.
    
* **Key Features:**
    
    * **Encapsulation:** State parameters (`holder_name`, `balance`) are self-contained and manipulated strictly through defined instance behaviors (`deposit()`, `withdraw()`).
        
    * **Transaction Integrity Guards:** Prevents illegal business logic states (e.g., overdraft blocking with an insufficient balance handler).
        
    * **Multi-Tenant System:** Scalable dynamic account registry. Mutating one user entity's balance maintains data isolation from other parallel objects.
        

## 🚀 Technical Highlights & Key Learnings

Throughout developing this core pipeline, I have mastered:

1. **Dynamic Memory vs Persistent State:** Understanding when to use volatile runtime structures (Dictionaries) versus non-volatile serialized IO boundaries (Files & Logs).
    
2. **Defensive Coding Practices:** Writing predictable, clean code by implementing granular validation conditionals, advanced regular expressions, and explicit type conversions.
    
3. **The OOP Shift:** Moving away from sequential execution blocks toward building modular, reusable blueprints (Classes) that control their own internal data mutations.
    

## 💻 How To Run Locally

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/farhanadilumarkhan/python-core-mastery.git
cd Python-Core-Projects