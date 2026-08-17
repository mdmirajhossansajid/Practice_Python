QUESTION:::
--------------------------------------------------------------------------------------------------------------------
Create a text file named names.txt containing a list of names.
Some names may have extra spaces, inconsistent capitalization (like “aLiCe” or “ bob ”), or appear more than once.
Write a Python program to clean the data by:
1.  Removing extra spaces.
2.  Converting all names so that only the first letter is capitalized.
3.  Removing duplicate names. 
4. Sorting the names alphabetically.
Finally, save the cleaned list into a new file named clean_names.txt.
-----------------------------------------------------------------------------------------------------------------------

with open("names.txt","r") as file:
  names=file.readlines()
  clean_names=set()
  for name in names:
    name=name.strip().capitalize()
    clean_names.add(name)
  clean_names=sorted(clean_names)
  with open("clean_names.txt","w") as file:
    for name in clean_names:
      file.write(name+"\n")
    print(*clean_names, sep="\n")
