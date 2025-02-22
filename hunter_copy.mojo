from sys import argv, exit
import os
from pathlib import Path
from testing import assert_true, assert_raises
from mojo_csv import CsvReader
from find_substring.find_substring import find_substring


# ------------------------------------------------------------------------------
fn hunter_copy(owned in_csv: Path, owned search_dir: Path, owned out_dir: Path,
    owned verbose: Bool = False):
    try:
        var no_match_csv = open("./not_found.csv", "w")
        var work_dir: List[String] = os.listdir(search_dir)
        var case_exists: Bool = False
        # ----------------------------
        with open(in_csv, "r") as csvfile:
            var reader = CsvReader(csvfile.read(), delimiter=",", quotation_mark="|")
            for i in range(len(reader.elements)):
                # print(reader.elements[i])
                for k in range(len(work_dir)):
                    if find_substring(work_dir[k], reader.elements[i]):
                        case_exists=True
                        var matchee = search_dir.joinpath(work_dir[k])
                        var out = out_dir.joinpath(work_dir[k])
                        with open(matchee, "r") as match_file:
                            with open(out_dir, "w") as out_file:
                                out_file.write(match_file.read())
                        if verbose:
                            print(
                                String("Copied: {} to: {}").format(matchee, out)
                            )
                        break
                if case_exists == False and len(reader.elements[i])>0:
                    print(reader.elements[i], end=",\n", file=no_match_csv)
                else:
                    case_exists = False
        no_match_csv.close()
    except Exception:
        if verbose:
            print("unknown error")
        pass

# -----------------------------------------------------------------------------------

fn main():
    try:
        var in_args: Int8 =(len(argv()))
        assert_true(in_args >= 3)
        var in_csv = Path(argv()[1])
        var search_dir = Path(argv()[2])
        var out_dir = Path(argv()[3])
        if argv()[4] == "--verbose" or argv()[4] == "-v":
            hunter_copy(
                in_csv=in_csv,
                out_dir=out_dir,
                search_dir=search_dir,
                verbose=True
            )
        else:
            hunter_copy(
                in_csv=in_csv,
                out_dir=out_dir,
                search_dir=search_dir,
            )
    except AssertionError:
        print("Usage: hc(.exe) <in_csv> <search_dir> <out_dir> < --verbose(optional)>")
        print("Example: hc(.exe) ./csv.csv ./search_dir_path ./out_dir_path --verbose")
        exit()
