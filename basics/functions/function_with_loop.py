def cross_bridge(in_steps):
    for step in range (in_steps):
        print("Crossed step")

    if in_steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")

cross_bridge(3)
cross_bridge(6)