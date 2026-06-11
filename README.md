# CIS261_WK10_VIBE - Student Records Management System

## Overview
A comprehensive Python program that manages student records, including test scores and automatic grade calculations. Features input validation, error handling, and clear user feedback throughout. All scores are formatted to 2 decimal places for consistency. The system supports multiple operations per session with automatic data persistence in pipe-delimited format.

## Features

### Student Management
- **Add Students**: Create new student records with unique ID and name with input validation
- **Remove Students**: Delete student records with confirmation prompt
- **View Students**: Display individual or all student records in formatted tables
- **Search by Name**: Case-insensitive search for students by name or partial name match
- **Multiple Operations**: Add and manage multiple students in a single session

### Test Score Management
- **Add Test Scores**: Record three test scores for each student (0-100 scale) with validation
- **Score Formatting**: All scores consistently formatted to 2 decimal places
- **View Scores**: See all test scores for a student with proper formatting
- **Calculate Averages**: Automatically compute average test scores (floats)

### Error Handling & Validation
- **Input Validation**: All user inputs validated for correct format and range
- **Error Messages**: Clear, informative messages guide users on corrections
- **File Error Handling**: Graceful handling of file I/O errors with user feedback
- **Exception Handling**: Comprehensive try/except blocks for robust operation
- **Confirmation Prompts**: Confirmation required for destructive operations

### Grade Calculation
- **Automatic Grading**: Grades are calculated based on average test score:
  - A: 90-100
  - B: 80-89
  - C: 70-79
  - D: 60-69
  - F: Below 60

### Class Statistics
- **Class Statistics**: View overall class performance metrics
  - Average class score
  - Highest student average
  - Lowest student average
  - Total number of students

### Data Persistence
- **Save Records**: Export student records to "student_grades.txt" in pipe-delimited format
- **Auto-Save**: Records are automatically saved on exit or manually
- **Auto-Load**: Previous student records are loaded automatically when the program starts
- **Pipe-Delimited Format**: Data format is `name|id|test1|test2|test3|average|grade` for easy import/export

### File Format
Student records are stored in pipe-delimited format with 2 decimal place precision:
```
name|id|test1|test2|test3|average|grade
John Smith|001|85.00|90.00|92.00|89.00|B
Jane Doe|002|95.00|93.00|91.00|93.00|A
```

### Display Features
- **Formatted Tables**: All student information displayed in organized, easy-to-read tables
- **Professional Output**: Properly aligned columns with clear headers and separators

## How to Use

### Running the Program
```bash
python VIBE.py
```
The program will automatically load any previously saved student records on startup.

### Menu Options
1. **Add a new student** - Enter student ID and name with validation
2. **Add test score to student** - Enter student ID, test number (1-3), and score (0-100)
3. **Remove a student** - Remove a student from the system with confirmation
4. **Display all students** - View all student records in formatted table (2 decimal places)
5. **Display class statistics** - See class-wide performance metrics (2 decimal formatting)
6. **View specific student** - Look up a specific student's record by ID
7. **Search for student by name** - Find students by name (case-insensitive partial match)
8. **Save records to file** - Export records to "student_grades.txt"
9. **Exit** - Exit the program (or press ESC)

## Example Usage

```
1. Add a new student
   - Student ID: 001
   - Student Name: John Smith
   ✓ Student 'John Smith' (ID: 001) added successfully!

2. Add test scores for the student
   - Enter Test 1 score: 85
   - Enter Test 2 score: 90
   - Enter Test 3 score: 92
   ✓ Test 1 score 85.00 added successfully for John Smith!
     New Average: 89.00 | Grade: B

3. View student record (formatted table)
   - Shows: 001 | John Smith | 85.00 | 90.00 | 92.00 | 89.00 | B

4. View class statistics (all values to 2 decimal places)
   - Class Average:    89.00
   - Highest Average:  93.00
   - Lowest Average:   85.00

5. Search for student by name
   - Enter partial name: "john"
   - Returns all students with "john" in their name
```

## File Structure

### Generated Files
- **student_grades.txt**: Pipe-delimited file with all student records and statistics
  - Format: `name|id|test1|test2|test3|average|grade`
  - All numbers formatted to 2 decimal places
  - Includes class statistics section
  - Easily importable into spreadsheet applications

### Auto-Save Feature
- Student records are automatically saved in pipe-delimited format when you exit the program
- Previous records are automatically loaded when you start the program
- Manual save option available in menu option 8

## Code Organization

### Functions for Input Validation
- `validate_student_id()`: Check student ID is not empty
- `validate_student_name()`: Check name is not empty
- `validate_test_number()`: Check test number is 1-3
- `validate_test_score()`: Check score is 0-100

### Functions for Getting Valid Input
- `get_valid_student_id()`: Get and validate student ID with retry loop
- `get_valid_student_name()`: Get and validate name with retry loop
- `get_valid_test_number()`: Get and validate test number with retry loop
- `get_valid_test_score()`: Get and validate score with retry loop

### Functions for Handling Menu Operations
- `handle_add_student()`: Add student with validation and error handling
- `handle_add_test_score()`: Add score with confirmation and feedback
- `handle_remove_student()`: Remove student with confirmation prompt
- `handle_display_all_students()`: Display all records with error handling
- `handle_display_statistics()`: Display class stats with error handling
- `handle_view_student()`: View specific student details
- `handle_search_student()`: Search by name with formatted results
- `handle_save_records()`: Save with comprehensive error handling

## Classes

### Student Class
- `__init__(student_id, name)`: Initialize student with ID, name, and zero scores
- `set_test_score(test_number, score)`: Set test score (1-3) with automatic average/grade update
- `_update_average_and_grade()`: Recalculate average and grade (2 decimal precision)
- `get_average()`: Return average score (float)
- `get_grade()`: Return letter grade (string)
- Attributes: `student_id`, `name`, `test_1`, `test_2`, `test_3`, `average`, `grade`

### StudentRecordManager Class
- `add_student(student_id, name)`: Add new student with duplicate ID check
- `remove_student(student_id)`: Remove existing student
- `add_score_to_student(student_id, test_number, score)`: Add test score with validation
- `display_all_students()`: Display all records with 2 decimal formatting
- `display_statistics()`: Show class statistics with 2 decimal formatting
- `get_student(student_id)`: Retrieve specific student
- `search_by_name(name)`: Case-insensitive name search
- `save_to_file()`: Export to pipe-delimited format with error handling
- `load_from_file()`: Import from file with error handling
- `export_to_json()`: Alias to save_to_file

## Error Handling Features
- **File I/O**: Comprehensive try/except blocks for all file operations
- **Input Validation**: All numeric inputs checked for valid range (0-100, 1-3)
- **User Feedback**: Clear success (✓) and error (✗) messages
- **Graceful Degradation**: Program continues after recoverable errors
- **Confirmation Prompts**: Requires confirmation before deleting students
- **Error Details**: Shows what went wrong for troubleshooting
- **Retry Loops**: Allows users to correct input without restarting
- **Empty State Handling**: Graceful messages when no students exist

## Exit Options
- Press **9** from the menu
- Type **esc** and press Enter
- Press **Ctrl+C** (keyboard interrupt)

All exit methods will automatically save your records before exiting.

## Author
Devonte Arrington - CIS261