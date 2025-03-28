# Shaxmat taxtasida harakatlanayotgan ot ning yurish yo‘lini topadigan dastur yozing. Dastur:
# ✅ 8x8 taxta yaratishi kerak.
# ✅ Otni boshlang‘ich nuqtaga qo‘yishi kerak.
# ✅ Barcha yurishlarni topish uchun rekursiv algoritm ishlatishi kerak.
# ✅ While, for va def dan foydalanib, kodni to‘liq bajarishi kerak.


# # Taxta o'lchami
# N = 8

# # Otning yurish yo'nalishlari
# moves = [
#     (2, 1), (1, 2), (-1, 2), (-2, 1),
#     (-2, -1), (-1, -2), (1, -2), (2, -1)
# ]

# # Taxta yaratish
# def create_board():
#     board = []
#     for _ in range(N):
#         row = []
#         for _ in range(N):
#             row.append(-1)
#         board.append(row)
#     return board

# # Taxtani chizish
# def print_board(board):
#     for row in board:
#         line = ""
#         for cell in row:
#             if cell < 10:
#                 line += " " + str(cell) + " "
#             else:
#                 line += str(cell) + " "
#         print(line)
#     print("\n")

# # Ot yurishi mumkin bo'lgan joyni tekshirish
# def is_valid_move(x, y, board):
#     if x >= 0 and x < N and y >= 0 and y < N and board[x][y] == -1:
#         return True
#     return False

# # Ot yurishini rekursiv topadigan funksiya
# def solve_knight_tour(x, y, move_count, board):
#     if move_count == N * N:
#         return True  # Barcha katak bosib o'tildi

#     i = 0
#     while i < len(moves):
#         dx, dy = moves[i]
#         new_x, new_y = x + dx, y + dy
#         if is_valid_move(new_x, new_y, board):
#             board[new_x][new_y] = move_count
#             if solve_knight_tour(new_x, new_y, move_count + 1, board):
#                 return True
#             board[new_x][new_y] = -1  # Backtracking
#         i += 1

#     return False

# # Dastur ishlashi
# def start_knight_tour(start_x=0, start_y=0):
#     board = create_board()
#     board[start_x][start_y] = 0  # Boshlang'ich nuqta

#     if solve_knight_tour(start_x, start_y, 1, board):
#         print("✅ Ot yurish yo'li topildi!")
#         print_board(board)
#     else:
#         print("❌ Yechim topilmadi.")

# # Dastur boshlanishi
# start_knight_tour()


print("\nFoydalanuvchi kiritgan soni 'toq', yoki 'juft' ekanligini aniqlovchi dastur.")
a = int(input(f"Son kiriting:"))

if a % 2 == 0:
    print(f"{a} juft son")
else:
    print(f"{a} toq son")