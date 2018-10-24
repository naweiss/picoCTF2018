cipher = "4-'3evh?'c)7%t#e-r,g6u#.9uv#%tg2v#7g'w6gA"

# As a first step we assumed the alphabet is a-z which is clearly not true
# But we noticed that evh can got to CTF, interesting
# Then we assumed that the flag is in the flag format: picoCTF{}

# So "4-'3evh?A" goes to "picoCTF{}"
# We can use that to find the alphabet.

# Apparently, it's rot over all the pritable characters (space to tilde)
# with subtraction of 34

ans = ""
for i in range(len(cipher)):
	tmp = (ord(cipher[i]) - 34)
	if tmp < ord(' '):
		tmp +=  ord('~') - ord(' ')
	ans += chr(tmp)

print(ans)