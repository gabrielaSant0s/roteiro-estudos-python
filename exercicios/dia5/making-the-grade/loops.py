def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    round_student_scores =[]
    for grade in student_scores:
        new_grade = round(grade)
        round_student_scores.append(new_grade)
    return round_student_scores

def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    cont = 0
    for grade in student_scores:
        if grade <= 40:
            cont +=1
    return cont

def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    new_student_scores = []
    for grade in student_scores:
        if grade >= threshold:
            new_student_scores.append(grade)
    return new_student_scores

def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:
             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    rate = round((highest-40)/4)
    d = 41
    c = 41+rate
    b = c+rate
    a = b+rate 

    return [d,c,b,a]

def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    list_student_ranking = []
    for (rank, score, name) in zip(range(len(student_scores)), student_scores, student_names):
        list_student_ranking.append(f'{rank+1}. {name}: {score}')
    return list_student_ranking

def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for student in student_info:
        if student[1] == 100:
            return student
    return []

