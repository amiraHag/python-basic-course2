# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------

usrTuple=("One", "Two", "Three")
usrDict={
"One":1,
"Two":2,
"Three":3,
"Four":4
}

def show_tuple_dict(usrName, *usrTuple, **usrDict):
    print(f"Hello User : {usrName.strip().title()}")
    for usrTupleItem in usrTuple:
        print(f" - User Tuple Item : {usrTupleItem.strip().capitalize()}")
    for usrDictItem in usrDict:
        print(f" ---   User Dictionary Item: {usrDict[usrDictItem]}")

show_tuple_dict("Amira", *usrTuple, **usrDict)
