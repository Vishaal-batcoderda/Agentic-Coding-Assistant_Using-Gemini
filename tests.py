# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.get_directory_tree import get_directory_tree

def main():
    working_dir = "calculator"
    # print(get_file_content(working_dir,"main.py"))
    # print(get_file_content(working_dir,"pkg/calculator.py"))
    # print(get_file_content(working_dir,"/bin/cat"))
    #print(write_file(working_dir,"lorem.txt","bruham"))
    #print(write_file(working_dir,"pkg/morelorem.txt","bruham bah"))
    # print(write_file(working_dir,"tmp/bruh.txt","bruham temp"))
    # print(run_python_file(working_dir,"main.py",["3 + 5"]))
    # print(run_python_file(working_dir,"tests.py"))
    # print(run_python_file(working_dir,"../main.py"))
    # print(run_python_file(working_dir,"nonexistent.py"))
    # print(get_directory_tree(working_dir))
    # print(get_directory_tree("calculator", "pkg"))

main()