
MyGraph = {'A':['B', 'C', 'D'],
           'B':['A', 'E'],
           'C':['A', 'F', 'G'],
           'D':['A', 'H'],
           'E':['B', 'I'],
           'F':['C', 'J'],
           'G':['C'],
           'H':['D'],
           'I':['E'],
           'J':['F']
           }


def my_dfs(graph, start_node):
    stack, visited = list(), list()

    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node not in visited:
            stack.extend(reversed(graph[node]))
            # append VS extend
            # extend 함수 : iterable한 데이터가 그대로 삽입됨.
            # append 함수 :  데이터 자료형 그대로 list 자료형에 삽입
            visited.append(node)

    print('dfs -', visited)
    return visited

my_dfs(MyGraph, 'A')