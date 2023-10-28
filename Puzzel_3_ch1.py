import math

class InputValidator:
    def __init__(self, inputdate):
        self.inputdate = inputdate
        self.parts = inputdate.split(":")

    def is_valid(self):
        if len(self.parts) > 1:
            left_part = self.parts[1].split("-")[0]
            right_part = self.parts[1].split("-")[1]

            left_list = list(map(int, left_part.split()))
            right_list = list(map(int, right_part.split()))

            if not (self._has_common_values(left_list, right_list) or self._has_duplicates(left_list) or self._has_duplicates(right_list)):
                if len(left_list) == len(right_list):
                    return True
            return False
        return False

    def _has_common_values(self, left_list, right_list):
        common_values = set(left_list) & set(right_list)
        return bool(common_values)

    def _has_duplicates(self, values):
        return len(values) != len(set(values))

    def calculate_and_print_result(self):
        if self.is_valid():
            left_part, right_part = self.parts[1].split("-")
            left_list = list(map(int, left_part.split()))
            right_list = list(map(int, right_part.split()))

            # Намиране на общия знаменател
            common_denominator = self.find_common_denominator(left_list + right_list)

            # Изчисление на дробите
            left_fraction = [common_denominator // x for x in left_list]
            right_fraction = [common_denominator // x for x in right_list]

            # Проверка за равенство
            if sum(left_fraction) == sum(right_fraction):
                return left_list, right_list

        return None, None

    def find_common_denominator(self, values):
        # Намира НОК на всички стойности в списъка values
        common_denominator = values[0]
        for value in values[1:]:
            common_denominator = (common_denominator * value) // math.gcd(common_denominator, value)
        return common_denominator

def calculate_id_sum(inputdates):
    id_sum = 0
    for inputdate in inputdates:
        left_list, right_list = InputValidator(inputdate).calculate_and_print_result()
        if left_list and right_list:
            id_sum += int(inputdate.split(":")[0])
    return id_sum

# Четене на входни данни от текстов файл
inputdates = []
with open(r"C:\Users\user\Desktop\My proget\New folder\Festo\13_trap_balance.txt", "r") as file:
    for line in file:
        inputdates.append(line.strip())

valid_id_sum = calculate_id_sum(inputdates)
print(f"Сума на id номерата при верните уравнения: {valid_id_sum}")
