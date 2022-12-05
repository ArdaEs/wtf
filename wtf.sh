prev_command=`fc -l -n -2 | head -n 1`

python 'PATH_FOR_SCRIPT'/main.py $prev_command
