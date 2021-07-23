from itertools import groupby

def txt_generator(filepath):
    # A generator to read rows in a text file
    for row in open(filepath):
        yield row

def get_number(line):
    # Get the number before ".\t" for questions and answers
    return line.split("\t")[0].split(".")[0]

def get_words(line):
    # Get the content after ".\t" for questions and answers
    return line.split("\t")[1].strip()

def export_tuples(filepath) -> tuple:
    # Define lists of variables for storage
    Questions, QuestionNumbers, AnswerNumbers, Answers, AnswerNumTemp, AnswerTemp = ([] for i in range(6))

    EndOfQuestion = False
    # Generator to read rows in a text file
    lines = (line for line in open(filepath))
    lists = (l.split(".\t") for l in lines)
    for element in lists:
        if len(element) > 1:
            # Check if it's the question section
            if EndOfQuestion == False:
                # Append the question number to list
                QuestionNumbers.append(element[0])
                Questions.append(element[1].strip())
            else:
                AnswerNumTemp.append(element[0])
                AnswerTemp.append(element[1].strip())
        elif len(element) == 1:
            # If it is the end of one question, append everything
            if EndOfQuestion == True:
                AnswerNumbers.append(AnswerNumTemp)
                Answers.append(AnswerTemp)
                # Reset the lists
                AnswerNumTemp = []
                AnswerTemp = []

            #  If a ' \n' is shown, it means the end of question
            EndOfQuestion = not EndOfQuestion

    # Once the last row reaches, append the last sublists to the lists
    AnswerNumbers.append(AnswerNumTemp)
    Answers.append(AnswerTemp)

    # Return all variables        
    return Questions, QuestionNumbers, Answers, AnswerNumbers

def export_variables(filepath):
    """
    Assumption:

    Here we assume that the file has the first line as the first question, 
    and it ends with a "\n" character. 
    The whole file ends with the last answer not "\n".
    Each question/answer has a "\t" tab character between number and content.
    Questions are not always ending with question mark.
    """
    
    # Define lists of variables for storeage
    CounterQuestion = 0
    Questions = []
    QuestionNumbers = []
    AnswerNumbers = []
    Answers = []
    # Temp lists
    AnswerNumTemp = []
    AnswerTemp = []

    # "input.txt"
    with open(filepath) as f:
        # Read all content into lines, might change to Python generator if a large file is parsed
        lines = f.readlines()
        # Read each line
        for index, line in enumerate(lines):

            if CounterQuestion == 0:
                try: 
                    # Question line, remove unnecessary characters at the front and the end
                    QuestionNumbers.append(get_number(line))
                    Questions.append(get_words(line))

                except:
                    pass

            elif CounterQuestion > 1:
                
                if line == " \n":
                    # If reach the end of each question, reset the counter and append lists
                    CounterQuestion = 0
                    AnswerNumbers.append(list(AnswerNumTemp))
                    Answers.append(list(AnswerTemp))

                    # Reset List and skip this loop
                    AnswerNumTemp = []
                    AnswerTemp = []
                    continue

                elif index == (len(lines)-1):
                    # When reaching the end of the file, append the last element
                    AnswerNumTemp.append(get_number(line))
                    AnswerTemp.append(get_words(line))
                    AnswerNumbers.append(list(AnswerNumTemp))
                    Answers.append(list(AnswerTemp))
                
                try:
                    # Append the answers for each question
                    AnswerNumTemp.append(get_number(line))
                    AnswerTemp.append(get_words(line))
                except:
                    pass
            
            # Counter for each question
            CounterQuestion += 1
            
        # Return all variables        
        return Questions, QuestionNumbers, Answers, AnswerNumbers

                
if __name__ == "__main__":
    Questions, QuestionNumbers, Answers, AnswerNumbers = export_tuples("input.txt")
    # Questions, QuestionNumbers, Answers, AnswerNumbers = export_variables("input.txt")
    print(Questions)
    print(QuestionNumbers)
    print(Answers)
    print(AnswerNumbers)

        
