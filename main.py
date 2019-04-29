import inquirer

def search_by_range(y1, y2):
    with open("bestsellers.txt", "r") as file:
        for line in file:
            if int(line.split("\t")[3].split("/")[2]) in range(y1, y2):
                print("\t" + line.split("\t")[0] + ", by " + line.split("\t")[1] + ' (' + line.split("\t")[3] + ')')

def search_by_month(m, y):
    with open("bestsellers.txt", "r") as file:
        for line in file:
            if line.split("\t")[3].split("/")[2] == y and line.split("\t")[3].split("/")[0] == m:
                print("\t" + line.split("\t")[0] + ", by " + line.split("\t")[1] + ' (' + line.split("\t")[3] + ')')

def search_by_author(name):
    with open("bestsellers.txt", "r") as file:
        for line in file:
            if name.lower() in line.split("\t")[1].lower():
                print("\t" + line.split("\t")[0] + ", by " + line.split("\t")[1] + ' (' + line.split("\t")[3] + ')')

def search_by_title(title):
    with open("bestsellers.txt", "r") as file:
        for line in file:
            if title.lower() in line.split("\t")[0].lower():
                print("\t" + line.split("\t")[0] + ", by " + line.split("\t")[1] + ' (' + line.split("\t")[3] + ')')

while True:
    options = [
    inquirer.List('opt',
                    message="What would you like to do?",
                    choices=['1: Look up year range', '2: Look up month/year', '3: Search for author', '4: Search for title', 'Q: Quit'],
                ),
    ]
    choises = inquirer.prompt(options)

    if choises['opt'][0] == '1':
        begin = input("Enter beginning year: ")
        end = input("Enter ending year: ")

        print(f"\nAll Titles between {begin} and {end} : ")
        search_by_range(int(begin), int(end)+1)
        print("\n")

    elif choises['opt'][0] == '2':
        month = input("Enter month (as a number, 1-12): ")
        year = input("Enter year: ")

        print(f"\nAll Titles in month {month} of {year} : ")
        search_by_month(month, year)
        print("\n")
        
    elif choises['opt'][0] == '3':
        author = input("Enter an author's name (or part of a name): ")
        search_by_author(author)
        print("\n")

    elif choises['opt'][0] == '4':
        title = input("Enter a title (or part of a title): ")
        search_by_title(title)
        print("\n")

    elif choises['opt'][0] == 'Q':
        exit()