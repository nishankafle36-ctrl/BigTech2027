def main():
    # Ask for the meal
    dollars = float(input("How much was the meal? "))
    
    # Ask for the tip percentage
    percent = float(input("What percentage tip would you like to give? "))
    
    # calculate (cost * percent) divided by 100
    tip = (dollars * percent) / 100
    
    # show the result
    print(f"You should leave a tip of ${tip:.2f}")
main()