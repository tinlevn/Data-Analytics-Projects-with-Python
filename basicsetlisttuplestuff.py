#CS433 Semo Class project. JD and I contributed most of the code. 
#All questions are in this one jupyter notebook file with corresponding comments.

def exec_questions():
# Py Prog to count string len > 2 and check whether it's a palindrome from a list of strings. 
# data
question1_strings = ['4224', 'i', 'aa', '', 'car', 'yoppoy','', 'Wow','Mom','No lemon, no melon','asdfbc']
# solution
palindrome_count = len([s for s in question1_strings if len(s) >= 2 and s[::-1] == s])
print('Question 1 Result: {}'.format(palindrome_count))
    
#Py Prog that takes two lists and returns the number of common members
# data
    l1 = ['python', 'soccer', '', 'basketball', 'racecar','beer','sugar','keyboard']
    l2 = ['racecar', 'buffet', 'baseball','keyboard','bee','salt']
    # solution
    common_members = list(set(l1) & set(l2))
    print('Question 2 Result: {}'.format(common_members))
    
# Py prog that splits a list into a list of dictionaries, with odd item as key and even item as value
# data
    l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# solution
    odd_even_dict = [{k: v} for k, v in zip(l1[::2], l1[1::2])]
    print('Question 3 Result: {}'.format(odd_even_dict))
    

# Py to find a word which has the most number of letters from a list of words.
# data
    l1 = ['cardiologist', 'dermatologist', 'doctor', 'optologist', 'dentist', 'surgeon', 'proctologist', 'psychologist']
# solution
    max_len_word = max(l1, key=lambda x: len(x))
    print('Question 4 Result: {}'.format(max_len_word))
    
    
# Py prog to print all common values in a dictionary
# data
    dict1 = {0: 'MOm', 1: 'elephant', 2: 'data', 3: 'MOm', 4: 'elephant', 5: 'bird', 6: 'bees', 7: 'bird'}
# solution
    repeating_vals = list(set([v for v in dict1.values() if list(dict1.values()).count(v) > 1]))
    print('Question 5 Result: {}'.format(repeating_vals))

    
# Py Prog that combinres two dictionaries based on their keys, 
#if two keys are the same, sum their values together
# data
    dict1 = {'one': 1, 'two': -7, 'three': 3, 'four': 9,'six':6}
    dict2 = {'one': 15, 'two': 2, 'four': 4, 'three': 3,'five':2}
# solution
    new_dict = {k: v+dict2[k] if dict2.get(k) else v for k, v in dict1.items()}
    new_dict.update({k: v for k, v in dict2.items() if not dict1.get(k)})
    print('Question 6 Result: {}'.format(new_dict))
    
    
# Py Prog to remove tuple(s) which has certain given value from a list of tuples
# data
    l1 = [(1, 2, 3, 4), (4, 5, 6, 7), (8, 9, 10), (2, 3, 1), (0, 11, 23)]
    l2 = [(1, 2, 3, 4), (3, 5, 0, 7), (5, 6, 11), (2, 3, 1), (2, -5, 19)]
    value = 4
    val = 2
    # solution
    l1 = list(filter(lambda x: value not in x, l1))
    l2 = list(filter(lambda x: val not in x, l2))
    print('Question 7 Result: {}'.format(l1))
    print('Question 7 Result: {}'.format(l2))
    
    
# Py Prog to sort a list of tuples by the first element in the tuple
# data
    l1 = [(4, 5, 6, 7), (1, 2, 3, 4), (7, 9, 10),(9, 3, -1, 0),(-2, 5, 11, 22)]
    l2 = [('car', 'bike', 'train'), ('airplane', 'rocket', 'yatch'), ('helicopter', 'submarine', 'jet'),
          ('scooter','bullet train')]
    # solution
    l1 = sorted(l1, key=lambda x: x[0])
    l2 = sorted(l2, key=lambda x: x[0])
    print('Question 8 Result: {}'.format(l1))
    print('Question 8 Result: {}'.format(l2))


if __name__ == '__main__':
    exec_questions()
#Alternative solutions to questions 2,3,4
#2
def findCommon(list1, list2):
    return set(list1) & set(list2)
#3
def listToDict(lst): 
    dict = {lst[i]: lst[i+1] for i in range(0, len(lst), 2)} 
    return dict 
#4
def mostLetter(wordl):
    result=''
    for word in wordl:
        if len(word)>len(result):
            result=word
    return result
 
