questions = {
  "How many states does United State has?":"50",
  "How many days are there in a year?": "365",
  #This question is from Anna:
  "How many days are there in December?": "31"

  # ***add more questions here: do it as the one above and use comma to separate two question***
  #**comment your name above the question**

}


#Please, don't change anything below this line

def main():
 
  print("Hello learners!")
  # ans = trivia_fetch(6)
  # print(ans)


  # The first answer for the quiz is 0 in order to proceed 
  def quiz(dic):
    score = 0
    qnumb = 0
    for q, a in questions.items():
        print(q)
        qnumb = qnumb + 1
        ans = input("Enter your answer: ")
        if ans == a:
          print("\n Hurray!! you are right\n")
          score = score + 1
         
        else:
          print("\n You failed it!!! Try again\n")
          break
    print(f"Your Score is {score/qnumb*100}%")

# Here we passed the question to the quiz function
  quiz(questions)
  

if __name__=="__main__":
  main()
