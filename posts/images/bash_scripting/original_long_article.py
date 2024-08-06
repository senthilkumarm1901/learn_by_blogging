#!/usr/bin/env python
# coding: utf-8
---
author: Senthil Kumar
badges: true
branch: master
categories:
- Coding
- Bash Scripting
date: '2022-08-15'
description: A quick guide manual to the world of Bash Scripting
output-file: 2022-08-15-I-Shell-Scripting.html
title: The Practical Guide to Bash Scripting
toc: true
---
# <hr>

# ## Introduction
# 
# Arguably, Shell Scripting is the **often untaught foundation** to the most important skills in software engineering

# You may have seen `Shell Commands` in
# - Git
# - Makefile, VirtualEnv or Any Software Packaging
# - Docker, Kubernetes
# - Server Administration
# - Application Deployment
# - Cloud Computing &
# - many more ...

# This blog is  <br>
# - **NOT** about Linux but about Shell Scripting
# - **NOT** meant to cover esoteric commands

# **Purpose** of this blog is
# - To cover a selected list of useful bash scripting utilities
# - To remove the reluctance in writing/interpreting shell commands
# - To inform where Shell Scripting is useful and where it is not 

# <hr>

# ## I. Theory Fundamentals behind Bash Scripting

# ### **What is a Linux**
# - An open source operating system 
# - Used as both Server OS (web servers, db servers, etc.,) and Desktop OS
# - Linux Operating System is a collection of software build around the `Linux kernel` of the system - `the core of the computer's operating system`; that interacts between hardware and other software

# ### **Which Lang is Linux written with**
# - Most things are written in C 

# ### **Linux** vs **Unix**
# - Unix developed by AT&T Labs. IBM AIX, HP UX are some unix OS
# - Linux is a Unix clone but completely different code
# - Linux is more popular than Unix. Linux has distributions include Redhat, Fedora, etc.,
# - MacOS is officially certified UNIX

# ###  **Linux CLI/Shell Terminal**
# - A non-graphical text-based interface to the Kernel 
# - A program to access the features and functionalities offered by kernel
# - How instructions flow: Hardware <-- Kernel <-- Shell/Terminal <-- Command Libraries and Applications (like mail) <-- User
# 
# 
# ![](https://cdn.mindmajix.com/blog/images/linux-0203-1919.png)
# 

# ### **Different Types of Shell**
# - Bourne Shell developed by Steve Bourne at AT&T Labs (sh)
# - C shell (csh)
# - Korn Shell (ksh) - better version of `sh`
# - Bourne-Again Shell (bash) had features of csh and `ksh`
# - Z Shell (zsh) - A more modern shell !

# ## II. Common Single Line Recipes from Personal Experience

# > There are so many bash commands. Here, I attempt to cover those that I use often. Also, it is no use to learn the bash commands in silos. We often use a combination of them in practical use. 
# 
# > I am taking a simple example of a directory of `text_datasets` to explain the use of several bash commands. 

# ### 1. `tree`
# 
# - **Purpose**: Show the dir and files
# 
# ```bash
# senthilkumar.m@BashScripter ~/datasets % tree 
# .
# └── text_datasets
#     ├── ag_news
#     │   └── ag_news_csv.tar.gz
#     ├── dbpedia
#     │   └── dbpedia_csv.tar.gz
#     └── yelp_reviews
#         └── yelp_review_full_csv.tar.gz
# 
# 4 directories, 3 files
# ```

# ### 2. `find` + `xrgs`
# 
# - **Purpose**: Find the size of the archived files
# 
# 
# ```bash
# senthilkumar.m@BashScripter ~/datasets % find . -name "*.tar*" | xargs du -hs 
# 187M	./text_datasets/yelp_reviews/yelp_review_full_csv.tar.gz
#  12M	./text_datasets/ag_news/ag_news_csv.tar.gz
#  65M	./text_datasets/dbpedia/dbpedia_csv.tar.gz
# ```
# - **Want to know more?**: `man xargs`,  `man du` or `man find`

