from binary_difference.big_files import calculate_difference
from binary_difference.recover import recover


old_file = open('files/file1', 'rb')
new_file = open('files/file2', 'rb')
diff_file = open('files/file1_diff_file2', 'wb')

calculate_difference(old_file, new_file, diff_file)

old_file.close()
new_file.close()
diff_file.close()

old_file = open('files/file1', 'rb')
diff_file = open('files/file1_diff_file2', 'rb')
recovered_file = open('files/recovered_file2', 'wb')

recover(old_file, diff_file, recovered_file)

old_file.close()
diff_file.close()
recovered_file.close()
