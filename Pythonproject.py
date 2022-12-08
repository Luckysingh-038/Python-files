def nameRank(name,marks,updates,n):
    #Array of students
    x=[[0 for j in range(3)] for i in range(n)]
    for i in range(n):
        #Store the name of the student
        x[i][0] = names[i]
        #Update the marks of the student
        x[i][1]=marks[i] + updates[i]
        #Store the current rank of the student
        x[i][2] = i+1
    highest=x[0]
    for j in range(1,n):
        if(x[j][1] >= highest[1]):
            highest = x[j]

    #Print the name and jump in rank
    print("Name: ",highest[0],",jump: ",abs(highest[2]-1),sep="")

#Driver code
#Names of the students
names = ["sachin","rahul","aman"]
marks = [80, 90, 75]
updates = [0, 5, -9]

#number of students
n = len(marks)
nameRank(names,marks,updates,n)