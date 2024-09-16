""" batch copier script"""

import os
import sys
import shutil
import re
import csv


# ------------------------------------------------------------------------------
def batch(in_csv, out_dir, search_dir, verbose=True):
    """Copies files based on a (single column csv) list of search elements"""
    work_dir = os.listdir(search_dir)
    case_exists = False
    # ----------------------------
    with open(in_csv, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar="|")

        for query in reader:
            for item in work_dir:
                # search thru items in dir for string (id) in CSV
                match = re.search(f"{query[0]}", item)
                if match is not None:
                    case_exists = True
                    shutil.copy(f"{search_dir}\\{item}", f"{out_dir}\\{item}")
                    if verbose is True:
                        print(
                            "Copied: "
                            + f"{search_dir}\\{item}"
                            + " to: "
                            + f"{out_dir}\\{item}"
                        )

            # write not copied
            if case_exists is False:
                print(f"{query[0]},", file=open(".\\not_found.csv", "a"))
            else:
                case_exists = False


# -----------------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        in_csv = sys.argv[1]
        out_dir = sys.argv[2]
        search_dir = sys.argv[3]
        # verbose = True if sys.argv[4] == "--verbose" else False
        batch(
            in_csv=in_csv,
            out_dir=out_dir,
            search_dir=search_dir,
        )
    except IndexError:
        print(f"Usage: hc.exe <in_csv> <out_dir> <search_dir> < --verbose(optional)>")
        print(f"Example: hc.exe .\\csv .\\out_dir_path .\\search_dir_path --verbose")
