from main import batch


try:
    in_csv = "test\query.csv"
    search_dir = "test\search"
    out_dir = "test\out"
    verbose = True if sys.argv[4] == "--verbose" else False
    batch(in_csv, search_dir, out_dir, verbose)
except IndexError:
    print(f"Usage: hc.exe <in_csv> <search_dir> <out_dir> <--verbose(optional)>")
    print(f"Example: hc.exe .\\csv .\\source_dir_path .\\out_dir_path --verbose")
