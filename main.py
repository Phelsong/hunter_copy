""" TrueFit batch reprocessing script"""
import os
import sys
import shutil
import re
import csv


def batch(in_csv, search_dir, out_dir, verbose=False):
    """Copies files based on a (single column csv) list of search elements"""
    work_dir = os.listdir(search_dir)
    case_exists = False
    # ----------------------------
    with open(in_csv, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for i in reader:
            for item in work_dir:
                # search thru items in dir for string (id) in CSV
                match = re.search(f"{i[0]}", work_dir[u])
                if match is not None:
                    case_exists = True
                    shutil.copy(
                        f"{search_dir}\\{work_dir[u]}", f"{out_dir}\\{work_dir[u]}"
                    )
                    if verbose is True:
                        print(
                            "Copied: "
                            + f"{search_dir}\\{work_dir[u]}"
                            + " to: "
                            + f"{out_dir}\\{work_dir[u]}"
                        )
            # write not copied
            if case_exists is False:
                print(f"{i[0]},", file=open(".\\not_found.csv", "a"))
            else:
                case_exists = False


# ------------------------------------------------------------------------------


# if __name__ == "__main__":
#     search_dir = "C:\\Users\\joshs\\myscripts\\PYTHON\\batch_searcher\\test_dir"
#     out_dir = "C:\\Users\\joshs\\myscripts\\PYTHON\\batch_searcher"
#     in_csv = "C:\\Users\\joshs\\myscripts\\PYTHON\\batch_searcher\\SpeedFlex Tru -.csv"
#     batch(in_csv, search_dir, out_dir)

# -----------------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        in_csv = sys.argv[1]
        search_dir = sys.argv[2]
        out_dir = sys.argv[3]
        verbose = True if sys.argv[4] == "--verbose" else False
        batch(in_csv, search_dir, out_dir, verbose)
    except IndexError:
        print(
            f"Usage: batch.exe <in_csv> <search_dir> <out_dir> < --verbose(optional)>"
        )
        print(f"Example: batch.exe .\\csv .\\source_dir_path .\\out_dir_path --verbose")
