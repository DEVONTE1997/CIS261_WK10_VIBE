#Devonte Arrington
#CIS261 
#VIBE Coding - Student Records Management System

import json
import os
from datetime import datetime


class Student:
    """Represents a student with test scores and grade calculation."""
    
    def __init__(self, student_id, name):
        # Student attributes
        self.student_id = student_id  # Student ID (string)
        self.name = name  # Student name (string)
        
        # Test scores (floats)
        self.test_1 = 0.0
        self.test_2 = 0.0
        self.test_3 = 0.0
        
        # Calculated attributes
        self.average = 0.0  # Calculated average (float)
        self.grade = 'F'    # Calculated grade (string)
    
    def set_test_score(self, test_number, score):
        """Set a test score for the student (test_number: 1, 2, or 3)."""
        if not (0 <= score <= 100):
            return False
        
        if test_number == 1:
            self.test_1 = score
        elif test_number == 2:
            self.test_2 = score
        elif test_number == 3:
            self.test_3 = score
        else:
            return False
        
        # Update average and grade after setting test score
        self._update_average_and_grade()
        return True
    
    def _update_average_and_grade(self):
        """Update average and grade attributes based on test scores."""
        self.average = (self.test_1 + self.test_2 + self.test_3) / 3
        
        if self.average >= 90:
            self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
            self.grade = 'C'
        elif self.average >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'
    
    def get_average(self):
        """Get the calculated average of the three test scores."""
        return self.average
    
    def get_grade(self):
        """Get the calculated letter grade based on average score."""
        return self.grade
    
    def __str__(self):
        """String representation of student record."""
        return f"ID: {self.student_id} | Name: {self.name} | Test 1: {self.test_1:.1f} | Test 2: {self.test_2:.1f} | Test 3: {self.test_3:.1f} | Avg: {self.average:.2f} | Grade: {self.grade}"


