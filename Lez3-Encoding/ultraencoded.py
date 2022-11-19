#open the text file
with open('C:/Users/miche/Desktop/CyberSecurity/CyberSecurity/Challenges/3_ultraencoded/zero_one', 'r') as file:
    challenge = file.read()

#replace the zeros and ones in the numerical representation
challenge = challenge.replace('ZERO', '0')
challenge = challenge.replace('ONE', '1')
challenge = challenge.replace(' ', '')

print(challenge)

#since it is a multiple of 8, we can think that this is a series of
#ascii characters
decoded=''.join(chr(int(challenge[i*8:i*8+8],2)) for i in range(len(challenge)//8))
print(decoded)

#convert morse to string
decoded2 = ''.join(morse2alpha.get(i) for i in decoded.split())
print(decoded2)

