import json
with open("recipes.json","r",encoding="utf-8") as f:
    recipes=json.load(f)


ingredients_list=[];
while 1:
    question2=input("Write ingredients that you got. When you're done, type \"Q\" to exit:\n").strip();
    if question2.lower()=="q":
        print("\n")
        break
    ingredients_list.append(question2.lower())


found=False;
for recipe in recipes:
    if any(ingredient["item"].lower() in ingredients_list for ingredient in recipe["mainIngredients"]):
        found=True;
        print(recipe["name"]+"\n\n")
        print("Ingredients:\n")
        for ingredient in recipe["mainIngredients"]:
            print(ingredient["item"]+"-->"+ingredient["amount"])
        for ingredient in recipe["sideIngredients"]:
            print(ingredient["item"]+"-->"+ingredient["amount"])
        print("\n"+"Mandatory steps"+"\n")    
        steps=recipe["steps"];
        for i in range(1,len(steps)):
            print(f"Step {i}\n\n"+ steps[i-1]+"\n")
        print("\nNutrition details per 100g: \n")
        for key,value in recipe["nutrition"].items():
            print(key+": "+value)
if not found:
    print("There is either no recipe with the ingredients you typed or there are some diferences between your typing and the code.")
    print("The main ingredients available are:")
    allIngredients=[];
    for recipe in recipes:
        for ingredient in recipe["mainIngredients"]:
            allIngredients.append(ingredient["item"])
print(allIngredients)              
