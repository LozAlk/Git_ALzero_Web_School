# ----------------------------
# -- Practical Slice Email --
# ----------------------------

theName = input('What\'s Your Name ?').strip().capitalize()
theEmail = input ('What\'s Your Email ?').strip()

theUsername = theEmail[theEmail.index("@")]
theWebsite = theEmail[theEmail.index("@")+1:]

print(f"Hello {theName} You Email Is {theEmail}")
print(f"Your Username Is {theUsername}\n Your Website Is {theWebsite}")







email = "Seraj@alkherat.com"
print(email[:email.index("@")])