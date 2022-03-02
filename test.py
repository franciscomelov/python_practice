from ctypes import LittleEndianStructure


s = "abb" # 2
s = "pwwkew" # 3
s = "sdfvvvfsvdsvscsfvvsdcgbvlk,fnhdlccnhhklvgflbmccos" # 12 , iter:49
#s = "sdfvvvfsvdsvscsfvvsdcgbvlk,afnhdlccnhhklvgflbmccosñdsjdkdnsyuwpkendyapdmabsdxytavdakendpskfbfyavadexrwzxtcuvbbnni" # 13 , iter:49
counter = 0


sub =""
biggest = 0
size = len(s)

for start in range(size):
    print("_____", biggest, len(s[start:]))
    if biggest >= len(s[start:]):
        print("############")
        break
    end = biggest + start + 1
    while end <= size+1:
        print("Biggest:", biggest, "Start:", start, "end", end)
        counter += 1
        sub = s[start:end]
        print(sub)

        if len(set(sub)) < len(sub):
            break

        if len(sub) > biggest:
            biggest = len(sub)
        end +=1

print(counter, "-")
print(biggest)


set_s = set("sdfvvvfsvdsvscsfvvsdcgbvlk,fnhdlccnhhklvgflbmccos")
print(set_s)