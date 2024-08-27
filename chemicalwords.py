
from chemify import chemify, chemify_words

# chemicalAbbrs = ['Fe', 'Na', 'Ag', 'Sn', 'Sb', 'W', 'Au', 'Hg', 'Pb', 'K', 'Cu',
#                  'B', 'C', 'F', 'H', 'I', 'N', 'O', 'P', 'S', 'U', 'V', 'Y',
#                  'Ac', 'Al', 'Am', 'Ar', 'Ba', 'Be', 'Bi', 'Br', 'Ca', 'Ce', 'Cl', 'Co', 'Dy',
#                  'Er', 'Eu', 'Fl', 'Fr', 'Ga', 'Ge', 'He', 'Ho', 'In', 'Ir', 'Kr', 'La', 'Li', 'Lu', 'Mo',
#                  'Ne', 'Ni', 'No', 'Og', 'Os']

# buildings = ['bollos', 'blacksburg books', 'gillies', 'bollos', 'greens', 'coop', 'puzzlr', 'live wire', 'sugar magnolia', 'new river art and fiber', 'blacksburg tavern', 'cabo', 'observatory', 'kent square', 'dental']
# buildings += ["New Hall West", "Cochrane", "Hancock", "Cassell", "Coliseum", "Graduate Life Center", "GLC", "Donaldson Brown", "Surge", "Space Building", "Hahn Hurst", "Basketball Practice Center", "Grove", "Goodwin", "Squires", "Student Center", "Inn", "Thomas", "Bishop-Favrao", "BF", "New Res East", "War", "Memorial", "Chapel", "Sochinski-McKee", "MVC", "Marching Virginians Center", "Jamerson", "Athletic Center", "Golf Course", "Theatre 101", "Burrows-Burleson", "Tennis Center", "Hutcheson", "Durham", "Dietrick", "Steger", "Williams", "Vawter", "Cowgill", "Payne", "Pritchard", "Major Williams", "Military Building", "Drillfield", "Lavery", "North End", "Health and Safety", "Harper", "smith", "Smith Career Center", "(Career and Professional Development)", "Solitude", "Skelton", "Skelton Conference Center", "University Bookstore", "Bookstore", "War Memorial", "Wallace", "Public Safety Building", "Miles", "Patton", "Price", "Moss", "Moss Arts Center", "Johnson", "Perry Street Parking", "Holtzman", "Alumni Center", "Lane Stadium", "Worsham Field", "Worsham", "Harry T. Peters Jr.", "Large Animal Clinic", "Fralin", "Life Science Institute", "Cheatham", "Seitz", "Torgersen", "Smyth", "Litton-Reaves", "Media Annex", "McBryde Hall", "McComas Hall", "Media Building", "Carol M. Newman Library", "Newman", "Pearson", "Pearson Hall East", "Oshag", "O'Shaughnessy Hall", "Latham", "Wright House", "Campbell", "Agnew", "Burchard", "Henderson", "Food Science", "Davidson", "Hahn", "Hahn North", "Hahn Hall-North Wing", "Saunders", "Whittemore", "Peddrew-Yates Residence", "Randolph", "Rector", "Field House", "Old Security", "Newman", "Biosciences I", "Hahn Garden", "Hahn Hort", "Horticulture Garden", "Student Services", "Parking Services", "Sterrett", "Hillcrest", "Engel", "Pamplin", "Merryman", "Athletic Facility", "Alphin-Stuart", "Livestock Teaching Arena", "Oak Lane", "Admissions", "Richard B. Talbot", "Educational Resources Center", "Lavery", "William E. Lavery Animal Health Research Center", "Beamer-Lawson", "Indoor Practice Facility", "Burruss", "Lane", "G. Burke Johnston Student Center", "Johnston", "Femoyer", "Virginia-Maryland Regional College of Veterinary Medicine", "vet med", "veterinary medicine", "College of Liberal Arts and Human Sciences Building", "Sandy", "Robeson", "Owens", "Monteith", "Life Sciences I Facility", "Dairy Science", "Kentland Farm", "Kelly", "Ambler Johnston", "Architecture", "Annex", "Holden", "Derring", "Hahn South", "Eggleston", "Art and Design Learning Center", "Armory", "Shanks", "Slusher", "Norris", "Institute for Critical Technology and Applied Science (ICTAS II)", "Old Growth", "Classroom Building", "NCB", "Steger", "Pearson West", "Whitehurst", "Hoge", "CID", "Creativity and Innovation District Residence Hall", "Data and Decision Sciences"]
#
# buildings += ["Life Science One", "Mccomas", "Schiffert", "Bollos", "Puzzlr", "Milk Parlor", "Blacksburg Books", "Idego", "Bishop Favrao", "Blacksburg Library", "Newman", "Library", "Cowgill", "Massey", "Herbarium", "Derring", "Frith", "Goodwin", "Holden", "Inn", "Holtzman", "Center", "ICTAS II", "ICTAS TWO", "Hancock", "Kelly", "Major Williams", "Moss Arts", "Owens", "Pamplin", "Price", "Robeson", "Skelton", "Torgersen", "Torg Bridge"]
# buildings = ['Fun N Games', 'Board Game Store', 'Mathematics Emporium', 'Board game shop', 'board games shop', 'board games store', 'hobby shoppe', 'ucb fun hobby shop']

# buildings = [i[::-1] for i in buildings]
# print(buildings)
buildings = ["ava", 'avery', 'bobby', 'chuma', 'coco', 'david', 'ellie', 'flynn',
             'fred', 'giovanni', 'grant', 'heath', 'imani', 'jared', 'opal', 'otto',
             'richard', 'scarlett', 'timothy', 'ulysses']

for each in buildings:
    chemed = chemify_words(each)
    if chemed is not None:
        print(f'{each[::-1]} = {each} = {chemed}')


