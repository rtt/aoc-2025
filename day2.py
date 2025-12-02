# encoding: utf8
from utils import get_file_contents, string_to_lines, csv_separate


def part_1():
  puzzle_input = csv_separate(get_file_contents('2.txt'))

  invalids = []

  for input_range in puzzle_input:
    start, end = input_range.split('-')
    inputs = map(str, range(int(start), int(end)+1))
    
    for i in inputs:
      # 999 is not a repeating pattern, but 9999 would be
      if i[0:int(len(i)/2)] == i[int(len(i)/2):]:
        invalids.append(i)

  print(sum(map(int, invalids)))


def part_2():
  puzzle_input = csv_separate(get_file_contents('2.txt'))


if __name__ == '__main__':
  part_1()
  part_2()