# ### 3. `tar` + `sed` + `find` with a `for` loop
# 
# - **Purpose**: Unzip files across directories
# 
# 
# ```bash
# senthilkumar.m@BashScripter ~/datasets % for f in $(find . -name "*.tar*" | sed -e 's|/[^/]*$||g' ); do tar -xvf "$f"/*.tar.* -C "$f"; done 
# x yelp_review_full_csv/
# x yelp_review_full_csv/readme.txt
# x yelp_review_full_csv/train.csv
# x yelp_review_full_csv/test.csv
# x ag_news_csv/
# x ag_news_csv/train.csv
# x ag_news_csv/test.csv
# x ag_news_csv/classes.txt
# x ag_news_csv/readme.txt
# x dbpedia_csv/
# x dbpedia_csv/classes.txt
# x dbpedia_csv/test.csv
# x dbpedia_csv/train.csv
# x dbpedia_csv/readme.txt
# ```
# - **Want to know more?**: 
#     - `man tar` and 
#     - search for the individual arguments on what they do using backward slash `/` `/-x | -v | -z | -f`

# ### 4.  `find` + `wc` + `grep`
# 
# - **Purpose**: Find number of rows in each file in each sub directory 
# 
# ```bash
# senthilkumar.m@BashScripter ~/*/text_datasets % for f in $(find . -name "*.csv"); do (echo "Number of rows in $f" &&  wc -l "$f" | grep -o "[0-9]*" && echo); done
# Number of rows in ./yelp_reviews/yelp_review_full_csv/test.csv
# 50000
# 
# Number of rows in ./yelp_reviews/yelp_review_full_csv/train.csv
# 650000
# 
# Number of rows in ./ag_news/ag_news_csv/test.csv
# 7600
# 
# Number of rows in ./ag_news/ag_news_csv/train.csv
# 120000
# 
# Number of rows in ./dbpedia/dbpedia_csv/test.csv
# 70000
# 
# Number of rows in ./dbpedia/dbpedia_csv/train.csv
# 560000
# ```

# ### 5.  `find` + `head` + `sed`
# 
# - **Purpose**: Find number of columns in each file in each sub directory 
# 
# ```
# senthilkumar.m@BashScripter ~/*/text_datasets % for f in $(find . -name "*.csv"); do (echo "*****$f***": &&  echo "Number of Columns:" &&  head -n 1 "$f"| sed 's/","/"\n"/g' |wc -l && echo) ; done
# *****./yelp_reviews/yelp_review_full_csv/test.csv***:
# Number of Columns:
#        2
# 
# *****./yelp_reviews/yelp_review_full_csv/train.csv***:
# Number of Columns:
#        2
# 
# *****./ag_news/ag_news_csv/test.csv***:
# Number of Columns:
#        3
# 
# *****./ag_news/ag_news_csv/train.csv***:
# Number of Columns:
#        3
# 
# *****./dbpedia/dbpedia_csv/test.csv***:
# Number of Columns:
#        2
# 
# *****./dbpedia/dbpedia_csv/train.csv***:
# Number of Columns:
#        2
# ```

# ### 6. `find` + `head`  +  `sed` +  `nl`
# 
# - **Purpose**: Human understandable display of 1 line in each file 
# 
# ```bash
# senthilkumar.m@BashScripter ~/text_datasets % for f in $(find . -name "*train.csv"); do (echo && echo "*********$f*******:" && head -n 1 "$f" | sed 's/,"/\n"/g' | nl); done
# 
# *********./yelp_reviews/yelp_review_full_csv/train.csv*******:
#      1	"5"
#      2	"dr. goldberg offers everything i look for in a general practitioner.  he's nice and easy to talk to without being patronizing; he's always on time in seeing his patients; ..."
# 
# *********./ag_news/ag_news_csv/train.csv*******:
#      1	"3"
#      2	"Wall St. Bears Claw Back Into the Black (Reuters)"
#      3	"Reuters - Short-sellers, Wall Street's dwindling\band of ultra-cynics, are seeing green again."
# 
# *********./dbpedia/dbpedia_csv/train.csv*******:
#      1	1
#      2	"E. D. Abbott Ltd"
#      3	" Abbott of Farnham E D Abbott Limited was a British coachbuilding business based in Farnham Surrey trading under that name from 1929. A major part of their output was under sub-contract to motor vehicle manufacturers. Their business closed in 1972."
# ```
# 
# - **Want to know more?**:
#     - `man nl`

