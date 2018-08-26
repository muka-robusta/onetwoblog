h_Illia = {"name":"Illia","sname":"Savenko","age":"18"}
h_Vanya = {"name":"Vanya","sname":"Lutsenko","age":"18"}
if h_Illia["name"] == "Illia" and h_Vanya["name"] == "Vanya":
	print("The data is correct")
elif h_Illia["name"] == "Vanya":
	print("Vice versa data")
else: print("The data is incorrect")

def say_hello(name):
	print("Hello, " + str(name) + "!")
friends = ["Illia","Vanya","Max","Vlad"]
for name in friends:
	say_hello(name)
for n in range(1,3):
	print(n)