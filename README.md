# hc

Originally a python utility from mass copying files for workflow automation. Now updated to Mojo at 10x+ the speed, which is compiled to a single binary.
(The original version still works for regex, as mojo doesn't yet have libraries for it)

Just drop it in any user $Path location.

## Usage: hunter_copy <in_csv> <search_dir> <out_dir> --verbose(optional)
Example: 

```sh
hunter_copy test/query.csv test/search test/found
```

For regular usage I recommend adding the follow to your bashrc

```
alias hc=hunter_copy
```