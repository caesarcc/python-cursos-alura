def validate_Name(value):
    return str(value).__len__() > 3
def validate_Age(value):
    return 0 < int(value) < 150
def validate_Salary(value):
    return float(value) > 0
def validate_Sex(value):
    v = str(value)
    return (v == 'f') | (v == 'm')
def validate_Martial(value):
    v = str(value)
    return (v == 's') | (v == 'c') | (v == 'v') | (v == 'd')

swicher = {
    1 : validate_Name,
    2 : validate_Age,
    3 : validate_Salary,
    4 : validate_Sex,
    5 : validate_Martial,
}

questions = [(1,'name'), (2,'age'), (3,'salary'), (4,'sex'), (5,'martials')]

def fill_form():
    print("============================================================")
    for q in questions:
        try:
            question = "Please, inform your " + q[1] + "? "
            if swicher[q[0]](input(question)) :
                print("Your " + q[1] + " is valid!")
                continue
            else:
                fill_form()
                break
        except:
            print("Inputed value is unformatted!")
            break


fill_form()
