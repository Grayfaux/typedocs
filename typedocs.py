import os
import time as t


def write_doc(file_to_read, root_path, doc_file_name, doc_name, code_version, doc_author, dl_link, short_description):

    header = f"{doc_name}\n" \
             f"Ver: {code_version}\n" \
             f"Author: {doc_author}\n" \
             f"{dl_link}\n" \
             f"Documentation Updated:{t.strftime('%m/%d/%Y, %H:%M:%S')}\n" \
             f"Description:\n{short_description}\n" \


    doc_root = root_path
    if not os.path.exists(doc_root):
        os.mkdir(doc_root)
        with open(f"{doc_root}/{doc_file_name}", "w") as w_data:
            w_data.write(f"{header}\n\n")
    else:
        with open(f"{doc_root}/{doc_file_name}", "w") as w_data:
            w_data.write(f"{header}\n\n")

    with open(file_to_read, "r") as code:
        read_code = code.readlines()

    td_tag = ["# ht>", "# hc>", "# >", "# t>", "# rt>", "# rt/t", "# ol>", "# ole>", "# end>", "# c>", "# dc>", "# mln>", "# mln/t", "# n>"]
    spacing = "    "
    entries = 1

    doc_entry_format = ""
    end = False
    while not end:
        for i, line in enumerate(read_code):
            if td_tag[8] in line:
                end = True

            # if td_tag[11] in line:
            #     end = True

            if td_tag[6] in line:
                ol_split = line.split("# ol>")
                ol_format = f"{ol_split[1]}{spacing}{ol_split[0]}\n\n"
                read_code = read_code[i + 1:]

                with open(f"{doc_root}/{doc_file_name}", "a") as w_data:
                    w_data.write(f"{spacing}{ol_format}\n")
                break

            if td_tag[7] in line:
                ole_split = line.split("# ole>")
                ole_format = f"{entries}: {ole_split[1]}\n{spacing}{ole_split[0]}\n\n"
                read_code = read_code[i + 1:]
                entries += 1

                with open(f"{doc_root}/{doc_file_name}", "a") as w_data:
                    w_data.write(f"{ole_format}\n")
                doc_entry_format = ""
                break

            if td_tag[0] in line:
                format_header_title = line
                format_header_title = format_header_title.split(td_tag[0])
                doc_entry_format = f"{entries}: {format_header_title[1]}"

                read_code = read_code[i + 1:]
                with open(f"{doc_root}/{doc_file_name}", "a") as w_data:
                    w_data.write(f"{doc_entry_format}\n")
                doc_entry_format = ""
                break

            if td_tag[1] in line:
                format_header = line
                format_header = format_header.split(td_tag[1])
                doc_entry_format = f"{doc_entry_format}{spacing}{format_header[0][:-2]}\n"

                read_code = read_code[i + 1:]
                with open(f"{doc_root}/{doc_file_name}", "a") as w_data:
                    w_data.write(f"{doc_entry_format}\n")
                doc_entry_format = ""
                break

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

                doc_entry_format = f"{doc_entry_format}{spacing}-{arrow_split[1]}{spacing}{spacing}{arrow_split[0]}\n"
                read_code = read_code[i + 1:]
                with open(f"{doc_root}/{doc_file_name}", "a") as w_data:
                    w_data.write(f"{doc_entry_format}\n")
                doc_entry_format = ""
                break


            if td_tag[3] in line:
                read_code = read_code[i+1:]
                entries += 1

                with open(f"{doc_root}/{doc_file_name}", "a") as w_data:
                    w_data.write(f"{doc_entry_format}\n")
                doc_entry_format = ""
                break


            if td_tag[4] in line:
                format_rt_line = line
                split_rt_line = format_rt_line.split(td_tag[4])
                doc_entry_format = f"{doc_entry_format}\n{spacing}-{split_rt_line[1]}{spacing}{spacing}{split_rt_line[0]}\n"
                read_code = read_code[i+1:]

                with open(f"{doc_root}/{doc_file_name}", "a") as w_data:
                    w_data.write(f"{doc_entry_format}\n")
                for r, r_line in enumerate(read_code):
                    if td_tag[5] not in r_line:
                        with open(f"{doc_root}/{doc_file_name}", "a") as w_data:
                            w_data.write(f"{spacing}{spacing}{r_line}")
                    if td_tag[5] in r_line:
                        read_code = read_code[i + 1:]
                        # entries += 1
                        doc_entry_format = ""
                        with open(f"{doc_root}/{doc_file_name}", "a") as w_data:
                            w_data.write("\n\n")
                        break
                break

            if td_tag[11] in line:
                format_nt_line = line
                split_nt_line = format_nt_line.split(td_tag[11])
                doc_entry_format = f"{doc_entry_format}{split_nt_line[1]}"
                read_code = read_code[i+1:]

                with open(f"{doc_root}/{doc_file_name}", "a") as w_data:
                    w_data.write(f"{doc_entry_format}")
                for n, n_line in enumerate(read_code):
                    if td_tag[12] not in n_line:
                        with open(f"{doc_root}/{doc_file_name}", "a") as w_data:
                            w_data.write(f"{n_line[2:]}")
                    if td_tag[12] in n_line:
                        read_code = read_code[i + 1:]
                        # entries += 1
                        doc_entry_format = ""
                        with open(f"{doc_root}/{doc_file_name}", "a") as w_data:
                            w_data.write("\n")
                        break
                break

            if td_tag[13] in line:
                format_n_line = line
                split_n_line = format_n_line.split(td_tag[13])
                doc_entry_format = f"{doc_entry_format}{split_n_line[1]}"
                read_code = read_code[i + 1:]

                with open(f"{doc_root}/{doc_file_name}", "a") as w_data:
                    w_data.write(f"{doc_entry_format}")
                doc_entry_format = ""
                break


