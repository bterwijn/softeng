import math

def main():
    print("q1:", question1() )
    print("q2:", question2() )
    print("q3:", question3() )
    print("q4:", question4() )
    print("q5:", question5() )
    print("q6:", question6() )
    print("q7:", question7() )
    print("q8:", question8() )

def permutation_repetition(n: int, r:int) -> int:
    """ Returns the number of permutations of choosing
    'n' different things 'r' times with repetition.
    """
    raise NotImplementedError()

def permutation(n: int, r:int) -> int:
    """ Returns the number of permutations of choosing
    'n' different things 'r' times without repetition.
    """
    raise NotImplementedError()

def combination(n: int, r:int) -> int:
    """ Returns the number of combinations of choosing
    'n' different things 'r' times without repetition.
    """
    raise NotImplementedError()

def combination_repetition(n: int, r:int) -> int:
    """ Returns the number of combinations of choosing
    'n' different things 'r' times with repetition.
    """
    raise NotImplementedError()

# ----------------- Questions -----------------

def question1() -> int:
    """ There are 2174 students at a university. A group
    of 40 students are selected to participate in a
    special program. How many ways can the group be selected?
    """
    raise NotImplementedError()

def question2() -> int:
    """ A passwords consists of 16 characters that each can be:
    - lower case letter (26)
    - upper case letter (26)
    - number (10)
    - or special character (32)
    How many possible passwords are there?
    """
    raise NotImplementedError()

def question3() -> int:
    """ A theater has 200 seats and 189 people are attending
    a performance. How many different ways can the people be 
    seated?
    """
    raise NotImplementedError()

def question4() -> int:
    """ There are 50.000 voters expected to vote in an election.
    The election has 12 candidates where each voter has to choose 
    one from. How many ways can the votes be distributed?
    """
    raise NotImplementedError()

def question5() -> int:
    """ A passwords consists of at least 6 and at most 20 
    characters that each can be:
    - lower case letter (26)
    - upper case letter (26)
    - number (10)
    - or special character (32)
    How many possible passwords are there?
    """
    raise NotImplementedError()

def question6() -> int:
    """ A vending machine has 425 coins. There are only 1, 2, 
    5, 10, 25, 50, 100 and 200 cent coins. How many different
    total amounts of money can be in the machine?
    """
    raise NotImplementedError()

def question7() -> int:
    """ How many unique words do you get with all 
    rearrangments of the letters in the word "MISSISSIPPI"?
    ("MISSISSIPPI" itself counts as one as these unique
    words)
    """
    raise NotImplementedError()

def question8() -> int:
    """ A passwords consists of characters that each can be:
    - lower case letter (26)
    - upper case letter (26)
    - number (10)
    - or special character (32)
    What is the minimal length of password that we need to have
    10e18 (one quintillion) possible passwords of that length?
    """
    raise NotImplementedError()

if __name__ == "__main__":
    main()
