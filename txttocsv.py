import csv

FILENAME = './data/mit-movie/10-shot-train'
label_list = set()

with open(FILENAME+'.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Source sentence","Answer sentence"])

	with open(FILENAME+'.txt', 'r', encoding="utf-8") as f:
		words = []
		labels = []
		for line in f:
			if line.startswith("-DOCSTART-") or line == "" or line == "\n":
				if words:
					sentence = " ".join(words)
					rows = []
					phrase = []
					for i in range(len(words)):
						if labels[i] == "O":
							if phrase:
								rows.append([sentence, f'{" ".join(phrase)} is a {labels[i-1][2:]} entity .'])
								phrase = []
							rows.append([sentence, f"{words[i]} is not a named entity ."])
						else:
							if phrase and labels[i][0] == "B":
								rows.append([sentence, f'{" ".join(phrase)} is a {labels[i-1][2:]} entity .'])
								phrase = []
							phrase.append(words[i])

					if phrase:
						rows.append([sentence, f'{" ".join(phrase)} is a {labels[-1][2:]} entity .'])
						phrase = []

					writer.writerows(rows)
					words = []
					labels = []
			else:
				splits = line.split(" ")
				words.append(splits[0])
				if len(splits) > 1:
					label = splits[-1].replace("\n", "")
					labels.append(label)
					label_list.add(label[2:])
				else:
					# Examples could have no label for mode = "test"
					labels.append("O")
					label_list.add("O")

label_list = list(label_list)
template_list = []

print("{",end="")
for i in range(len(label_list)):
	template_list.append(f'\" is a {label_list[i]} entity .\"')
	print(f'{i}: \"{label_list[i]}\",',end="")
print("}")
print("[",end="")
for template in template_list:
	print(template,end=",")
print("]")