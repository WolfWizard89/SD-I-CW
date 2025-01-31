# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W2052039
# Date: 10/12/2023

from graphics import * # import the graphics.py module


def table():
    # OPEN THE WINDOW
    win = GraphWin("Histogram", 1000, 750)
    win.setBackground(color_rgb(196, 196, 194))
    # Drawing lines
    aline_horizontal = Line(Point(70, 600), Point(930, 600))
    aline_horizontal.setArrow("last")
    aline_horizontal.draw(win)
    aline_vertical = Line(Point(70, 600), Point(70, 60))
    aline_vertical.setArrow("last")
    aline_vertical.draw(win)
    # Drawing bars for Progress, Progress (module trailer), Do not Progress-module retriever and Exclude. Colour codes are also added
    progress_rectangle = Rectangle(Point(100, graphic_progress), Point(200, 598))
    progress_rectangle.setFill(color_rgb(154, 212, 123))
    progress_rectangle.draw(win)
    progressMT_rectangle = Rectangle(Point(300, graphic_progress_mt), Point(400, 598))
    progressMT_rectangle.setFill(color_rgb(200, 212, 123))
    progressMT_rectangle.draw(win)
    module_retriever_rectangle = Rectangle(Point(500, graphics_module_retriver), Point(600, 598))
    module_retriever_rectangle.setFill(color_rgb(201, 195, 4))
    module_retriever_rectangle.draw(win)
    exclude_rectangle = Rectangle(Point(700, graphics_exclude), Point(800, 598))
    exclude_rectangle.setFill(color_rgb(242, 109, 127))
    exclude_rectangle.draw(win)
    # Printing Progress, Progress (module trailer), Do not Progress-module retriever and Exclude text depicted under the bars
    progress_text = Text(Point(150, 620), "Progress")
    progress_text.setFill("black")
    progress_text.draw(win)
    progrssMT_text1 = Text(Point(350, 620), "Progress")
    progrssMT_text1.setFill("black")
    progrssMT_text1.draw(win)
    progrssMT_text2 = Text(Point(350, 650), "(module trailer)")
    progrssMT_text2.setFill("black")
    progrssMT_text2.draw(win)
    module_retriever_text1 = Text(Point(550, 620), "Do not Progress")
    module_retriever_text1.setFill("black")
    module_retriever_text1.draw(win)
    module_retriever_text2 = Text(Point(550, 650), "module retriever")
    module_retriever_text2.setFill("black")
    module_retriever_text2.draw(win)
    exclude_text = Text(Point(750, 620), "Exclude")
    exclude_text.setFill("black")
    exclude_text.draw(win)
    # Printing Progress, Progress (module trailer), Do not Progress-module retriever and Exclude amounts are stated above the bars
    progress_amount_number = Text(Point(150,progress_amount),progress)
    progress_amount_number.setFill("black")
    progress_amount_number.draw(win)
    progressmt_amount_number = Text(Point(350,progress_mt_amount),progress_mt)
    progressmt_amount_number.setFill("black")
    progressmt_amount_number.draw(win)
    module_retriever_number = Text(Point(550,module_retriever_amount),module_retriever)
    module_retriever_number.setFill("black")
    module_retriever_number.draw(win)
    exclude_number = Text(Point(750,exclude_amount),exclude)
    exclude_number.setFill("black")
    exclude_number.draw(win)
    # Printing total outcomes
    total_outcomes_text1 = Text(Point(398,700),total_outcomes)
    total_outcomes_text1.setSize(18)
    total_outcomes_text1.setFill("black")
    total_outcomes_text1.draw(win)
    total_outcomes_text2 = Text(Point(515,700),": outcomes in total")
    total_outcomes_text2.setSize(18)
    total_outcomes_text2.setFill(color_rgb(13, 13, 12))
    total_outcomes_text2.draw(win)
    histogram_text = Text(Point(500,20),"Histogram Results")
    histogram_text.setFill("black")
    histogram_text.setSize(20)
    histogram_text.draw(win)
    # Mouse click for exit
    win.getMouse()
    win.close()
# If conditions are in a user define for outputs
# I used this user define in line number 150 and 151

def calculate_progress_outcome(pass_credits, defer_credit, fail_credit):
    if (pass_credits == 120) and (defer_credit == 0) and (fail_credit == 0):
        return "Progress"
    if pass_credits == 100 and (defer_credit == 0 or defer_credit == 20) and (
            fail_credit == 0 or fail_credit == 20) and (defer_credit != fail_credit):
        return "Progress (module trailer)"
    if (0 <= pass_credits <= 40) and (0 <= defer_credit <= 120) and (80 <= fail_credit <= 120):
        return "Exclude"
    if (0 <= pass_credits <= 80) and (0 <= defer_credit <= 120) and (0 <= fail_credit <= 80):
        return "Do not Progress-module retriever"
# these variables used for graph
progress = 0         #progress
progress_mt = 0      #Progress (module trailer)
module_retriever = 0 #Do not Progress-module retriever
exclude = 0          #Exclude
# these lists used for part 2
progress_list = []          # input values list for Progress
module_mt_list = []         # input values list for Progress (module trailer)
module_retriever_list = []  # input values for Do not Progress-module retriever
exclude_list = []           # input values for Exclude
# After this comment, user identification option stage commence
print("User identification options\n","1. Enter 1, if you are a member of staff.\n","2. Enter 2, if you are a student.")
option_valid_values=[1,2] # If user input except 1 or 2, program will loop until user gives a valid input
while True:
    option_check=int(input("enter your option number: "))
    if option_check not  in option_valid_values:
        print("invalid option")
    else:
        break
