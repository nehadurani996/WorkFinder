import os 
colors = {
    'red' : "\033[91m",
    'green' : "\033[92m",
    'yellow' : "\033[93m",
    'base': "\033[0m"
}
def files_path(extention=".txt"):
    f_path=os.path.join(os.curdir,"Words_Directory")
    f_full_path= [os.path.join(f_path , f) for f in os.listdir(f_path) if f.endswith(extention)] #word dic for faster work
    return f_full_path


def word_finder(str_to_find):
    files= files_path()
    for file in files:
        with open (file, "r") as datafile: #context manager
             lines= datafile.readlines()
             for line in lines:
                if str_to_find in line:
                    pretty_line= line.replace(str_to_find,f"{colors['red']}{str_to_find}{colors['base']}")
                    print(f"{file}:{pretty_line}")
