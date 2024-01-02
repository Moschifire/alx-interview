#!/usr/bin/python3
'''Module to return the pascal triangle'''


def pascal_triangle(n):
    '''
    Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of lists of integers representing the Pascal’s triangle
    '''
    lists = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(lists[i-1][j-1] + lists[i-1][j])
        row.append(1)
        lists.append(row)
    return lists