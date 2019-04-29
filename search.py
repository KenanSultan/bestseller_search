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
