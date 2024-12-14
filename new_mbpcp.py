#Marcus Becker Bounded PCP implemented from csci561 final
#Claude.ai used for some code generation
#test cases sourced from https://github.com/bbrown683/bounded-pcp-solver


from itertools import product

#constructs the RL as described in problem3 on the exam
#this is a brute force construction of regular language of 
# all possible strings for the A or B domino sections
#Importantly, this construction concatenates the reversed
#indices (Xn)of the domino components for each string
#this is exactly what we described in class to ensure the actual dominos
#used are a proper match 
def construct_rl(dominos, k):
#Steps 3 and 4 on my proof
    """
    Construct a regular language of strings using given dominos
    
    Args:
    - dominos: List of domino strings
    - k: Maximum number of dominos to use
    
    Returns:
    - List of generated strings with appended reversed indices
    """
    lang = []
    for j in range(1, k + 1):
        for indices in product(range(len(dominos)), repeat=j):
            # Construct string from selected dominos
            data = "".join(dominos[i] for i in indices)
            # Append reversed indices
            # idxs = "".join(map(str, indices[::-1]))
            idxs = "".join(f"X{i}" for i in indices[::-1])
            lang.append(data+idxs)
    return lang 
#In my answer on the exam, I did describe the inclusion of these Xn indices
#to ensure the strings are unique, but the actual construction of the regular 
#languages is through brute force
#Importantly, that construction of RLs is totally valid here for the finite possibilities 
#I did all this because of the full credit rubric option 
# "Correct: decidable because brute force now works"
# feels like the algorithm I provided



# This Function takes the intersection of the brute-force generated
#regular languages of possible strings, which is all that is needed to 
#filter actual matching strings, since they include Xn indices
def becker_pcp(A, B, k):
#Step 5 on my proof

    """
    Solve Bounded Post Correspondence Problem
    
    Args:
    - A: First set of dominos
    - B: Second set of dominos
    - k: Maximum number of dominos to use
    
    Returns:
    - List of matching strings
    """
    # Generate languages for A and B
    Ra = construct_rl(A, k)
    Rb = construct_rl(B, k)
    
    # Find intersection of languages
    Rbpcp = list(set(Ra) & set(Rb))
    
    return Rbpcp


if __name__ == "__main__":

    test_cases = [
        {
            'A': ['a', 'ab', 'bba'],
            'B': ['baa', 'aa', 'bb']
        },
        {
            'A': ['110', '0011', '0110'],
            'B': ['110110', '00', '110']
        },
        {
            'A': ['abab', 'aaabbb', 'aab', 'ba', 'ab', 'aa'],
            'B': ['ababaaa', 'bb', 'baab', 'baa', 'ba', 'a']
        }
        #Test PCP dominos that I provided on the exam. Not a valid example/solution
        #sorry i wasn't able to come up with matching dominos under pressure
        # {
        #     'A': ["1", "01"],
        #     'B': ["01", "1"]
        # }
    ]
    
    #output.txt decides T/F for a given max K, the actual official problem instance 
    #increment_out.txt starts with k=1 and increments until a match is detected
    # 
    maxk=12
    for case in test_cases:
        k=1
        bmatch = False
        while bmatch == False:
            if k > maxk:
                print("QUITTING: k exceeds threshold of ", maxk)
                break
            print("\nTest Case:")
            print(f"A: {case['A']}, B: {case['B']}, k: {k}")
            results = becker_pcp(case['A'], case['B'], k)

            if results:
                print("TRUE with k=", k)
                print("Matches found:")
                
                for match in results:
                    print(match)
                    #unnecessary to reconstruct this but I wanted to print it when match is found
                    print("Ra: ", construct_rl(case['A'], k))
                    print("Rb: ", construct_rl(case['B'], k))
                    print("Intersection: ", results)
                    
                bmatch=True
                # k=k+1
            else:
                # print("FALSE with k=", k)
                # break
                k=k+1
                # print("No matches found, increasing k to ", k)
                
                