# ### 7. find` +  `cat`  + `nl`
# 
# - **Purpose**: What is the distribution of classes in `ag_news` dataset?

# ### 7. `find` +  `cat`  + `nl`
# 
# - **Purpose**: What do the class numbers represent? 
# - **Utilities**: 
# 
# ```bash
# senthilkumar.m@BashScripter ~/text_datasets % for f in $(find . -name "*classes.txt"); do (echo "*******$f*****"; cat "$f"|nl); done
# *******./ag_news/ag_news_csv/classes.txt*****
#      1	World
#      2	Sports
#      3	Business
#      4	Sci/Tech
# *******./dbpedia/dbpedia_csv/classes.txt*****
#      1	Company
#      2	EducationalInstitution
#      3	Artist
#      4	Athlete
#      5	OfficeHolder
#      6	MeanOfTransportation
#      7	Building
#      8	NaturalPlace
#      9	Village
#     10	Animal
#     11	Plant
#     12	Album
#     13	Film
#     14	WrittenWork
# ```

# ### Text Datasets - Distribution of Classes - Shell Scripting vs Python [5A/6] 
# 
# - **Purpose**: What do the class numbers represent? 
# - **Utilities**: `find`, `for` ,`awk`, `sort`, `uniq`
# - **Time Taken**: `13 seconds`
# 
# ```bash
# senthilkumar.m@BashScripter ~/text_datasets % time (for f in $(find . -name "*train.csv"); do (echo "*******$f*****" &&  awk -F ',' '{print $1}' "$f" | sort | uniq -c ) ; done)
# *******./yelp_reviews/yelp_review_full_csv/train.csv*****
# 130000 "1"
# 130000 "2"
# 130000 "3"
# ...
# ...
# 40000 4
# 40000 5
# 40000 6
# 40000 7
# 40000 8
# 40000 9
# ( for f in $(find . -name "*train.csv"); do; ( echo "*******$f*****" && awk -)  12.80s user 0.23s system 101% cpu 12.813 total
# ```

# ### Text Datasets - Distribution of Classes - Shell Scripting vs Python [5B/6]
# 
# - **Purpose**: What do the class numbers represent? 
# - **Utilities**: `Python`
# - **Time Taken**: `5.7 seconds`
# 
# ```python
# from glob import glob
# import pandas as pd
# 
# file_names_with_path = list(glob("./*/*/*train.csv"))
# for each_file in file_names_with_path:
#     ip = pd.read_csv(each_file, header=None, index_col=None)
#     print(f"********{each_file}*****")
#     print(ip[0].value_counts())
#     
# # python3 test_python_code.py  5.29s user 0.52s system 100% cpu 5.759 total
# ```

# ### Text Datasets - Distribution of Classes [6/6] </h4>
# 
# - **Purpose**: What do the class numbers represent? 
# - **Utilities**: `find`, `for` , `cut`, `sort`, `uniq`
# - **Time Taken**: `4.3 seconds`
# 
# ```bash
# senthilkumar.m@BashScripter ~/text_datasets % time (for f in $(find . -name "*train.csv"); do (echo "*******$f*****" &&  cat "$f" | cut -d',' -f1 | sort | uniq -c ) ; done)
# *******./yelp_reviews/yelp_review_full_csv/train.csv*****
# 130000 "1"
# 130000 "2"
# ...
# ...
# 40000 4
# 40000 5
# 40000 6
# 40000 7
# 40000 8
# 40000 9
# ( for f in $(find . -name "*train.csv"); do; ( echo "*******$f*****" && cat  )  4.49s user 0.22s system 107% cpu 4.373 total
# ```

# > Shell Scripting (4.5 sec) wins over Python (5.7 sec). Okay, let's have a better rematch

