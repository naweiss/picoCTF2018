# unshadow is part of the tool John the Ripper
# Generate some sort of hash
unshadow ../passwd ../shadow > pwdump
# Crack it
john pwdump
# Show it
john --show pwdump
# Use the user-name: root
# and password: password1