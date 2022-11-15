# CSV Combiner

A command line program that takes several CSV files as arguments. Each CSV
file (found in the `fixtures` directory of this repo) will have the same
columns. The script outputs a new CSV file to `stdout` that contains the
rows from each of the inputs along with an additional column that has the
filename from which the row came (only the file's basename, not the entire path).
Use `filename` as the header for the additional column.

## How to use

Example:
Given two input files named `clothing.csv` and `accessories.csv`.

Command to run the script
```
$ python csv_combiner.py fixtures/accessories.csv fixtures/clothing.csv fixtures/household_cleaners.csv > merge.csv
```


|email_hash|category|
|----------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|

|email_hash|category|
|----------|--------|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|

Output:

|email_hash|category|filename|
|----------|--------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|clothing.csv|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|clothing.csv|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|clothing.csv|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|accessories.csv|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|accessories.csv|


Command to do unittest
```
$ python -m unittest  test_csv_combiner.py
```

##  Considerations 
* Using coding best practices and the program is re-usable and extensible.
My program uses function "merge_csv_files" to merge csv files, which is reusable in other projects.
The parameter received by merge_csv_files is a list of files, so any number of csv files can be processed.
The program is generalized for taking csv files that contain different number of columns and rows

* Testable by a CI/CD process. 
The input of my program is a file, the error information is printed through stderr,
and the merged data is printed through stdout. At the same time,
it returns 0 when the program executes successfully, and returns 1 when it fails.
CI/CD can determine execution status by the information through stderr or the return value of the program exit.

* Unit tests should is included.
My program has a file list as a parameter, and the number of inputs is not limited.
If the input csv has different columns, the program will extract all the columns,
and the output result contains all the columns, set an empty value when a column is missing in the result
Each file is processed line by line, so no matter how large the file is, it does not take up too much memory.


