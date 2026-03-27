from src.bmi_bmr import calculate_bmi, calculate_bmr

def test_bmi():
    bmi, category = calculate_bmi(65, 170)
    print("BMI:", bmi, "Category:", category)

def test_bmr():
    bmr = calculate_bmr(65, 170, 22, "male")
    print("BMR:", bmr)

test_bmi()
test_bmr()
