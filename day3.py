from utils import get_file_contents, string_to_lines, csv_separate, ignore_comments


def part_1() -> None:
    puzzle_input = ignore_comments(string_to_lines(get_file_contents('3.txt')))

    joltages = []

    for bank in puzzle_input:
        
        highest = max(int(batt) for batt in bank)
        highest_ix = bank.index(str(highest))
        
        # print(f'{bank}, max={highest}, ix={highest_ix}, len={len(bank)}')

        if highest_ix == 0:
            joltages.append(int(str(highest) + str(max(int(batt) for batt in bank[1:]))))
        elif highest_ix == len(bank) - 1:
            print('highest=end')
            joltages.append(int(str(max(int(batt) for batt in bank[:highest_ix])) + str(highest)))
        else:
            joltages.append(int(str(highest) + str(max(int(batt) for batt in bank[highest_ix+1:]))))
        
        print('')
    
    print(sum(joltages))


def part_2() -> None:
    puzzle_input = ignore_comments(string_to_lines(get_file_contents('3.txt')))

    joltages = []

    for bank in puzzle_input:
        # sanitise, repeats dont matter
        pass
    
    print(sum(joltages))


if __name__ == '__main__':
    part_1()
    part_2()
