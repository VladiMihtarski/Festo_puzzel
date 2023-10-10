# Условията
conditions = {
    1: "A -> BC",
    2: "A -> CB",
    3: "B -> DD",
    4: "B -> BD",
    5: "C -> CD",
    6: "C -> FE",
    7: "D -> AF",
    8: "D -> FA"
}

def is_valid_recipe(recipe):
    current_transformation = "A"
    steps = recipe.strip().split(' - ')

    for step in steps:
        parts = step.strip('()').split(', ')
        if len(parts) != 2:
            return False

        try:
            hammer, position = int(parts[0]), int(parts[1])
        except ValueError:
            return False

        if hammer not in conditions:
            return False

        original_segment = conditions[hammer].split(" -> ")[0]
        if position > len(current_transformation) or current_transformation[position - 1] != original_segment:
            return False

        transformed_segment = conditions[hammer].split(" -> ")[1]
        current_transformation = current_transformation[:position - 1] + transformed_segment + current_transformation[position:]

    return True

# Четене на рецептите от файла
recipe_file = r'C:\Users\user\Desktop\My proget\New folder\Festo\11_keymaker_recipe.txt'
with open(recipe_file, 'r') as file:
    recipes = file.readlines()

# Търсене на правилната рецепта
valid_recipe = None
for recipe in recipes:
    if is_valid_recipe(recipe):
        valid_recipe = recipe
        break

if valid_recipe:
    print(f"Правилната рецепта е: {valid_recipe}")
    # Тук може да изведете крайния символ, ако е необходимо
else:
    print("Няма намерена правилна рецепта.")
# AFDFCDAFFE
