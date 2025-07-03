gunzip -c dictionary.gz | grep -E ".{4,}" | grep -v "[^zircona]" | grep -c "r"    

# output: 50