# ## III.A. Advancing to Shell Scripting Files

# ### Shell Script with positional arguments
# 
# 
# ```bash
# senthilkumar.m@BashScripter ~/*/text_datasets % cat basic_shell_with_positional_args.sh 
# #!/bin/sh
# echo "This tutorial is not about $1. It is about $2." 
# echo "Did you like it? $3"
# ```
# 
# 
# - Shebang line at 1. `#!/bin/sh` or `#!/bin/bash` or `#!/bin/zsh` 
# - Most terminal (CLI interpreters) take care of it even when not expliticity mentioned by assuming it to be `bash` or `sh`
# 
# <hr>

# 
# 
# ```bash
# sh basic_shell.sh Linux "Shell Scripting" No
# 
# # ./basic_shell.sh
# 
# This tutorial is not about Linux. It is about Shell Scripting.
# Did you like it? No
# ```

# ### Shell Script with one-letter keyword arguments
# 
# 
# - **Utilities**: `getopts`, `grep`, `OPTARG`, `tr`,  `[:upper:]` or `[:lower:]` or `[:space:]` 
# 
# ```bash
# #!/bin/bash
# while getopts ":n:a:l:" opt;
# do 
#     case ${opt} in
#         n) NOT=${OPTARG};;
#             a) ABOUT=${OPTARG} ;;
#         l) LIKE=${OPTARG} ;;
#     esac
# done
# echo "This tutorial is not about $NOT. It is about $ABOUT."
# # if [ $LIKE = "No" ]; then
# if [ $(echo $LIKE | grep -i -o "^N" | tr '[:upper:]' '[:lower:]') = 'n' ]; then
#     echo "Did you like it? $LIKE"
#     echo "What Shell Scripting man !?!"
#     echo "Who uses such 40+ years old lang"
# else
#     echo "Did you like it? $LIKE"
# fi
# ```
# 
# <hr>

# 
# ```bash
# senthilkumar.m@BashScripter ~/text_datasets % sh shell_w_getopts_args.sh \
# -n Linux \
# -a "Shell Scripting" \
# -l No
# 
# This tutorial is not about Linux. It is about Shell Scripting.
# Did you like it? No
# What Shell Scripting man !?!
# Who uses such 40+ years old lang
# ```

# ### Shell Script with word keyword arguments
# 
# 
# - **Utilities**: `{#VAR}`, `grep`, `tr`,  `[:upper:]` or `[:lower:]` or `[:space:]` 
# 
# ```bash
# #!/bin/bash
# for ARGUMENT in "$@"
# do
#     KEY_INITIAL=$(echo $ARGUMENT | cut -f1 -d=)
#     KEY_LENGTH=${#KEY_INITIAL}
#     KEY=${KEY_INITIAL:2}
#     VALUE="${ARGUMENT:$KEY_LENGTH+1}"
#     export "$KEY"="$VALUE"
#     # echo "$KEY=$VALUE"
# done
# 
# echo "This tutorial is not about $NOT. It is about $ABOUT."
# # if [ $LIKE = "No" ]; then
# if [ $(echo $LIKE | grep -i -o "^N" | tr '[:upper:]' '[:lower:]') = 'n' ]; then
#     echo "Did you like it? $LIKE"
#     echo "What Shell Scripting man !?!"
#     echo "Who uses such 40+ years old lang"
# else
#     echo "Did you like it? $LIKE"
# fi
# ```
# 
# <hr>

# 
# ```bash
# senthilkumar.m@BashScripter ~/text_datasets % sh shell_w_full_kw_args.sh \
# --NOT=Linux \
# --ABOUT="Shell Scripting" \
# --LIKE=No
# 
# This tutorial is not about Linux. It is about Shell Scripting.
# Did you like it? No
# What Shell Scripting man !?!
# Who uses such 40+ years old lang
# ```