def code_stats(file_to_read, root_path, doc_file_name):

    with open(file_to_read, "r") as code:
        read_code = code.readlines()

    blanks = 0
    for i in read_code:
        if i == "\n":
            blanks += 1
    line_data = f"Lines:{len(read_code)}\nBlank Lines:{blanks}"

    imports = 0
    imports_body = ""
    for i in read_code:
        if "import" in i and "#" not in i:
            imports_body = f"{f'{imports_body}{read_code.index(i)}: {i}'}"
            imports += 1
    imports_data = f"Imports:{imports}\n{imports_body}"

    loops = 0
    loops_body = ""
    for i in read_code:
        if "#" not in i:
            if " for " in i or " while " in i:
                loops_body = f'{loops_body}{f"{read_code.index(i)}:{i}"}'
                loops += 1
    loops_data = f"Loops:{loops}\n{loops_body}"

    functions = 0
    func_body = ""
    for i in read_code:
        if "def" in i and "#" not in i and "self" not in i:
            func_body = f"{func_body}{f'{read_code.index(i)}: {i}'}"
            functions += 1
    function_data = f"functions:{functions}\n{func_body}"

    classes = 0
    class_body = ""
    for i in read_code:
        if "class" in i and "#" not in i:
            class_body = f"{class_body}{f'{read_code.index(i)}: {i}'}"
            classes += 1
    class_data = f"classes:{classes}\n{class_body}"

    methods = 0
    method_body = ""
    for i in read_code:
        if "def" in i and "#" not in i and "self" in i:
            method_body = f"{method_body}{f'{read_code.index(i)}: {i}'}"
            methods += 1
    method_data = f"methods:{methods}\n{method_body}"

    returns = 0
    returns_body = ""
    for i in read_code:
        if " return " in i and "#" not in i:
            returns_body = f"{returns_body}{f'{read_code.index(i)}: {i}'}"
            returns += 1
    returns_data = f"returns:{returns}\n{returns_body}"

    prints = 0
    prints_body = ""
    for i in read_code:
        if "print" in i and "#" not in i:
            prints_body =  f"{prints_body}{f'{read_code.index(i)}: {i}'}"
            prints += 1
    prints_data = f"prints:{prints}\n{prints_body}"

    appends = 0
    appends_body = ""
    for i in read_code:
        if "append" in i and "#" not in i:
            appends_body = f"{appends_body}{f'{read_code.index(i)}: {i}'}"
            appends += 1
    appends_data = f"appends:{appends}\n{appends_body}"

    variables = 0
    variables_body = ""
    for i in read_code:
        if "=" in i and "#" not in i and "==" not in i:
            variables_body = f"{variables_body}{f'{read_code.index(i)}: {i}'}"
            variables += 1
    variables_data = f"variables/assignments:{variables}\n{variables_body}"

    opens = 0
    opens_body = ""
    for i in read_code:
        if "open" in i and "#" not in i:
            opens_body = f"{opens_body}{f'{read_code.index(i)}: {i}'}"
            opens += 1
    opens_data = f"read/writes:{opens}\n{opens_body}"

    comments = 0
    comments_body = ""
    for i in read_code:
        if "# c>" in i:
            comments_slice = i.replace("# c>", "")
            comments_body = f"{comments_body}{f'{read_code.index(i)}: {comments_slice}'}"
            comments += 1
    comments_data = f"comments:{comments}\n{comments_body}"

    dev_comments = 0

    for i in read_code:
        if "# dc>" in i:
            dev_comments += 1
    dev_comments_data = f"dev comments:{dev_comments}"

    return_format = f"\nDocument Stats:\n\nLines: {line_data}\nCode Lines: {len(read_code)-blanks}\n" \
                    f"Imports: {imports}\nLoops: {loops}\nFunctions: {functions}\nReturns: {returns}\n" \
                    f"Prints: {prints}\nAppends: {appends}\nVariables/Assignments: {variables}\nClasses: {classes}\n" \
                    f"Methods: {methods}\nRead/Writes: {opens}\nComments: {comments}\nDev_comments: {dev_comments}\n" \
                    f"\n\n" \
                    f"Document Index:\n\n" \
                    f"{imports_data}\n\n" \
                    f"{loops_data}\n\n" \
                    f"{function_data}\n\n" \
                    f"{class_data}\n\n" \
                    f"{method_data}\n\n" \
                    f"{returns_data}\n\n" \
                    f"{prints_data}\n\n" \
                    f"{appends_data}\n\n" \
                    f"{variables_data}\n\n" \
                    f"{opens_data}\n\n" \
                    f"{comments_data}\n\n" \
                    f"{dev_comments_data}\n\n" \
                    f"\n" \

    doc_root = root_path
    if not os.path.exists(doc_root):
        os.mkdir(doc_root)
        with open(f"{doc_root}/{doc_file_name}", "w") as w_data:
            w_data.write(f"{return_format}\n\nDocument generated by TypeDocs @:{t.strftime('%m/%d/%Y, %H:%M:%S')}\n")
    else:
        with open(f"{doc_root}/{doc_file_name}", "a") as w_data:
            w_data.write(f"{return_format}\n\nDocument generated by TypeDocs @:{t.strftime('%m/%d/%Y, %H:%M:%S')}\n")

