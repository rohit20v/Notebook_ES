import re

if __name__ == '__main__':
    recipe = "oliva\t, pepe,cappero ,\n detersivo,\t \n cappero, peperone, acciuga ,oliva , pepe\t,\t cappero , \noliva,pasta\n"

    recipeList = re.split(r'[\t \n ,]+', recipe)

    print(recipeList)

    olive = recipeList.count("oliva")
    pepe = recipeList.count("pepe")
    cappero = recipeList.count("cappero")
    print("", olive, "Olive\n", pepe, "Pepe\n", cappero, "Cappero")