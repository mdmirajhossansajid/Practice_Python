Question::::::
Create a text file named emails.txt containing multiple email addresses, some in uppercase and some repeated.
Write a Python program to clean the data by converting all emails to lowercase, removing duplicates, sorting them alphabetically, and saving the cleaned list to a new file named unique_emails.txt.




with open("sample_data/emails.txt","r") as file:
  emails=file.readlines()
  uniques_email=set()
  for email in emails:
    email=email.strip().lower()
    uniques_email.add(email)
  uniques_email=sorted(uniques_email)
with open("unique_emails.txt","w") as file:
  for email in uniques_email:
    file.write(email+"\n")
print(*uniques_email, sep="\n")
