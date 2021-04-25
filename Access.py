from Passport import Passport

def Target(passport: Passport, value):
    select = value.Get("target")

    if select == "Direct":
        return value.Get("value")
    else:
        raise Exception("Can't target this.")

def Source(passport: Passport, value):
    select = value.Get("source")

    if select == "Direct":
        return value.Get("value")

    elif select == "Load":
        return passport.builder.load(value.Get("value"))
    
    else:
        raise Exception("Can't source this.")