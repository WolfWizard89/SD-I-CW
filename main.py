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