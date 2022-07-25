from collections import defaultdict

def solution(tickets):
    answer = []
    path = defaultdict(list)

    for ticket in tickets:
        path[ticket[0]].append(ticket[1])

    for key in path.keys():
        path[key].sort(reverse=True)

    stack = ['ICN']
    while stack:
        tmp = stack[-1]

        if not path[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(path[tmp].pop())
            
    answer.reverse()

    return answer