with open('names.txt','r') as names_db:
    all_names = names_db.read()
    print(all_names)
    
    names_db =open('names.txt')
    all_names =names_db.read()
    print(all_names)
    names_db.close