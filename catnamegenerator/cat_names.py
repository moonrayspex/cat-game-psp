import random

print("=^._.^= Cat Name Generator =^._.^=")

# x = "Merlin Counting Stars of Thaifong"
# print(x)

cat_names = ["Merlin", "Celeste", "Smiley", "Blue", "Kiki", "Muffincakes", "Dog", "Wombat", "Pyewacket"]
breeder_names = ["Tailgate", "Earl Grey", "Xanadu", "Zazicat", "Tabbypatch"]
award_titles = ["GC", "RW", "CH"]

def select_from_array(array):
  return random.choice(array)
    
for x in range(15):

  title = select_from_array(award_titles)
  # print(title)

  first_breeder_name = select_from_array(breeder_names)
  # print(first_breeder_name)

  cat_casual_name = select_from_array(cat_names)
  # print(cat_casual_name)

  second_breeder_name = select_from_array(breeder_names)
  # print(second_breeder_name)

  if second_breeder_name == first_breeder_name:
    index = breeder_names.index(second_breeder_name)
    second_breeder_name = breeder_names[index - 1]


  print("{}. {} {} {} of {}".format(x, title, first_breeder_name, cat_casual_name, second_breeder_name))