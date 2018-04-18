from sys import argv

def exam_grade(std_dev_of_scores, average_of_scores):
    #grades are determined based on the following:
    #>3/2 standard devation from mean = A
    #+1/2 to 3/2 standard deviation from mean = B
    #+/- 1/2 standard deviation from mean = C
    #-1/2 - -3/2 standard deviation from mean = D
    #- 3/2 or less standard deviation from mean = F
    examinee_score = int(input("What was your score on the exam?\n"))
    if(examinee_score < average_of_scores - 1.5 * std_dev_of_scores):
        print("Your grade is an F.")
    elif(examinee_score < average_of_scores - 0.5 * std_dev_of_scores and examinee_score >= average_of_scores - 1.5 * std_dev_of_scores):
        print("Your grade is a D.")
    elif(examinee_score < average_of_scores + 0.5 * std_dev_of_scores and examinee_score >= average_of_scores - 0.5 * std_dev_of_scores):
        print("Your grade is a C.")
    elif(examinee_score < average_of_scores + 1.5 * std_dev_of_scores and examinee_score >= average_of_scores + 0.5 * std_dev_of_scores):
        print("Your grade is a B.")
    else:
        print("Your grade is an A.")
    
exam_grade(2, 50)

std_dev = int(input("What is the standard deviation of the exam scores?\n"))
avg = int(input("What is the average exam grade?\n"))

exam_grade(std_dev, avg)

exam_grade(int(open('std_dev.txt').read()), int(open('avg.txt').read()))

exam_grade(13-10,100/2)

script, arg_std_dev, arg_avg = argv

exam_grade(int(arg_std_dev), int(arg_avg))
exam_grade(18/3,500/5)
exam_grade(10+10,25*4)
exam_grade(200/20,10**2)
exam_grade(13,10*5-4)
exam_grade(6/3,25/5*4)