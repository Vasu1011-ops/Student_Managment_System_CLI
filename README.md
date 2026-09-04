# 🏫 School Management System

A **console-based School Management System built using Python** that allows users to manage basic information of students and teachers. The project demonstrates important Python concepts such as **Object-Oriented Programming (OOP), inheritance, constructors, and CSV file handling**.

## 🚀 Features

* 👨‍🎓 Add student information
* 👨‍🏫 Add teacher information
* 💾 Store student records in a CSV file
* 💾 Store teacher records in a CSV file
* 📋 Display basic student and teacher information
* 🔄 Uses inheritance to share common attributes between classes
* 🗂️ Uses CSV files for simple data storage

## 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **Inheritance**
* **Constructors**
* **CSV File Handling**

## 📂 Project Structure

```text
school-management-system-python/
│
├── main.py
├── students.csv
├── Teachers.csv
└── README.md
```

> `students.csv` and `Teachers.csv` are used to store the entered records.

## 🧠 OOP Concepts Used

The project uses a parent class and child classes:

```text
             School
            /      \
           /        \
      Students     Teachers
```

### `School`

The parent class contains common student/teacher attributes such as:

* Name
* Age

### `students`

The `students` class inherits from `School` and contains:

* Class
* Roll Number
* Percentage

### `teachers`

The `teachers` class inherits from `School` and contains:

* Subject
* Salary

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd school-management-system-python
```

### 3. Run the Python program

```bash
python main.py
```

## 💻 How It Works

When the program starts, the user can choose between:

```text
For Students Enter 'S'
For Teachers Enter 'T'
```

### Student

If the user enters `S`, the program asks for:

* Student Name
* Class
* Age
* Roll Number
* Percentage

The information is then stored in `students.csv`.

### Teacher

If the user enters `T`, the program asks for:

* Teacher Name
* Age
* Teaching Subject
* Salary

The information is then stored in `Teachers.csv`.

## 📌 Example

```text
For Students Enter 'S'
For Teachers Enter 'T'

Enter here: S

Enter Student name: Rahul
Enter Student class: 12
Enter Student age: 18
Enter roll no.: 25
Enter Student Percentage %: 85.5

The Name Of the Student is Rahul, and its Roll no. is 25
Data entered successfully!
```

## 🎯 Learning Objectives

This project was created to practice and understand:

* Python classes and objects
* Constructors (`__init__`)
* Inheritance
* `super()`
* Instance attributes
* User input
* Type conversion
* CSV file handling
* Writing data to files

## 🔮 Future Improvements

Some features that can be added in future versions:

* 🔍 Search student/teacher records
* ✏️ Update existing records
* 🗑️ Delete records
* 📊 Display all records in a formatted table
* ✅ Input validation
* 🔐 Admin login system
* 🗄️ Database integration using MySQL/SQLite
* 🖥️ GUI using Tkinter
* 📈 Student performance tracking

## 👨‍💻 Author

**Vasu Sharma**

A Python project created as part of my journey in learning **Python, OOP, and file handling**.
