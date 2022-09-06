# HashUtil
HashUtil is a simple Command Line Utility (CLI), for cryptographically hashing text input.


# Downloads 
https://github.com/ellipse12/HashUtil/releases Hash-Large (recommended) is not self-contained so it has a lot of supporting files, it has the fastest runtime because of this. Hash-Small is completely contained in one executable file, but it is also the slowest (not recommended).

You will also want to add the files to your systems Path, how to do so can be found here: https://www.c-sharpcorner.com/article/add-a-directory-to-path-environment-variable-in-windows-10/ and just use the path to either the excutable or where you unzipped the download.

# Usage 
Open the command prompt and either navigate to the download using cd (hash.exe), or if you have already added it to path you can do it anywhere. To use it just type hash + <your input> and it will hash it using the default algorithm of SHA256. Note - just typing in "hash" will return the SHA256 hash of an empty string or "" which should come up with: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 
you can also use Hash --help for a more detailed help menu.
