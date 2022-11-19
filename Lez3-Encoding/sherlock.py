with open('C:/Users/miche/Desktop/CyberSecurity/CyberSecurity/Challenges/2_sherlock/challenge.txt', 'r') as file:
    data = file.read().replace('\n', '')

capitalMessage = ""
for letter in data:
    if 65 <= ord(letter) <= 90:
        capitalMessage += letter

binaryMessage = capitalMessage.replace('ZERO', '0').replace('ONE', '1')

result=''.join(chr(int(binaryMessage[i*8:i*8+8],2)) for i in range(len(binaryMessage)//8))
print(result)     