# ## III.B. Shell Script vs Python
# ###  Shell Script to Replace Text in csv File
# 
# - `vi ag_news_classes.json` 
# 
# ```json
# {
# 	"ag_news": {
# 		"1": "World",
# 		"2": "Sports",
# 		"3": "Business",
# 		"4": "Sci/Tech"
# 	},
# 	"dbpedia": {
# 		"1": "Company",
# 		"2": "EducationalInstitution",
# 		"3": "Artist",
# 		"4": "Athlete",
# 		"5": "OfficeHolder",
# 		"6": "MeanOfTransportation",
# 		"7": "Building",
# 		"8": "NaturalPlace",
# 		"9": "Village",
# 		"10": "Animal",
# 		"11": "Plant",
# 		"12": "Album",
# 		"13": "Film",
# 		"14": "WrittenWork"
# 	}
# }
# ```

# 
# 
# - **Utilities**: `grep`, `find`, `wc`, `sed`, `cut`, `jp`
# 
# - vi `replace_class_num_with_text.sh`
# 
# ```bash
# senthilkumar.m@BashScripter ~/text_datasets % cat replace_class_num_with_text.zsh 
# #!/bin/zsh
# num_of_ag_news_classes=$(jp -f dict_classes.json 'length(ag_news)')
# num_of_dbpedia_classes=$(jp -f dict_classes.json 'length(dbpedia)')
# echo $num_of_ag_news_classes $num_of_dbpedia_classes
# for f in $(find . -name "*.csv")
# do  
#     echo "\n**************************"
#     # length_of_matched_text=$(echo "$f" | grep -e 'ag' -e 'db'| wc -m | sed 's/^ *//g')
#     dataset=$(echo "$f" | cut -d'/' -f2)
#     file=$(echo "$f" | cut -d'/' -f4)
#     # echo "$dataset" 
#     # echo "$file"
#     if [[ $dataset == "ag_news"  ]] ; then
#         echo "*****First IF: Processing dataset $dataset and file $file********"
#         for i in {1..$num_of_ag_news_classes};
#         do
#             class_name=$(jp -f dict_classes.json $dataset.\"$i\" -u |sed -e 's#/##' -e 's/"//g')
#             echo $i $class_name
#             sed -i -e "s/$i/$class_name/" $f
#         done
#     fi
#     if [[ $dataset == "dbpedia"  ]] ; then
#         echo "*****Second IF: Processing dataset $dataset and file $file********"
#         for i in {$num_of_dbpedia_classes..1};
#         do
#             class_name=$(jp -f dict_classes.json $dataset.\"$i\" -u|sed -e 's/"//g')
#             echo $i $class_name
#             sed -i -e "s/$i/\"$class_name\"/" $f
#         done
#     fi
# done
# ```

# 
# - **Time Taken**: `17.7 seconds`
# 
# ```bash
# senthilkumar.m@BashScripter ~/text_datasets % time zsh replace_class_num_with_text.zsh 
# ...
# ...
# zsh replace_class_num_with_text.zsh  12.17s user 4.93s system 96% cpu 17.666 total
# ```

# ```bash
# senthilkumar.m@BashScripter ~/text_datasets % head -n 1 ./dbpedia/dbpedia_csv/test.csv
# "Company","TY KU"," TY KU /taɪkuː/ is an American alcoholic beverage company that specializes in sake and other spirits..."
# 
# senthilkumar.m@BashScripter ~/text_datasets % head -n 1 ./dbpedia/dbpedia_csv/test.csv-e
# 1,"TY KU"," TY KU /taɪkuː/ is an American alcoholic beverage company that specializes in sake and other spirits..."
# ```

# ### Python Script to Replace Text in csv File
# 
# ```python
# import json
# import pandas as pd
# from glob import glob
# import re
# 
# with open('dict_classes.json','r') as f:
#     dict_classes = json.load(f)
# 
# csv_files = list(glob('./*/*/*.csv'))
# 
# for csv_file in csv_files:
#     if not re.search('ag_news|dbpedia',csv_file):
#         continue
#     if re.search('ag_news',csv_file):
#         repl_dict = dict_classes['ag_news']
#     elif re.search('dbpedia', csv_file):
#         repl_dict = dict_classes['dbpedia']
#     else:
#         print(csv_file)
#     print(repl_dict)
#     original_file = re.sub('.csv$','_original.csv',csv_file) 
#     print(f"Saving {original_file}")
#     df = pd.read_csv(csv_file,header=None)
#     df.to_csv(original_file,index=None, header=None)
#     print(f"Processing {csv_file}")
#     df[0] = df[0].astype(str)
#     df[0] = df[0].map(repl_dict)
#     df.to_csv(csv_file, index=None, header=None)
# ```

