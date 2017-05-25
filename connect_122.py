import sys

def check_row(e_no, line, seq_len):
   line_segment = line[e_no: e_no + seq_len]
   x_count = 0
   if len(line_segment) != seq_len:
      return 0
   for e in line_segment:
      if e != 'x':
         return 0
   return 1

def check_column(e_no, grid, start_line, seq_len):
   grid_segment = grid[start_line: start_line + seq_len]
   if len(grid_segment) < seq_len:
      return 0
   for line in grid_segment:
      if line[e_no] != 'x':
         return 0
   return 1

def check_diagonal(e_no, grid, start_line, seq_len):
   grid_segment = grid[start_line: start_line + seq_len]
   if len(grid_segment) < seq_len:
      return 0
   diag_iter = 0
   for line in grid_segment:
      if line[e_no + diag_iter] != 'x':
         return 0
      diag_iter += 1
   return 1

def check_rdiagonal(e_no, grid, start_line, seq_len):
   grid_segment = grid[start_line: start_line + seq_len]
   if len(grid_segment) < seq_len:
      return 0
   diag_iter = 0
   for line in grid_segment:
      if line[e_no + diag_iter] != 'x':
         return 0
      diag_iter -= 1
   return 1



def main():
   total_rows = 0
   total_columns = 0
   total_diagonals = 0
   total_rdiagonals = 0


   sequence_len = int(sys.argv[1])
   grid = sys.stdin.readlines()
   line_no = 0
   while line_no < len(grid):
      row_in_line = False
      line = grid[line_no]
      i = 0
      while i < len(line):
         if line[i] == 'x':
            if not row_in_line:
               if check_row(i, line, sequence_len):
                  total_rows += 1
                  row_in_line = True
            total_columns += check_column(i, grid, line_no, sequence_len)
            total_diagonals += check_diagonal(i, grid, line_no, sequence_len)
            total_rdiagonals += check_rdiagonal(i, grid, line_no, sequence_len)
         i += 1
      line_no += 1

   print(total_rows + total_columns + total_diagonals + total_rdiagonals)

if __name__ == '__main__':
   main()