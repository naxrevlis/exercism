def convert(number: int) -> str:
    result_str = ""
    if number % 3 == 0:
        result_str = "Pling"
    if number % 5== 0:
        result_str += "Plang"
    if number % 7== 0:
        result_str += "Plong"
    if result_str == "":
        return str(number)
    return result_str
