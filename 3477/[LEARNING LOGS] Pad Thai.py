"""[LEARNING LOGS] Pad Thai"""

taste = set()
ing = set()
alling = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip",
    "Shrimp", "Bean Sprouts", "Noodle", "Chives",
    "Lime", "Egg", "Oil", "Peanuts"
}
approve = {"Sweet", "Sour", "Salty"}

while True:
    ingredients = input()
    if ingredients == "Cook":
        break
    ing.add(ingredients)

while True:
    flavor = input()
    if flavor == "End":
        break
    taste.add(flavor)

if not ing.issubset(alling):
    print("This is not Pad Thai!!!")
elif len(ing) != len(alling):
    print("This is bad!")
elif not taste.issubset(approve) or len(taste) != len(approve):
    print("Not Bad...")
else:
    print("Delicious!")
