questions = ("apa nama planet terbesar? :",
             "apa nama planet yang dekat dengan matahari? :",
             "apa sebutan hewan yang pemakan daging? :",
             "apa sebutan hewan pemakan tumbuhan? :",
             "berapa hasil dari 2 x 5? :")

options = (("A.Bumi","B.Mars","C.Jupiter","D.Saturnus")
         ,("A.Merkurius","B.Saturnus","C.Jupiter","D.Mars")
         ,("A.Karnivora","B.Hebivora","C.Omnivora","D.Detritivora")
         ,("A.Karnivora","B.Omnivora","C.Herbivora","D.Detritivora")
         ,("A.12","B.10","C.20","D.9"))
         

answer = ("C","A","B","A","B")
guesses = []
score = 0
question_num = 0
for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("masukan (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        score += 1
        print("BENAR!")
    else:
        print("JAWABAN SALAH COBA LAGI!")
        print(f"{answer[question_num]} adalah jawaban yang benar")
    question_num += 1

print("--------------------")
print("       HASIL        ")
print("--------------------")

print("jawaban: ",end="")
for answer in answer:
    print(answer, end=' ')

print("pertanyaan: ",end="")
for guess in guesses:
    print(guess, end=' ')
print()

score = (score / len(question) * 100)
print(f"score mu adalah : {score}%")