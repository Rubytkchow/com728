def observed():
    observations = []
    for count in range(5):
        print("Please enter an observation:")
        observations.append(input())

    return observations

def remove_observation(observations):
    is_running = True
    print("Do you wish to remove observations?")

    while(is_running):
        print("Yes or No?")
        response = input()

        if (response == "yes"):
            print("What observation would you like removed?")
            remove_observation = input()
            observations.remove(remove_observation)
        else:
            is_running = False

def run():
    observations = observed()
    remove_observation(observations)

    observations_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)

    print(observations_set)

run()
