# coding: utf8

from utils import get_file_contents, string_to_lines, csv_separate


def part_1():
  puzzle_input = csv_separate(get_file_contents('2s.txt'))

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

  invalids = []

  for input_range in puzzle_input:
    start, end = input_range.split('-')
    inputs = map(str, range(int(start), int(end)+1))
    for i in inputs:
      if len(i) == 1:
        pass
      elif len(set(i)) == 1:
        invalids.append(i)
      elif i[0:int(len(i)/2)] == i[int(len(i)/2):]:
        invalids.append(i)
      else:
          for x in range(2, int(len(i) / 2) + 1):
            for m in range(2, int(len(i) / 2) + 1):
              if (i[0:x] * m)[:len(i)+1] == i:
                if not i in invalids:
                  invalids.append(i)

  print(sum(map(int, invalids)))


def _chunk_range(min_, max_):
    ranges = []
    current = min_

  while current <= max_:
        digits = len(str(current))
        max_in_range = int('9' * digits)
        end = min(max_in_range, max_)
        ranges.append((current, end))
        current = end + 1

    return ranges


def part_2_smart():
  # instead let's generate the invalid ids

  puzzle_input = csv_separate(get_file_contents('2.txt'))

  invalids = []
  new_ranges = []

  # parse input and turn into chunked ranges
  for input_range in puzzle_input:
    start, end = input_range.split('-')
    start = int(start)
    end = int(end)
    for _r in _chunk_range(start, end):
      new_ranges.append(_r)
  
  # work on each chunked range from the original ranges
  for chunk in new_ranges:
    start, end = chunk

    s_start = str(start)
    s_end = str(end)

    len_start = len(s_start)
    len_end = len(s_end)
  
    factors = []

    for f in range(1, len(s_end)):
      if len(s_end) % f == 0:
        factors.append(f)
    
    # now we have factors for this range
    for factor in factors:
      # generate range at factor
      check_range = range(
        int(s_start[0:factor]),
        int(s_end[0:factor]) + 1
      )

      for r in check_range:
        # generate pattern and clamp (lazy)
        target = int((str(r) * len_start)[:len_start])
        if target >= start and target <= end:
          if not target in invalids:
            invalids.append(target)

  print(invalids)
  print(sum(map(int, invalids)))


if __name__ == '__main__':
  part_1()
  part_2()
  part_2_smart()
