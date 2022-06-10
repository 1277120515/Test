from food import Food
import sys

def get_filename()-> tuple:
    '''
    Reads the command line arguments from sys to get the file name.
    Returns: result, tuple
    First element - bool, True for sufficient arguments. Otherwise, False.
    Second element - str, file path. Empty string if first element is False.
    '''
    # Write your answer for Question 2.1 here. 
    try:
        fn = sys.argv[1]
        return (True, fn)
    except Exception as e:
        print('Error: Insufficient arguments.')
        return (False, "")


def read_file(filename: str) -> list:
    '''
    Reads all the lines in the file and stores it in a list.
    Parameters: filename, str
    Returns: result, list
    '''
    # Write your answer for Question 2.2 here. 
    try:
        content = []
        with open(filename, 'r') as f:
            content = f.readlines()
        return (True, content)
    except Exception:
        print('Error: The file or directory cannot be found.')
        return (False, [])

def extract_contents(contents:list, food_cat: tuple) -> list:
    '''
    Extract menu details from the list of contents retrieved from the file.
    Parameters: 
      contents, list
      food_cat, tuple
    Returns: menu_items, list of tuples
    '''
    # Write your answer for Question 2.3 here.

    menu_items = []
    i = 0
    while i<len(contents):
        category = contents[i].strip()[:-1]
        name = contents[i + 1].strip()
        desp = contents[i + 2].strip()
        if i + 3 < len(contents):
            ingre = contents[i + 3].strip()
        else:
            ingre = ''
        if ingre == '':
            items = []
            i += 4
        else:
            words = ingre.split(' - ')[1]
            items = [item.strip() for item in words.split(',') if item.strip()]
            i += 5
        m = (name, desp, items, category)
        if category in food_cat:
            menu_items.append(m)
    return menu_items

#t, content = read_file('ii.txt')
#menu_items = extract_contents(content, ["Appetizers","Mains",""])


# Main program
def main(menu_list=[]):
    # Write your answer for Question 2.5.2 here.
    print(f"Menu has {len(menu_list)} items!")
    for item in menu_list:
        name, desp, items, category = item

        food = Food(catetory, name, desp, items)

#if __name__ == "__main__":
#    args_success = True
#    # args_success, fname = get_filename()
#    # Write your answer for Question 2.5.1 here.
#    if args_success:
#        succ, content = read_file('ii.txt')
#        #succ, content = read_file(fname)
#        if succ:
#            menu_items = extract_contents(content, ["Appetizers","Mains",""])
#            main(menu_items)

if __name__ == "__main__":
    args_success = True
    args_success, fname = get_filename()
    # Write your answer for Question 2.5.1 here.
    if args_success:
        # succ, content = read_file('ii.txt')
        succ, content = read_file(fname)
        if succ:
            menu_items = extract_contents(content, ["Appetizers","Mains",""])
            main(menu_items)