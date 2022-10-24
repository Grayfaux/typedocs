import os


def write_doc(file_to_read, doc_path):

    with open(file_to_read, "r") as code:
        read_code = code.readlines()

    td_tag = ["# ht>", "# h>", "# >", "# t>", "# rt>", "# rt/t", "# ol>", "# end>"]
    spacing = "    "
    entries = 1

    doc_entry_format = ""
    end = False
    while not end:
        for i, line in enumerate(read_code):
            if td_tag[7] in line:
                end = True

            if td_tag[0] in line:
                format_header_title = line
                format_header_title = format_header_title.split(td_tag[0])
                doc_entry_format = f"{entries}: {format_header_title[1]}"

            if td_tag[1] in line:
                format_header = line
                format_header = format_header.split(td_tag[1])
                doc_entry_format = f"{doc_entry_format}{spacing}{format_header[0][:-2]}\n\n"

            if td_tag[2] in line:
                format_content = line
                content_arrow_split = format_content.split("#")
                content_arrow_split = content_arrow_split[1][1:]
                arrows = 0
                arrow_char = ""
                for o in content_arrow_split:
                    if o == ">":
                        arrows += 1
                        arrow_char = f"{arrow_char}>"
                    else:
                        pass
                content_arrow = f"# {arrow_char}"
                arrow_split = line.split(content_arrow)

                doc_entry_format = f"{doc_entry_format}{spacing}-{arrow_split[1]}{spacing}{spacing}{arrow_split[0]}\n\n"

            if td_tag[3] in line:

                read_code = read_code[i+1:]
                entries += 1

                if not os.path.exists(doc_path):
                    with open(doc_path, "w") as w_data:
                        w_data.write(f"{doc_entry_format}\n")
                else:
                    with open(doc_path, "a") as w_data:
                        w_data.write(f"{doc_entry_format}\n")
                doc_entry_format = ""
                break

            if td_tag[4] in line:
                format_rt_line = line
                split_rt_line = format_rt_line.split(td_tag[4])
                doc_entry_format = f"{doc_entry_format}\n{spacing}-{split_rt_line[1]}{spacing}{spacing}{split_rt_line[0]}\n"
                read_code = read_code[i+1:]

                if not os.path.exists(doc_path):
                    with open(doc_path, "w") as w_data:
                        w_data.write(f"{doc_entry_format}\n")
                else:
                    with open(doc_path, "a") as w_data:
                        w_data.write(f"{doc_entry_format}\n")
                for r, r_line in enumerate(read_code):
                    if td_tag[5] not in r_line:
                        with open(doc_path, "a") as w_data:
                            w_data.write(f"{spacing}{spacing}{r_line}")
                    if td_tag[5] in r_line:
                        read_code = read_code[i + 1:]
                        entries += 1
                        doc_entry_format = ""
                        with open(doc_path, "a") as w_data:
                            w_data.write("\n\n")
                        break
                break


write_doc("functions.py", "typedoc.tdc")



# for i in read_code:
#     if "import" in i and read_code.index(i) < 10:
#         print(f'{read_code.index(i)}: {i}')
#
# functions = 0
# for i in read_code:
#     if "def" in i:
#         print(f'{read_code.index(i)}: {i.replace("def", "")}')
#         functions += 1
# print(f"functions: {functions}")
#
#
# returns = 0
# for i in read_code:
#     if "return" in i and "#" not in i:
#         print(f'{read_code.index(i)}: {i}')
#         returns += 1
# print(f"returns: {returns}")
