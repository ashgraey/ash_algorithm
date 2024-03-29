# OMR카드 : 클래스 + 메서드
import random


class ScoreMng:
    omr = [1, 4, 3, 2, 2]       # 모범답안
    me = []                     # 학생답안

    cnt = 0                     # 정답 맞춘 개수
    score = 0                   # 성적

    def set_my_answer(self):
        for i in range(5):
            r = random.randint(1, 5)
            self.me.append(r)

    def check_score(self):
        for i in range(5):
            if self.omr[i] == self.me[i]:
                self.cnt += 1
        self.score = self.cnt * 20

    def check_omr(self):
        print("[", end="")
        for i in range(5):
            if self.omr[i] == self.me[i]:
                print("O", end="")
            else:
                print("X", end="")
            if i != 4:
                print(", ", end="")
        print("]")

    def run(self):
        self.set_my_answer()
        self.check_score()

        print(self.omr)
        print(self.me)
        self.check_omr()
        print(self.score)


# ----------------------------------------------------
sm = ScoreMng()
sm.run()

# omr카드 실습


class scoreOmr:
    omr = [1, 4, 3, 2, 2]
    me = []

    cnt = 0
    score = 0

    def setMy(self):

        for _ in range(5):
            self.me.append(random.randint(1, 5))

    def scoreCk(self):
        for i in range(5):
            if self.omr[i] == self.me[i]:
                self.cnt += 1

        self.score = self.cnt * 20

    def omrCk(self):
        print("[", end="")
        for i in range(5):
            if self.omr[i] == self.me[i]:
                print("O", end="")
            elif self.omr[i] != self.me[i]:
                print("X", end="")

            if i != 4:
                print(",", end="")
        print("]")

    def run(self):
        self.setMy()
        self.scoreCk()

        print(self.omr)
        print(self.me)
        self.omrCk()
        print("score : ", self.score)


# 실행
result = scoreOmr()
result.run()
