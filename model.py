
object_array=[{"hello" , 0},{"beans",1},{"pumking" , 2},{"hello" , 0},{"cucumber",4},{"halmasso",5},{"chicken",6}]

perscentage = [[0,0,0,0,0,0,0],[0,100,100 , 0 , 50 , 100, 80],[0,100 , 100 , 0, 100 , 100 ,80],[0,0,0,0,0,0,0] , [0,50, 100,0,100 , 70 ,40 ],[0 , 100 , 100 , 0 , 70 , 100 , 30],[0 , 80 , 80 , 0 , 40 , 30 , 100]]

vege_menu = []
stew_menu = []
meat_menu = []

suitable_couples = []

def returnObj(x , y):
    return {
        "first":x,
        "second":y
    }




def list_mostSuitable_couple():
    for i in range(len(vege_menu)-1):
        for j in range(i+1 , len(vege_menu)):
            if perscentage[vege_menu[i]][vege_menu[j]] == 100:
                suitable_couples.append(returnObj(vege_menu[i] , vege_menu[j]))


def set_menu(vege_menu1 , stew_menu1 , meat_menu1):
    vege_menu.clear()
    meat_menu.clear()
    stew_menu.clear()
    while vege_menu1:
        vege_menu.append(vege_menu1.pop())

    vege_menu.reverse()

    while stew_menu1:
        stew_menu.append(stew_menu1.pop())

    stew_menu.reverse()

    while meat_menu1:
        meat_menu.append(meat_menu1.pop())

    meat_menu.reverse()
    list_mostSuitable_couple()

set_menu([1,2,4],[5],[6])
print(vege_menu)



def suitability_of_couple(Id1 , Id2):
    return perscentage[Id1][Id2]

print(suitability_of_couple(1,4))

def returnStewSuitabilityOBJ(x , y):

    return {
        "id" : x,
        "suitability":y
    }


def stew_suitability(Id1 , Id2):
    stew_suitability = []

    for i in stew_menu:
        suitability = (perscentage[i][Id1] + perscentage[i][Id2])/2
        stew_suitability.append(returnStewSuitabilityOBJ(i , suitability))
    return stew_suitability



def meet_suitability(Id1 , Id2 , Id3):
    meat_suitability = []

    for i in meat_menu:
        suitability = (perscentage[i][Id1] + perscentage[i][Id2] + perscentage[i][Id3]) / 3
        meat_suitability.append(returnStewSuitabilityOBJ(i , suitability))
    return meat_suitability


def final_suitability(param_list):
    total_suitability = 0
    for i in range(len(param_list)-1):

        for j in range(i+1 , len(param_list)):
            total_suitability+=perscentage[param_list[i]][param_list[j]]
            print(total_suitability)

    return total_suitability/6

print(final_suitability([1,2,5,6]))