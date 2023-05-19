"""
Project Management Program
Time estimate: 5 hours
"""

import os
import datetime
from operator import attrgetter
from project import Project


def main():
    projects = load_projects("projects.txt")
    menu(projects)


def load_projects(filename):
    projects = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            file.readline()
            for line in file:
                parts = line.strip().split("\t")
                date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
                project = Project(parts[0], date, parts[2], parts[3], parts[4])
                projects.append(project)
    return projects


def save_projects(projects, filename):
    with open(filename, "w") as file:
        file.write("Name\tStart\tPriority\tCost Estimate\tPercent Complete\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.percent_complete}\n")


def menu(projects):
    choice = ""
    while choice.lower() != "q":
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()

        if choice == "l":
            filename = input("Enter the filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter the filename to save projects to: ")
            save_projects(projects, filename)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            projects.append(add_new_project())
        elif choice == "u":
            update_project(projects)

    print("Thank you for using custom-built project management software.")


def display_projects(projects):
    incomplete_projects = sorted([project for project in projects if project.percent_complete < 100],
                                 key=attrgetter('priority'))
    completed_projects = sorted([project for project in projects if project.percent_complete == 100],
                                key=attrgetter('priority'))

    print("\nIncomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects: ")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered_projects = sorted([project for project in projects if project.start_date > date],
                               key=attrgetter('start_date'))

    for project in filtered_projects:
        print(f"  {project}")


def add_new_project():
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))  # Convert to int
    cost_estimate = input("Cost estimate: ")
    percent_complete = int(input("Percent complete: "))  # Convert to int

    return Project(name, start_date, priority, cost_estimate, percent_complete)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    print(project)

    new_percent = input("New Percentage: ")
    if new_percent:
        project.percent_complete = int(new_percent)

    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)


if __name__ == "__main__":
    main()
