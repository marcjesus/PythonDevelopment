#Challenge: 
#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
#Print the average of the marks array for the student name provided, showing 2 places after the decimal.


if __name__ == '__main__':
    student_marks = {'Marc': [46.0, 24.0, 53.0], 'Krishna': [44.0, 32.0, 84.0]} 
    print("Introduce number of students:")

    """
    n = int(input())
    student_marks = {}
    print("Introduce names and scores -> Krishna 67 68 69")
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    """
    print(f"Student marks {student_marks}")
    print("What student do you want to check the average")
    query_name = input()    
    
    def calculate_avg_marks(student_marks):
        avg_marks = {}
        for name, scores in student_marks.items():
            avg_marks[name] = sum(scores) / len(scores)
        return avg_marks
        

    avg_marks = calculate_avg_marks(student_marks)    
    for name, avg in avg_marks.items():  # Changed 'avg_marks' to 'avg' for clarity
        if name == query_name:
            print("{:.2f}".format(avg))
    
    