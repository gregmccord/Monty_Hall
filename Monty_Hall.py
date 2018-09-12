import random

def main():

    # Initialize constants and set seed for reproducibility
    random.seed(0)
    NUM_DOORS = 3
    NUM_TRIALS = 1000
    hist = [0,0] # to save trial results

    # Run each trial
    for trial in range(NUM_TRIALS):

        # Initialize doors, car location, and guess
        doors = [0] * NUM_DOORS
        car_loc = random.randrange(0,NUM_DOORS)
        guess = random.randrange(0,NUM_DOORS)
        doors[guess] = 1

        # If guessed right, choose a random other door to keep
        if guess == car_loc:
            subset = []
            for index in range(len(doors)):
                if doors[index] == 0:
                    subset.append(index)
            keep = subset[random.randrange(0,len(subset))]
        # If guessed wrong, choose the door that has the car
        else:
            keep = car_loc

        # If you swap, you get the kept door from the subset, else you get your original
        swap = keep
        no_swap = guess

        # Add values to histogram
        if swap == car_loc:
            hist[1] += 1
        else:
            hist[0] += 1

    # Find percent correct/incorrect
    percent_swap = float(hist[1]) / NUM_TRIALS * 100
    percent_no_swap = 100 - percent_swap

    # Print results
    print('With swapping, percent correct: %0.2f%%' % percent_swap)
    print('Without swapping, percent correct: %0.2f%%' % percent_no_swap)

if __name__ == '__main__':
    main()