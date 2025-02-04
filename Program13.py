words = ["zero","one","two","three","four","five",'six', "seven","eight", "nine", "ten", "eleven","twelve", "thirteen"]
for i in range(0,20):
    if i < 14:
        print(words[i])
    else: 
        print(f"{words[i-10]}teen")