class StudentRecordManager:
    """Manages a collection of student records."""
    
    def __init__(self):
        self.students = {}
    
    def add_student(self, student_id, name):
        """Add a new student to the system."""
        if student_id in self.students:
            return False  # Student ID already exists
        self.students[student_id] = Student(student_id, name)
        return True
    
    def remove_student(self, student_id):
        """Remove a student from the system."""
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False
    
    def add_score_to_student(self, student_id, test_number, score):
        """Add a test score to a specific test for a student."""
        if student_id not in self.students:
            return False
        return self.students[student_id].set_test_score(test_number, score)
    
    def get_student(self, student_id):
        """Retrieve a student by ID."""
        return self.students.get(student_id)
    
    def display_all_students(self):
        """Display all student records in a formatted table with 2 decimal places."""
        if not self.students:
            print("\n✗ No students in the system.")
            return
        
        try:
            print("\n" + "="*130)
            print("STUDENT RECORDS - FORMATTED TABLE")
            print("="*130)
            print(f"{'Student ID':<12} {'Name':<20} {'Test 1':<12} {'Test 2':<12} {'Test 3':<12} {'Average':<12} {'Grade':<8}")
            print("-"*130)
            
            for student in self.students.values():
                print(f"{student.student_id:<12} {student.name:<20} {student.test_1:<12.2f} {student.test_2:<12.2f} {student.test_3:<12.2f} {student.get_average():<12.2f} {student.get_grade():<8}")
            
            print("="*130 + "\n")
        except Exception as e:
            print(f"✗ Error displaying students: {e}")
    
    def get_class_statistics(self):
        """Calculate class-wide statistics."""
        if not self.students:
            return None
        
        all_averages = [s.get_average() for s in self.students.values()]
        class_avg = sum(all_averages) / len(all_averages)
        highest_avg = max(all_averages)
        lowest_avg = min(all_averages)
        
        return {
            'class_average': class_avg,
            'highest_average': highest_avg,
            'lowest_average': lowest_avg,
            'student_count': len(self.students)
        }
    
    def display_statistics(self):
        """Display class statistics with clear formatting."""
        try:
            stats = self.get_class_statistics()
            if stats:
                print("\n" + "="*50)
                print("CLASS STATISTICS")
                print("="*50)
                print(f"Total Students:    {stats['student_count']}")
                print(f"Class Average:     {stats['class_average']:.2f}")
                print(f"Highest Average:   {stats['highest_average']:.2f}")
                print(f"Lowest Average:    {stats['lowest_average']:.2f}")
                print("="*50 + "\n")
            else:
                print("✗ No students to calculate statistics for.")
        except Exception as e:
            print(f"✗ Error calculating statistics: {e}")
    
    def search_by_name(self, name):
        """Search for students by name (case-insensitive)."""
        results = []
        search_name = name.lower()
        for student in self.students.values():
            if search_name in student.name.lower():
                results.append(student)
        return results
    
    def save_to_file(self, filename="student_grades.txt"):
        """Save all student records to a pipe-delimited file with error handling."""
        try:
            if not self.students:
                print("✗ No students to save!")
                return False
            
            with open(filename, 'w') as file:
                # Write header
                file.write(f"# STUDENT RECORDS - Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("name|id|test1|test2|test3|average|grade\n")
                
                # Write student records with 2 decimal places
                for student in self.students.values():
                    file.write(f"{student.name}|{student.student_id}|{student.test_1:.2f}|{student.test_2:.2f}|{student.test_3:.2f}|{student.average:.2f}|{student.grade}\n")
                
                # Add class statistics
                file.write("\n# CLASS STATISTICS\n")
                stats = self.get_class_statistics()
                if stats:
                    file.write(f"Total Students|{stats['student_count']}\n")
                    file.write(f"Class Average|{stats['class_average']:.2f}\n")
                    file.write(f"Highest Average|{stats['highest_average']:.2f}\n")
                    file.write(f"Lowest Average|{stats['lowest_average']:.2f}\n")
            
            return True
        except IOError as e:
            print(f"✗ File I/O error while saving: {e}")
            return False
        except Exception as e:
            print(f"✗ Unexpected error while saving: {e}")
            return False
    
    def load_from_file(self, filename="student_grades.txt"):
        """Load student records from a pipe-delimited file with error handling."""
        if not os.path.exists(filename):
            return False
        
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                loaded_count = 0
                
                # Skip header lines and comments
                for line in lines:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    
                    # Skip statistics lines (they contain pipes but not 7 fields)
                    parts = line.split('|')
                    if len(parts) != 7:
                        continue
                    
                    # Parse student record with error handling
                    try:
                        name, student_id, test_1, test_2, test_3, average, grade = parts
                        student_id = student_id.strip()
                        
                        # Check for duplicate IDs
                        if student_id in self.students:
                            continue
                        
                        student = Student(student_id, name.strip())
                        student.test_1 = float(test_1.strip())
                        student.test_2 = float(test_2.strip())
                        student.test_3 = float(test_3.strip())
                        student._update_average_and_grade()  # Recalculate to ensure accuracy
                        self.students[student_id] = student
                        loaded_count += 1
                    except (ValueError, IndexError) as e:
                        # Skip malformed lines silently
                        continue
                
            return loaded_count > 0
        except IOError as e:
            print(f"✗ Error reading file: {e}")
            return False
        except Exception as e:
            print(f"✗ Unexpected error loading records: {e}")
            return False
    
    def export_to_json(self, filename="student_records.json"):
        """Export student records to pipe-delimited format for persistent storage."""
        # Convert JSON filename to txt for consistency
        if filename.endswith('.json'):
            filename = filename.replace('.json', '.txt')
        
        return self.save_to_file(filename)


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("STUDENT RECORDS MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add a new student")
    print("2. Add test score to student")
    print("3. Remove a student")
    print("4. Display all students (formatted table)")
    print("5. Display class statistics")
    print("6. View specific student")
    print("7. Search for student by name")
    print("8. Save records to file")
    print("9. Exit (or press ESC)")
    print("="*50)


def validate_student_id(student_id):
    """Validate student ID input."""
    if not student_id:
        print("✗ Student ID cannot be empty!")
        return False
    return True


def validate_student_name(name):
    """Validate student name input."""
    if not name:
        print("✗ Student name cannot be empty!")
        return False
    return True


def validate_test_number(test_num):
    """Validate test number (1-3)."""
    if test_num not in [1, 2, 3]:
        print("✗ Test number must be 1, 2, or 3!")
        return False
    return True


def validate_test_score(score):
    """Validate test score (0-100)."""
    if score < 0 or score > 100:
        print("✗ Test score must be between 0 and 100!")
        return False
    return True


def get_valid_student_id():
    """Get and validate student ID from user."""
    while True:
        student_id = input("Enter student ID: ").strip()
        if validate_student_id(student_id):
            return student_id


def get_valid_student_name():
    """Get and validate student name from user."""
    while True:
        name = input("Enter student name: ").strip()
        if validate_student_name(name):
            return name


def get_valid_test_number():
    """Get and validate test number from user."""
    while True:
        try:
            test_num = int(input("Enter test number (1, 2, or 3): "))
            if validate_test_number(test_num):
                return test_num
        except ValueError:
            print("✗ Please enter a valid number (1, 2, or 3)!")


def get_valid_test_score():
    """Get and validate test score from user."""
    while True:
        try:
            score = float(input("Enter test score (0-100): "))
            if validate_test_score(score):
                return score
        except ValueError:
            print("✗ Please enter a valid decimal number!")


def handle_add_student(manager):
    """Handle adding a new student."""
    try:
        student_id = get_valid_student_id()
        name = get_valid_student_name()
        
        if manager.add_student(student_id, name):
            print(f"✓ Student '{name}' (ID: {student_id}) added successfully!")
            return True
        else:
            print(f"✗ Student ID '{student_id}' already exists! Please use a different ID.")
            return False
    except Exception as e:
        print(f"✗ Error adding student: {e}")
        return False


def handle_add_test_score(manager):
    """Handle adding a test score to a student."""
    try:
        student_id = input("Enter student ID: ").strip()
        if not validate_student_id(student_id):
            return False
        
        student = manager.get_student(student_id)
        if not student:
            print(f"✗ Student with ID '{student_id}' not found!")
            return False
        
        test_num = get_valid_test_number()
        score = get_valid_test_score()
        
        if manager.add_score_to_student(student_id, test_num, score):
            print(f"✓ Test {test_num} score {score:.2f} added successfully for {student.name}!")
            print(f"  New Average: {student.get_average():.2f} | Grade: {student.get_grade()}")
            return True
        else:
            print("✗ Error adding test score!")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def handle_remove_student(manager):
    """Handle removing a student."""
    try:
        student_id = get_valid_student_id()
        student = manager.get_student(student_id)
        
        if not student:
            print(f"✗ Student with ID '{student_id}' not found!")
            return False
        
        confirm = input(f"Are you sure you want to remove {student.name}? (yes/no): ").strip().lower()
        if confirm in ['yes', 'y']:
            if manager.remove_student(student_id):
                print(f"✓ Student '{student.name}' removed successfully!")
                return True
        else:
            print("✗ Removal cancelled.")
            return False
    except Exception as e:
        print(f"✗ Error removing student: {e}")
        return False


def handle_display_all_students(manager):
    """Handle displaying all student records."""
    try:
        if not manager.students:
            print("\n✗ No students in the system.")
            return
        
        print("\n" + "="*130)
        print("STUDENT RECORDS - FORMATTED TABLE")
        print("="*130)
        print(f"{'Student ID':<12} {'Name':<20} {'Test 1':<12} {'Test 2':<12} {'Test 3':<12} {'Average':<12} {'Grade':<8}")
        print("-"*130)
        
        for student in manager.students.values():
            print(f"{student.student_id:<12} {student.name:<20} {student.test_1:<12.2f} {student.test_2:<12.2f} {student.test_3:<12.2f} {student.get_average():<12.2f} {student.get_grade():<8}")
        
        print("="*130 + "\n")
    except Exception as e:
        print(f"✗ Error displaying students: {e}")


def handle_display_statistics(manager):
    """Handle displaying class statistics."""
    try:
        manager.display_statistics()
    except Exception as e:
        print(f"✗ Error displaying statistics: {e}")


def handle_view_student(manager):
    """Handle viewing a specific student."""
    try:
        student_id = get_valid_student_id()
        student = manager.get_student(student_id)
        
        if student:
            print("\n" + "="*80)
            print("STUDENT DETAILS")
            print("="*80)
            print(f"Student ID:    {student.student_id}")
            print(f"Name:          {student.name}")
            print(f"Test 1:        {student.test_1:.2f}")
            print(f"Test 2:        {student.test_2:.2f}")
            print(f"Test 3:        {student.test_3:.2f}")
            print(f"Average:       {student.get_average():.2f}")
            print(f"Grade:         {student.get_grade()}")
            print("="*80 + "\n")
        else:
            print(f"✗ Student with ID '{student_id}' not found!")
    except Exception as e:
        print(f"✗ Error viewing student: {e}")


def handle_search_student(manager):
    """Handle searching for students by name."""
    try:
        search_name = input("Enter student name (or part of name) to search: ").strip()
        if not search_name:
            print("✗ Search term cannot be empty!")
            return
        
        results = manager.search_by_name(search_name)
        
        if results:
            print(f"\n✓ Found {len(results)} student(s) matching '{search_name}':")
            print("="*130)
            print(f"{'Student ID':<12} {'Name':<20} {'Test 1':<12} {'Test 2':<12} {'Test 3':<12} {'Average':<12} {'Grade':<8}")
            print("-"*130)
            
            for student in results:
                print(f"{student.student_id:<12} {student.name:<20} {student.test_1:<12.2f} {student.test_2:<12.2f} {student.test_3:<12.2f} {student.get_average():<12.2f} {student.get_grade():<8}")
            
            print("="*130 + "\n")
        else:
            print(f"✗ No students found matching '{search_name}'!")
    except Exception as e:
        print(f"✗ Error searching students: {e}")


def handle_save_records(manager):
    """Handle saving records to file with error handling."""
    try:
        if manager.save_to_file():
            print("✓ Records saved to 'student_grades.txt' successfully!")
            print("  File format: name|id|test1|test2|test3|average|grade")
        else:
            print("✗ Error saving records to file! Please check file permissions.")
    except IOError as e:
        print(f"✗ File I/O error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error while saving: {e}")


def run_application():
    """Run the student records management system with organized function calls."""
    manager = StudentRecordManager()
    
    # Try to load existing records
    try:
        if manager.load_from_file():
            print("✓ Previous student records loaded successfully!")
    except Exception as e:
        print(f"✗ Could not load previous records: {e}")
    
    print("\n" + "="*50)
    print("WELCOME TO STUDENT RECORDS SYSTEM")
    print("="*50)
    
    while True:
        try:
            display_menu()
            choice = input("Enter your choice (1-9) or press ESC: ").strip()
            
            # Check for ESC key or exit command
            if choice.lower() == 'esc' or choice == '\x1b':
                print("\n✓ Exiting program...")
                try:
                    if manager.export_to_json():
                        print("✓ Records saved automatically!")
                except Exception as e:
                    print(f"✗ Error saving records: {e}")
                print("Thank you for using the Student Records System. Goodbye!\n")
                break
            
            # Route to appropriate handler based on user choice
            if choice == '1':
                handle_add_student(manager)
            
            elif choice == '2':
                handle_add_test_score(manager)
            
            elif choice == '3':
                handle_remove_student(manager)
            
            elif choice == '4':
                handle_display_all_students(manager)
            
            elif choice == '5':
                handle_display_statistics(manager)
            
            elif choice == '6':
                handle_view_student(manager)
            
            elif choice == '7':
                handle_search_student(manager)
            
            elif choice == '8':
                handle_save_records(manager)
            
            elif choice == '9':
                print("\n✓ Exiting program...")
                try:
                    if manager.export_to_json():
                        print("✓ Records saved automatically!")
                except Exception as e:
                    print(f"✗ Error saving records: {e}")
                print("Thank you for using the Student Records System. Goodbye!\n")
                break
            
            else:
                print("✗ Invalid choice! Please enter a number between 1 and 9.")
            
            # Allow user to continue with more operations
            input("\nPress Enter to continue...")
        
        except KeyboardInterrupt:
            print("\n\n✓ Program interrupted by user.")
            try:
                if manager.export_to_json():
                    print("✓ Records saved before exit!")
            except Exception as e:
                print(f"✗ Error saving records: {e}")
            print("Goodbye!\n")
            break
        
        except Exception as e:
            print(f"✗ An unexpected error occurred: {e}")
            print("  Please try again or contact support if the problem persists.")


if __name__ == "__main__":
    run_application()