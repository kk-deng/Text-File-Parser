def export_variables(filepath):

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
                    # Question line
                    QuestionNumbers.append(line.split("\t")[0].split(".")[0])
                    Questions.append(line.split("\t")[1].strip())

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
                    AnswerNumTemp.append(line.split("\t")[0].split(".")[0])
                    AnswerTemp.append(line.split("\t")[1].strip())
                    AnswerNumbers.append(list(AnswerNumTemp))
                    Answers.append(list(AnswerTemp))
                
                try:
                    # Append the answers for each question
                    AnswerNumTemp.append(line.split("\t")[0].split(".")[0])
                    AnswerTemp.append(line.split("\t")[1].strip())
                except:
                    pass
            
            # Counter for each question
            CounterQuestion += 1
            
        # Return all variables        
        return Questions, QuestionNumbers, Answers, AnswerNumbers

                
if __name__ == "__main__":
    Questions, QuestionNumbers, Answers, AnswerNumbers = export_variables("input.txt")
    print(Questions)
    print(QuestionNumbers)
    print(Answers)
    print(AnswerNumbers)

        