# toyeade1-100DaysofCoding-Day5-Challenge-RandomPasswordGenerator


the goal for this was creating a random password generator and it was actually a bit confusing at first. The key to it was breaking down each step. The password would be able to include letters, numbers and symbols so the first step was creating loops for each of the lists with these symbols. i would use the random.choice function to randomly select an item in the predefined library for each, after doing this, i would add those items to a list to create a list with all the requested parameters. The next step was shuffling this list using the random.shuffle function and then converting the shuffled list back into a string. This was done using a loop that went through each item in the list and added it to an empty list i had created.
