import os


def write_doc(file_to_read, doc_path):

    with open(file_to_read, "r") as code:
        read_code = code.readlines()

    typedoc_comment_tags = ["# h>", "# ht>", "# >", "# t>"]
    spacing = "    "
    entries = 1

    doc_entry_format = ""
    for i, line in enumerate(read_code):

        if typedoc_comment_tags[1] in line:
            format_header_title = line
            format_header_title = format_header_title.split("# ht>")
            doc_entry_format = f"{entries}: {format_header_title[1]}"

        if typedoc_comment_tags[0] in line:
            format_header = line
            format_header = format_header.split("# h>")
            doc_entry_format = f"{doc_entry_format}{spacing}{format_header[0][:-2]}\n\n"

        if typedoc_comment_tags[2] in line:
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

        if typedoc_comment_tags[3] in line:
            print("end", )
            read_code = read_code[i+1:]
            entries += 1

            if not os.path.exists(doc_path):
                with open(doc_path, "w") as w_data:
                    w_data.write(f"{doc_entry_format}\n")
            else:
                with open(doc_path, "a") as w_data:
                    w_data.write(f"{doc_entry_format}")


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
