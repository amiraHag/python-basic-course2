# ---------------------------
# -- Practical Slice Email --
# ---------------------------

myName = input('What\'s Your Name ?').strip().capitalize()
myEmail = input('What\'s Your Email ?').strip()

myUsername = myEmail[:myEmail.index("@")]
myWebsite= myEmail[myEmail.index("@")+1:]

print(f"Hello {myName} Your Email Is {myEmail}")
print(f"Your Username Is {myUsername} \nYour Website Is {myWebsite}")
