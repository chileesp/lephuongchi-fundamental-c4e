namsinh = input("ban sinh nam bao nhieu?")
tuoi =  2018 - int(namsinh)
print ("tuoi", tuoi)
if (tuoi < 10):
    print ("tre em")
elif (tuoi < 18):
    print ("thieu nien")
else:
    print ("nguoi lon")
