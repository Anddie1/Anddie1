def myfunction(parameter: int) -> str: # parameter is expected to be an integer (-> meaning what is expected to be returned)
    return f'{parameter  + 10}'
print(myfunction(20))

def otherfunction(otherparameter: str): 
    print(otherparameter)


otherfunction(myfunction(30))

def dosth(params: list[int]):
    pass