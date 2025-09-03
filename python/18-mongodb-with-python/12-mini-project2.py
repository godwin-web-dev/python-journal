import pymongo
from datetime import datetime

if __name__=="__main__":
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017")
    database = mongo_client['todo-app']
    collection = database['tasks']

    def todo_app():
        while True:
            print("\n1. Add todo")
            print("2. List all todo")
            print("3. Find todo")
            print("4. Update todo")
            print("5. Delete todo")
            print("6. Exit todo")
            choice = input("Choose any operation to perform: ")

            if choice == "1":
                task_name = input("Enter your task name: ")
                task_description = input("Enter the task description: ")
                task_priority = input("Enter the task priority: ")
                task_status = input("Enter your task status: ")
                task = {
                    "name": task_name,
                    "description": task_description,
                    "priority": task_priority,
                    "status": task_status,
                    "created_at": datetime.now(),
                    "updated_at": None
                }
                collection.insert_one(task)
                print(f"'{task_name}' added successfully!")

            elif choice == "2":
                list_all_task = collection.find({})
                print("\nAll Todos:")
                for item in list_all_task:
                    print(f"Name: {item['name']}, Status: {item['status']}, Created: {item.get('created_at')}, Updated: {item.get('updated_at')}")

            elif choice == "3":
                user_input = input("Search any todo (by name): ")
                search_result = collection.find({"name": {"$regex": user_input, "$options": "i"}})
                found = False
                for item in search_result:
                    found = True
                    print(f"Name: {item['name']}, Status: {item['status']}, Created: {item.get('created_at')}, Updated: {item.get('updated_at')}")
                if not found:
                    print("Task not found!")

            elif choice == "4":
                search_text = input("Enter the task name that you want to update: ")
                existing = collection.find_one({"name": {"$regex":search_text,"$options":"i"}})
                if not existing:
                    print("Task not found!")
                    continue
                updated_task_name = input(f"Enter your updated task name [{existing['name']}]: ") or existing['name']
                updated_task_description = input(f"Enter the updated task description [{existing['description']}]: ") or existing['description']
                updated_task_priority = input(f"Enter the updated task priority [{existing['priority']}]: ") or existing['priority']
                updated_task_status = input(f"Enter your updated task status [{existing['status']}]: ") or existing['status']
                updated_task = {
                    "name": updated_task_name,
                    "description": updated_task_description,
                    "priority": updated_task_priority,
                    "status": updated_task_status,
                    "updated_at": datetime.now()
                }
                result = collection.update_one(
                    {"name": search_text},
                    {"$set": updated_task}
                )
                if result.modified_count > 0:
                    print("Task updated successfully!")
                else:
                    print("No changes made.")

            elif choice == "5":
                delete_task = input("Enter the task name that you want to delete: ")
                deleted_task_result = collection.delete_one({"name": delete_task})
                if deleted_task_result.deleted_count > 0:
                    print("Task deleted successfully.")
                else:
                    print("Task not found or not deleted.")

            elif choice == "6":
                print("Todo app exited successfully.")
                break

    todo_app()