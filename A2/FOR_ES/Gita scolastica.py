def chunks(lst):
    for _ in range(0, len(lst), 3):
        yield lst[_:_ + 3]


if __name__ == '__main__':
    students = ['M_Alessandro', 'F_Alessia', 'F_Alice', 'M_Andrea', 'F_Anna', 'F_Arianna', 'F_Aurora',
                'F_Beatrice', 'F_Bianca', 'F_Camilla', 'F_Chiara', 'M_Federico', 'M_Francesco', 'M_Gabriele',
                'F_Gaia', 'F_Ginevra', 'F_Giorgia', 'F_Giulia', 'M_Giuseppe', 'F_Greta', 'M_Leonardo', 'M_Lorenzo',
                'F_Ludovica', 'M_Matteo', 'M_Mattia', 'M_Merlino', 'F_Nicole', 'M_Nicolo', 'F_Noemi', 'M_Riccardo',
                'F_Sara', 'F_Sofia', 'M_Tommaso', 'F_Vittoria']

    male = []
    female = []
    maleWith_M = []
    femaleWith_F = []
    for student in students:
        if student[0] == 'M':
            maleWith_M.append(student)
            male.append(student[2:])
        elif student[0] == 'F':
            femaleWith_F.append(student)
            female.append(student[2:])

    print("Male: ", maleWith_M)
    print("Male: ", male)
    print("Female: ", femaleWith_F)
    print("Female: ", female)

    for _ in chunks(male):
        print("Male: ", _)

    for i in chunks(female):
        print("Female: ", i)
