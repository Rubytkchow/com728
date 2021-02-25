def escape_by(the_plan):
    # print("What way should we escape?")
    # the_plan = input()
    if the_plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif the_plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif the_plan == "going deeper":
        print("That might just work! Lets go deeper!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")