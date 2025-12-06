# coding: utf8

def get_file_contents(file_path):
  with open(file_path) as f:
    return f.read()


def string_to_lines(s):
  return [x.strip() for x in s.strip().split('\n')]


def csv_separate(s):
  return filter(None, s.split(','))


def ignore_comments(lines):
  return filter(lambda x: not x.startswith('#'), lines)
