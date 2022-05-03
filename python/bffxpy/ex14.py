from sys import argv

script, user_name = argv
promote = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few question.")
print(f"DO you like me {user_name}?")
likes = input(promote)

print(f"Where do you live {user_name}")
lives = input(promote)

print("What kind of computer do you have?")
computer = input(promote)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
