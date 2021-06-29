# Задание 6
subjects = open("hw5ex6")
subjects_dict = {}
for line in subjects:
    subjects_new = line.replace("(", " (").split()
    subjects_dict[subjects_new[0][:-1]] = sum(int(hours) for hours in subjects_new if hours.isdigit())
print(subjects_dict)
subjects.close()