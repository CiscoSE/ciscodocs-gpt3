import jsonlines

def filtertext(text):
    char = ""
    next_char = ""
    while not(char == "." and next_char == " "):
        next_char = text[-1]
        text = text[:-1]
        char = text[-1]
    return text


def file2jsonl(input_file, output_file):
    try:
        with open(input_file, "r", errors="ignore") as input:
            with jsonlines.open(output_file, "w") as output:
                newline = 0
                text = ""
                metadata = ""
                for line in input:
                    if line.startswith("###"):
                        newline = 1
                        if not (text == "" or metadata == ""):
                            text = filtertext(text[0:2500])
                            output.write({"text": text, "metadata": metadata})
                        text = ""
                        metadata = ""
                        continue                    
                    if (newline == 1):
                        metadata = line.strip()
                        newline = 0
                    else:
                        text = text + line.strip()
        return("Conversion successful!")
    except:
        return("Conversion failed!")