# - **Time Taken**: `8.3 seconds`
# 
# ```bash
# ...
# ...
# python3 python_replace_script.py  7.56s user 0.61s system 98% cpu 8.324 total
# ```

# ```bash
# senthilkumar.m@BashScripter ~/text_datasets_python % head -n 1 ./dbpedia/dbpedia_csv/train_original.csv 
# 1,E. D. Abbott Ltd, Abbott of Farnham E D Abbott Limited was a British coachbuilding business ...
# senthilkumar.m@BashScripter ~/text_datasets_python % head -n 1 ./dbpedia/dbpedia_csv/train.csv         
# Company,E. D. Abbott Ltd, Abbott of Farnham E D Abbott Limited was a British coachbuilding business ...
# ```

# > Shell Scripting (17.6 sec) miserably loses against Python (8.3 sec)

# ## 4. AWS CLI + BASH Scripring

# ### (1) To upload multiple files to S3
# - Focus: `aws s3 cp` + `find` and `for` loop
# 
# ```
# #!/bin/zsh
# for f in $(find . -name "meta_data_files_*.csv")
# do 
#     aws s3 cp $f s3://s3_bucket_name/upload_csv/
# done 
# ```

# ### (2) Parsing JSON output from AWS CLI (E.g. Case - Extract Periodical Expense Report)
# - Focus: `aws ce get-cost-and-usage` + `JSON Matching Expression Path (JMESPATH)` (`jp`)
# 
# ```
# #!/bin/zsh
# 
# # boiler plate code accepting inputs
# ...
# ...
# 
# 
# aws ce get-cost-and-usage \
# --time-period Start=$start_date,End=$end_date \
# --granularity $type_of_report --metrics "BlendedCost" \
# --group-by Type=DIMENSION,Key=SERVICE \
# --query "ResultsByTime[0].Groups[].Keys" \ # querying a json output
# --output text > aws_services.txt
# 
# aws ce get-cost-and-usage \
# --time-period Start=$start_date,End=$end_date \
# --granularity $type_of_report \
# --metrics "BlendedCost" \
# --group-by Type=DIMENSION,Key=SERVICE \
# --query "ResultsByTime[0].Groups[].Metrics.BlendedCost.Amount" \
# --output text | sed -e 's/\t/\n/g'  > aws_cost.txt
# 
# echo "Service,Cost" > $aws_cost_report_name
# 
# paste -d',' aws_services.txt aws_cost.txt >> $aws_cost_report_name
# 
# # how to run the above shell file
# # zsh create_aws_cost_report.sh --start_date=2022-10-01 --end_date=2022-10-31 --type_of_report=MONTHLY
# ```

# ## 5. Conclusion

# ### **Why is Shell Scripting so hard?**
# - Complexity compounds | Commands like `awk` and `sed` are progamming lang on their own
# - Every quote, space and stringed together commands have meaning
# - Less errors | More unexpected behaviour

# ### **Where is Shell Scripting most useful?**
# - When the commands are only 5-20 lines long
#     - Small repetitive tasks. E.g. For small needs involving AWS, small scripting jobs with `jmespath`
# 
# ```
# for f in *.csv
# do
#      echo $f...
#      some transformation
# done
# ```
# 
# - A pure shell script written 15-20 years ago could still yield the same result today
# - Easier than packaging a Python application | Build process is smaller
# - Shell in combination with other language is more useful
# 

# ### **Where Shell Scripting can be avoided?**
# - Co-development is hard. Interpretability is tough.
# - Errors do not always stop your flow. It will go to the next command
# 

# > Unequivocally, Bash Scripting is definitely a useful skill to know in your toolbox 
