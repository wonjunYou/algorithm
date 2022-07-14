import sys

input = sys.stdin.readline

# recursive
def solve(times):
	if times == flag:
		print(rep_str * times + '"재귀함수가 뭔가요?"')
		print(rep_str * times + '"재귀함수는 자기 자신을 호출하는 함수라네"')
		print(rep_str * times + '라고 답변하였지.')
		return

	print(rep_str * times + '"재귀함수가 뭔가요?"')
	print(rep_str * times + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
	print(rep_str * times + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
	print(rep_str * times + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
	solve(times + 1)
	print(rep_str * times + '라고 답변하였지.')
  

flag = int(input().rstrip('\n'))
rep_str = "____" #기본 string

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

solve(0) # function call