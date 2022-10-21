def give_mark(stud):
    if stud["sex"] == "M":
        if stud["class"] == "6":
            if stud["time"] <= 9.9:
                mark = 5
            elif stud["time"] <= 10.4:
                mark = 4
            elif stud["time"] <= 11.1:
                mark = 3
            else:
                mark = 2
        else:
            if stud["time"] <= 9.4:
                mark = 5
            elif stud["time"] <= 10.2:
                mark = 4
            elif stud["time"] <= 11.0:
                mark = 3
            else:
                mark = 2
    else:
        if stud["class"] == "6":
            if stud["time"] <= 10.3:
                mark = 5
            elif stud["time"] <= 10.6:
                mark = 4
            elif stud["time"] <= 11.2:
                mark = 3
            else:
                mark = 2
        else:
            if stud["time"] <= 9.8:
                mark = 5
            elif stud["time"] <= 10.6:
                mark = 4
            elif stud["time"] <= 11.4:
                mark = 3
            else:
                mark = 2
    return mark

def toString(stud):
    stud_str = stud["name"] \
    + "  " + stud["sex"] \
    + "  " + stud["class"] \
    + "  " + str(stud["time"]) \
    + "  " + str(give_mark(stud))
    return stud_str

def byTime(stud):
    return (stud["time"])

def bySex(stud):
    return (stud["sex"])

studs = []
with open("run_of_60_m.txt","r") as f:
    for line in f:
        l = line.split()
        student = {"name":l[0],"sex":l[1],"class":l[2],"time":float(l[3])}
        studs.append(student)
f.close()
with open("run_of_60_mark.txt","w") as f:
    for i in studs:
        f.write(i.get("name") + " " + str(give_mark(i)) + "\n")
f.close()
studs.sort(key=byTime)
if studs[0]["sex"] == "M":
    print("Самый быстрый студент: \n" + toString(studs[0]))
    for i in studs:
        if i["sex"] == "F":
            print("Самая быстрая студентка: \n" + toString(i))
            break
else:
    print("Самая быстрая студентка: \n" + toString(studs[0]))
    for i in studs:
        if i["sex"] == "M":
            print("Самая быстрая студентка: \n" + toString(i))
            break