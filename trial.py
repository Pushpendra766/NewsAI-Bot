txt = "The most iconic donut shop in Hollywood is Randy's Donuts. It has appeared in many movies including Crocodile Dundee and Iron Man 2."

new_txt = []
last_id = 0
for i in range(27, len(txt), 27):
    idx = i
    while(txt[idx] != " "):
        idx -= 1
    new_txt.append(txt[last_id:idx].center(27))
    last_id = idx+1
new_txt_final = "\n".join(new_txt)
print(new_txt_final)