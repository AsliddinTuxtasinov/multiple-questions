from savol import Savol
score=0
quizs=[
["Python dasturlash tili asoschisi kim ?\n(a) Guido van Rossum\n(b) Stiv Jobs\n(c) Bil Geyts","a"],
["Qaysi biri to'gri sintaksisga ega ?\na) print('salom dunyo\nb) print(\"salom dunyo\")\nc) print(salom dunyo)","b"],
["dastur natijasini toping?\nprint(2+\"3\")\na) 5\nb) hech narsa chiqmaydi\nc) xatolik haqida xabar","c"]]
for i in quizs:
    quiz=Savol(i[0],i[1])
    print(quiz.question)
    j=input("javobni kiriting >>>\n")
    quiz.natija(j)
    if j == quiz.answer:
        score += 1
print(f"siz jami {len(quizs)} ta savoldan {score} tasiga to'g'ri javob berdingiz")


