
prev_command=`fc -l -n -2 | head -n 1`

python /mnt/e/Project/openai/main.py $prev_command
