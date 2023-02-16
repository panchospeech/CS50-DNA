import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit('Usage: python dna.py data.csv sequence.txt')

    # TODO: Read database file into a variable

    database = []

    # Open the file and read it
    with open(sys.argv[1], 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            # This returns as a list of strings
            database.append(row)

    # TODO: Read DNA sequence file into variable

    with open(sys.argv[2], 'r') as txtfile:
        dna_sequence = txtfile.read()

    # TODO: Find longest match of each STR in DNA sequence
    # Store the subsequences into a list (f.e / [AGAT, AATG, TATC])
    # Use keys() which will return the keys of the dictionary as a list

    subsequences = list(database[0].keys())[1:]  # We dont need the name of the header, so we start from the 1st position, not the 0

    # Run through the DNA sequence and look for the longest sequence of each subsequence

    result = {}  # creates a dictionary
    # Iterate through each subsequence in the list subsequences just created

    for subsequence in subsequences:
        # Apply the function and store it in results dictionary accordingly to each subsequence
        result[subsequence] = longest_match(dna_sequence, subsequence)

    # TODO: Check database for matching profiles

    # Go through each person in database (each element of the list of strings)
    for person in database:
        match = 0
        # Iterate trough each subsequence of the list subsequences
        for subsequence in subsequences:
            # if there is a match between a person subsequence value and the longest_match result for each subsequence
            if int(person[subsequence]) == result[subsequence]:
                match += 1

        # If all subsequence are matched
        if match == len(subsequences):
            print(person['name'])
            return

    print('No match')

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