while True:
    try:
        # Inputs ( every input in the while loop because if user a input  wrong value or string, program will loop until user enters a valid value. )
        while True:
            valid_values =[0,20,40,60,80,100,120]
            while True:
                try:
                    pass_credit = int(input("Please enter your pass credits: "))
                    if (pass_credit not in valid_values):
                        print("Out of range")
                    else:
                        break
                except ValueError:
                    print("Integer required")
            while True:
                try:
                    defer_credit = int(input("Please enter your defer credits: "))
                    if (defer_credit not in valid_values):
                        print("Out of range")
                    else:
                        break
                except ValueError:
                    print("Integer required")
            while True:
                try:
                    fail_credit = int(input("Please enter your fail credits: "))
                    if (fail_credit not in valid_values):
                        print("Out of range")
                    else:
                        break
                except ValueError:
                    print("Integer required")
            # If total of 3 inputs are not equal to 120, program will print "Total incorrect".
            total = (pass_credit + defer_credit + fail_credit)
            if total != 120:
                print("Total incorrect")
                continue
            # Using the user define function which is created for calculation
            else:
                progression_outcome = calculate_progress_outcome(pass_credit, defer_credit, fail_credit)
                print(progression_outcome)
            if option_check == 2: # If user a student program will end here
                print("Thank You!")
                break
            # Increments for graph and collecting(append) input values for part 2. ( I used string format for enhance outputs of part 2 & part 3)
            if progression_outcome == "Progress":
                progress += 1
                progress_list.append("{} Pass, {} Defer, {} Fail".format(pass_credit, defer_credit, fail_credit))
            if progression_outcome == "Progress (module trailer)":
                progress_mt += 1
                module_mt_list.append("{} Pass, {} Defer, {} Fail".format(pass_credit, defer_credit, fail_credit))
            if progression_outcome == "Do not Progress-module retriever":
                module_retriever += 1
                module_retriever_list.append("{} Pass, {} Defer, {} Fail".format(pass_credit, defer_credit, fail_credit))
            if progression_outcome == "Exclude":
                exclude += 1
                exclude_list.append("{} Pass, {} Defer, {} Fail".format(pass_credit, defer_credit, fail_credit))
            total_outcomes= progress + progress_mt + module_retriever + exclude
            graphic_progress= -(progress*12)+600
            graphic_progress_mt= -(progress_mt*12)+600
            graphics_module_retriver= -(module_retriever*12)+600
            graphics_exclude= -(exclude*12)+600
            progress_amount= graphic_progress-10
            progress_mt_amount= graphic_progress_mt-10
            module_retriever_amount=graphics_module_retriver-10
            exclude_amount=graphics_exclude-10
            print("Would you like to enter another set of data?")
            while True:
                restart=str(input("Enter 'y' to yes or 'q' to quit and view results: "))
                restart=restart.lower()
                valid_restart_inputs={"y","q"}
                if restart not in valid_restart_inputs:
                    print("wrong letter")
                else:
                    break
            if restart ==("q"):
                try:
                    table()  # Call the table user define function to display the histogram
                except GraphicsError:
                    print("")
                    # part 2 & part 3 commence after this comment( In the end of the every line I have mentioned what part that line used for)
                print("")
                
                 print("Part 2:")
                with open("W2052039_Part3_TextFile.txt", 'w') as file:  # open the file in writing mode (part3)
                    file.write("Part 3:\n")
                    print(" Progress:")                                 # printing Progress as title for input list (part 2)
                    file.write(" progress:\n")                          # writeing progress in text file as a title (part3)
                    for elements1 in progress_list:                     # using this loop for print every element line by line (part 2)
                        print(" ",elements1)                            # printing input list as an output (part2)
                        file.write(f"  {elements1}\n")                  # printing progress input list in text file  (part3)
                    print(" Progress (module trailer):")                # printing Progress (module trailer) as title for input list (part2)
                    file.write(" Progress (module trailer):\n")         # writeing Progress (module trailer) in text file as a title (part3)
                    for elements2 in module_mt_list:                    # (part 2)
                        print(" ",elements2)                            # printing input list as an output (part2)
                        file.write(f"  {elements2}\n")                  # printing progress (module trailer) input list in text file  (part3)
                    print(" Do not Progress-module retriever:")         # printing Do not Progress-module retriever: as title for input list (part2)
                    file.write(" Do not Progress-module retriever:\n")  # writeing Do not Progress-module retriever in text file as a title (part3)
                    for elements3 in module_retriever_list:             # (part 2)
                        print(" ",elements3)                            # printing input list as an output (part2)
                        file.write(f"  {elements3}\n")                  # printing Do not Progress-module retriever input list in text file  (part3)
                    print(" Exclude:")                                  # printing Exclude as the title for a input list (part2)
                    file.write(" Exclude:\n")                           # printing Exclude as the title in text file as a title (part3)
                    for elements4 in exclude_list:                      # (part2)
                        print(" ",elements4)                            # printing input list as an output (part2)
                        file.write(f"  {elements4}\n")                  # print Exclude input list in text file  (part3)
                    print("Thank you!")
                    break
            if restart == ("y"):
                print("Program is restarting")
    except RuntimeError:
        print("An unexpected runtime issue occurred. Try again")
        continue
    except SyntaxError:
        print("There is something wrong with the program. :)")
        break
    else:
        break