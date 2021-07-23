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
    # Define lists of variables for storeage
    CounterQuestion = 0
    Questions = []
    QuestionNumbers = []
    AnswerNumbers = []
    Answers = []
    # Temp lists
    AnswerNumTemp = []
    AnswerTemp = []

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
                AnswerNumbers.append(element[0])
                Answers.append(element[1].strip())
        elif len(element) == 0:
            # If a ' \n' is shown, it means the end of question
            EndOfQuestion = True


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
    export_tuples("input.txt")
    # Questions, QuestionNumbers, Answers, AnswerNumbers = export_variables("input.txt")
    # print(Questions)
    # print(QuestionNumbers)
    # print(Answers)
    # print(AnswerNumbers)

        
