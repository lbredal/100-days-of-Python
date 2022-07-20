# functions with outputs

def my_function(f_name,l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

f_name = "lars"
l_name = "bredal"

name = my_function(f_name, l_name)

print(name)