# The flag is printed via stderr so lats ignore stdout ( 1>/dev/null )
echo "Please may I have the flag?" | ../in-out-error 1>/dev/null

# It seems t work only on the server, locally I get Float point exception