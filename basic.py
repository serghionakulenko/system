import os

class FileManager:
    def __init__(self):
        self.current_directory = os.getcwd()

    def create_file(self, filename, content):
        filepath = os.path.join(self.current_directory, filename)
        with open(filepath, "w") as file:
            file.write(content)
        print(f"File '{filename}' created successfully.")

    def view_files(self):
        files = [f for f in os.listdir(self.current_directory) if os.path.isfile(f)]
        if not files:
            print("No files found in the current directory.")
        else:
            print("Files in the current directory:")
            for index, file in enumerate(files, start=1):
                print(f"{index}. {file}")

    def update_file(self, filename, new_content):
        filepath = os.path.join(self.current_directory, filename)
        if os.path.isfile(filepath):
            with open(filepath, "w") as file:
                file.write(new_content)
            print(f"File '{filename}' updated successfully.")
        else:
            print(f"File '{filename}' not found.")

    def delete_file(self, filename):
        filepath = os.path.join(self.current_directory, filename)
        if os.path.isfile(filepath):
            os.remove(filepath)
            print(f"File '{filename}' deleted successfully.")
        else:
            print(f"File '{filename}' not found.")

def main():
    file_manager = FileManager()

    while True:
        print("\nFile Management Menu:")
        print("1. Create File")
        print("2. View Files")
        print("3. Update File")
        print("4. Delete File")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter the filename: ")
            content = input("Enter the content: ")
            file_manager.create_file(filename, content)
        elif choice == "2":
            file_manager.view_files()
        elif choice == "3":
            filename = input("Enter the filename to update: ")
            new_content = input("Enter the new content: ")
            file_manager.update_file(filename, new_content)
        elif choice == "4":
            filename = input("Enter the filename to delete: ")
            file_manager.delete_file(filename)
        elif choice == "5":
            print("Exiting the File Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
