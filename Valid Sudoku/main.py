board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


def check_row():
    for r in range(9):
        s = set()
        for c in range(9):
            item = board[r][c]
            if item in s:
                print(f"Invalid number found at: {r,c}")
                return False
            elif item != ".":
                s.add(item)
    return True

def check_column():
    for r in range(9):
        s = set()
        for c in range(9):
            item = board[c][r]
            if item in s:
                print(f"Invalid number found at: {c,r}")
                return False
            elif item != ".":
                s.add(item)
    return True

def check_box():

    #start of box
    boxes_to_check = [(0,0),(0,3),(0,6),
                      (3,0),(3,3),(3,6),
                      (6,0),(6,3),(6,6)]

    for r,c in boxes_to_check:
        s = set()
        for i in range(r, r+3,1):
            for j in range(c, c+3, 1):
                item = board[i][j]
                if item in s:
                    print(f"Invalid number found at: {i,j} number {board[i][j]}")
                    return False
                elif item != ".":
                    s.add(item)
    return True

def one_pass():
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            item = board[i][j]

            if item == ".":
                continue
            box_index = (i // 3) * 3 + (j // 3)


            if item in rows[i]:
                return False
            if item in columns[j]:
                return False
            if item in boxes[box_index]:
                return False
            rows[i].add(item)
            columns[j].add(item)
            boxes[box_index].add(item)
    return True


def main():
    if check_row() and check_column() and check_box():
        print("Valid")
    if one_pass():
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()