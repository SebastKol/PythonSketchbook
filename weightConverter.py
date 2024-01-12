earthWeight = int(input("Tell me your weight: "))

def weightConverter(x: int):
    marsMultiplier = 0.378
    convertedWeight = x * marsMultiplier
    return convertedWeight

marsWeight = weightConverter(earthWeight)

print (f"If your earth weight is {earthWeight}, your weight on Mars would be {marsWeight}")