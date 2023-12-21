if __name__ == '__main__':
    fauna = ["cippimerli",
             "gufolanti",
             "branchisauri",
             "cumulognembi",
             "arzigovolanti",
             "rotototteri",
             "barbagianni"]

    [print(elem[0][:4] + elem[1][4:]) for elem in zip(fauna, fauna[::-1])]
