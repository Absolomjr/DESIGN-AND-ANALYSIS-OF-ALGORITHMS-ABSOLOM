import datetime
from bisect import bisect_left
import matplotlib.pyplot as plt


# Task class
class Task:
    def __init__(self, name, task_type, priority, start_time, end_time, deadline):
        self.name = name
        self.task_type = task_type  # 'personal' or 'academic'
        self.priority = priority
        self.start_time = start_time
        self.end_time = end_time
        self.deadline = deadline

    def __repr__(self):
        return (f"{self.name} ({self.task_type}): Priority {self.priority}, "
                f"Start: {self.start_time}, End: {self.end_time}, Deadline: {self.deadline}")


# Task Manager class
class TaskManager:
    def __init__(self):
        self.tasks = []

    # Add a new task
    def add_task(self, name, task_type, priority, start_time, end_time, deadline):
        task = Task(name, task_type, priority, start_time, end_time, deadline)
        self.tasks.append(task)

    # Search for a task by deadline using binary search
    def find_task_by_deadline(self, deadline):
        deadlines = sorted([task.deadline for task in self.tasks])
        index = bisect_left(deadlines, deadline)
        if index < len(deadlines) and deadlines[index] == deadline:
            for task in self.tasks:
                if task.deadline == deadlines[index]:
                    return task
        return None

    # Sort tasks by a given key
    def sort_tasks(self, key):
        def merge_sort(tasks, key):
            if len(tasks) > 1:
                mid = len(tasks) // 2
                left_half = tasks[:mid]
                right_half = tasks[mid:]

                merge_sort(left_half, key)
                merge_sort(right_half, key)

                i = j = k = 0
                while i < len(left_half) and j < len(right_half):
                    if getattr(left_half[i], key) < getattr(right_half[j], key):
                        tasks[k] = left_half[i]
                        i += 1
                    else:
                        tasks[k] = right_half[j]
                        j += 1
                    k += 1

                while i < len(left_half):
                    tasks[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    tasks[k] = right_half[j]
                    j += 1
                    k += 1

        merge_sort(self.tasks, key)

    # Optimise schedule using dynamic programming (Weighted Interval Scheduling)
    def optimise_schedule(self):
        sorted_tasks = sorted(self.tasks, key=lambda t: t.end_time)
        n = len(sorted_tasks)

        # Compute p(i): the index of the last non-overlapping task
        def find_previous_task(index):
            for j in range(index - 1, -1, -1):
                if sorted_tasks[j].end_time <= sorted_tasks[index].start_time:
                    return j
            return -1

        p = [find_previous_task(i) for i in range(n)]

        # DP array to store maximum utility
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            include_utility = sorted_tasks[i - 1].priority + (dp[p[i - 1] + 1] if p[i - 1] != -1 else 0)
            dp[i] = max(dp[i - 1], include_utility)

        # Reconstruct optimal task set
        optimal_tasks = []
        i = n
        while i > 0:
            if sorted_tasks[i - 1].priority + (dp[p[i - 1] + 1] if p[i - 1] != -1 else 0) > dp[i - 1]:
                optimal_tasks.append(sorted_tasks[i - 1])
                i = p[i - 1] + 1
            else:
                i -= 1

        return list(reversed(optimal_tasks))

    # Visualise tasks using a Gantt chart
    def create_gantt_chart(self, tasks):
        fig, ax = plt.subplots()
        for i, task in enumerate(tasks):
            start = (task.start_time - datetime.datetime(1970, 1, 1)).total_seconds()
            end = (task.end_time - datetime.datetime(1970, 1, 1)).total_seconds()
            ax.broken_barh([(start, end - start)], (i * 10, 9), facecolors=('tab:blue' if task.task_type == 'academic' else 'tab:orange'))

        ax.set_yticks([i * 10 + 5 for i in range(len(tasks))])
        ax.set_yticklabels([task.name for task in tasks])
        ax.set_xlabel('Time (seconds since 1970-01-01)')
        plt.show()


# Main application loop
def main():
    manager = TaskManager()

    while True:
        print("\nPersonal Scheduling Assistant")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Find Task by Deadline")
        print("4. Sort Tasks")
        print("5. Optimise Schedule")
        print("6. Visualise Gantt Chart")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Task Name: ")
            task_type = input("Task Type (personal/academic): ")
            priority = int(input("Priority (higher is better): "))
            start_time = datetime.datetime.strptime(input("Start Time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
            end_time = datetime.datetime.strptime(input("End Time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
            deadline = datetime.datetime.strptime(input("Deadline (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
            manager.add_task(name, task_type, priority, start_time, end_time, deadline)
        elif choice == '2':
            for task in manager.tasks:
                print(task)
        elif choice == '3':
            deadline = datetime.datetime.strptime(input("Enter Deadline (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
            task = manager.find_task_by_deadline(deadline)
            print(task if task else "No task found with the given deadline.")
        elif choice == '4':
            key = input("Sort by (name, task_type, priority, start_time, end_time, deadline): ")
            manager.sort_tasks(key)
            print("Tasks sorted!")
        elif choice == '5':
            optimal_tasks = manager.optimise_schedule()
            print("Optimal Task Schedule:")
            for task in optimal_tasks:
                print(task)
        elif choice == '6':
            manager.create_gantt_chart(manager.tasks)
        elif choice == '7':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
