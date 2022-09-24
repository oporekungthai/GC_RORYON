score1 = int(input("โปรดกรอกคะแนนเก็บ : "))
score2 = int(input("โปรดกรอกคะแนนสอบกลางภาค : "))
score3 = int(input("โปรดกรอกคะแนนสอบปลายภาค : "))
sumscore = score1 + score2 + score3

if sumscore >= 80 :
    print("A");
elif sumscore >= 75 :
    print("B+");
elif sumscore >= 70 :
    print("B");
elif sumscore >= 65 :
    print("C+");
elif sumscore >= 60 :
    print("C");
elif sumscore >= 55 :
    print("D+");
elif sumscore >= 50 :
    print("D");
elif sumscore < 50 :
    print("F");
