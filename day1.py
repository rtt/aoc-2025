# encoding: utf8

from utils import get_file_contents, string_to_lines


def part_1():
  puzzle_input = list(map(
    lambda x: int(x[1:]) if x.startswith('R') else -int(x[1:]),
    string_to_lines(get_file_contents('./1.txt'))
  ))

  dial = list(range(50, 100)) + list(range(0, 50))
  n = len(dial)
  ix = 0
  secret = 0

  print('start: ix -> {}, dial -> {}'.format(ix, dial[ix]))
  print('')

  for instruction in puzzle_input:
    ix += instruction
    if dial[ix % n] == 0:
      secret += 1

  print(secret)


def part_2():
  puzzle_input = list(map(
    lambda x: int(x[1:]) if x.startswith('R') else -int(x[1:]),
    string_to_lines(get_file_contents('./1.txt'))
  ))

  n = 100
  zeroes = 0
  ix = 50
  passes = 0

  for instruction in puzzle_input:
    at_zero = not ix == 0

    ix += instruction

    if ix == 0:
      passes += 1
    elif ix >= n:
      passes += ix // n
    elif ix < 0:
      passes += ix // -n + (1 if at_zero else 0) # could just rely on True to 1 and False to 0 but meh

    ix = ix % n

  print(passes)


if __name__ == '__main__':
  part_1()
  part_2()
