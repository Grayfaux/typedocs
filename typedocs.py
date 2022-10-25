import os
import time as t


def write_doc(file_to_read, root_path, new_file_name, doc_name, code_version, doc_author, dl_option, short_description):

    if len(short_description) > 106:
        raise Exception("description in the header can not exceed 106 characters")

    header = f"Doc Title: {doc_name}\n" \
             f"Ver: {code_version}\n" \
             f"Author: {doc_author}\n" \
             f"Get: {dl_option}\n" \
             f"Last Updated: {t.strftime('%m/%d/%Y, %H:%M:%S')}\n" \
             f"Description: {short_description}\n" \


    doc_root = root_path
    if not os.path.exists(doc_root):
        os.mkdir(doc_root)
        with open(f"{doc_root}/{new_file_name}", "w") as w_data:
            w_data.write(f"{header}\n\n")
    else:
        with open(f"{doc_root}/{new_file_name}", "w") as w_data:
            w_data.write(f"{header}\n\n")

    with open(file_to_read, "r") as code:
        read_code = code.readlines()

    td_tag = ["# ht>", "# hc>", "# >", "# t>", "# rt>", "# rt/t>", "# ol>", "# ole>", "# end>", "# c>", "# dc>", "# mln>", "# mln/t>", "# n>"]
    spacing = "    "
    entries = 1

    doc_entry_format = ""
    end = False
    while not end:
        for i, line in enumerate(read_code):
            if td_tag[8] in line:
                end = True
                break

            if td_tag[6] in line:
                ol_split = line.split(td_tag[6])
                ol_format = f"{ol_split[1]}{spacing}{spacing}{ol_split[0]}\n\n"
                read_code = read_code[i + 1:]

                with open(f"{doc_root}/{new_file_name}", "a") as w_data:
                    w_data.write(f"{spacing}{ol_format}\n")
                break

            if td_tag[7] in line:
                ole_split = line.split(td_tag[7])
                ole_format = f"{entries}: {ole_split[1]}\n{spacing}{ole_split[0]}\n\n"
                read_code = read_code[i + 1:]
                entries += 1

                with open(f"{doc_root}/{new_file_name}", "a") as w_data:
                    w_data.write(f"{ole_format}\n")
                doc_entry_format = ""
                break

            if td_tag[0] in line:
                format_header_title = line
                format_header_title = format_header_title.split(td_tag[0])
                doc_entry_format = f"{entries}: {format_header_title[1]}"

                read_code = read_code[i + 1:]
                with open(f"{doc_root}/{new_file_name}", "a") as w_data:
                    w_data.write(f"{doc_entry_format}\n")
                doc_entry_format = ""
                break

            if td_tag[1] in line:
                format_header = line
                format_header = format_header.split(td_tag[1])
                doc_entry_format = f"{doc_entry_format}{spacing}{format_header[0][:-2]}\n"

                read_code = read_code[i + 1:]
                with open(f"{doc_root}/{new_file_name}", "a") as w_data:
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
                with open(f"{doc_root}/{new_file_name}", "a") as w_data:
                    w_data.write(f"{doc_entry_format}\n")
                doc_entry_format = ""
                break


            if td_tag[3] in line:
                read_code = read_code[i+1:]
                entries += 1

                with open(f"{doc_root}/{new_file_name}", "a") as w_data:
                    w_data.write(f"{doc_entry_format}\n")
                doc_entry_format = ""
                break


            if td_tag[4] in line:
                format_rt_line = line
                split_rt_line = format_rt_line.split(td_tag[4])
                doc_entry_format = f"{doc_entry_format}\n{spacing}-{split_rt_line[1]}{spacing}{spacing}{split_rt_line[0]}\n"
                read_code = read_code[i+1:]

                with open(f"{doc_root}/{new_file_name}", "a") as w_data:
                    w_data.write(f"{doc_entry_format}\n")
                for r, r_line in enumerate(read_code):
                    if td_tag[5] not in r_line:
                        with open(f"{doc_root}/{new_file_name}", "a") as w_data:
                            w_data.write(f"{spacing}{spacing}{r_line}")
                    if td_tag[5] in r_line:
                        read_code = read_code[i + 1:]
                        # entries += 1
                        doc_entry_format = ""
                        with open(f"{doc_root}/{new_file_name}", "a") as w_data:
                            w_data.write("\n\n")
                        break
                break

            if td_tag[11] in line:
                format_nt_line = line
                split_nt_line = format_nt_line.split(td_tag[11])
                doc_entry_format = f"{doc_entry_format}{split_nt_line[1]}"
                read_code = read_code[i+1:]

                with open(f"{doc_root}/{new_file_name}", "a") as w_data:
                    w_data.write(f"{doc_entry_format}")
                for n, n_line in enumerate(read_code):
                    if td_tag[12] not in n_line:
                        with open(f"{doc_root}/{new_file_name}", "a") as w_data:
                            w_data.write(f"{n_line[2:]}")
                    if td_tag[12] in n_line:
                        read_code = read_code[i + 1:]
                        # entries += 1
                        doc_entry_format = ""
                        with open(f"{doc_root}/{new_file_name}", "a") as w_data:
                            w_data.write("\n")
                        break
                break

            if td_tag[13] in line:
                format_n_line = line
                split_n_line = format_n_line.split(td_tag[13])
                doc_entry_format = f"{doc_entry_format}{split_n_line[1]}"
                read_code = read_code[i + 1:]

                with open(f"{doc_root}/{new_file_name}", "a") as w_data:
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


def about_tag(tag):

    tags = ["# ht>", "# hc>", "# >", "# t>", "# rt>", "# rt/t>", "# ol>", "# ole>", "# end>", "# c>", "# dc>", "# mln>",
            "# mln/t", "# n>"]

    tag_dict = {
        "# ht>": "Header Title: The header title tag is used to label new entries and creates a new index number "
                 "used in conjunction with a tale tag (# t>). This tag only writes what comes after the tag. "
                 "Therefore it is best used above new entry content. Indentation is 0",

        "# hc>": "Header Content: The head content tag is used to return anything to its left as it's content. "
                 "This tag only writes what comes before the tag. Indentation is 4 spaces for point and 8 for content.",

        "# >": "Arrow: The arrow tag is used to break up the body of an entry into points. "
               "This tag writes what is on it's left as it's content, and what is to it's right as its title. "
               "The arrow tag will only is single line only. Therefore they are best suited for "
               "indicating points throughout an entry body "
               "Indentation is 4 spaces for point and 8 for content.",

        "# t>": "Tale: The tale tag indicates the end of an entry. "
                "This ensures that the entry that follows it will be indexed correctly",

        "# rt>": "Run Tag: The run tag used in conjunction with the run tag tale (# rt/t>) writes multi-line block "
                 "of content between # rt> and (# rt/t>). Content on the left of # rt> becomes it's first line of"
                 " content and what is written after the # rt> becomes the point of the tag. "
                 "No other tags can be used inside of a run tag block and comments "
                 "will appear in documentation if they are inside a run tag block."
                 "Indentation is 4 spaces for point and 8 for content.",

        "# rt/t>": "Run Tag Tale: The run tag tale indicates the end of a run tag (# rt>). If the rt/t> is not present"
                   " after (# rt>) in the content block, "
                   "all content that follows the run tag will be written to the document. "
                   "Run tag tale writes nothing so it can be used inline if you wish for that line to be excluded,"
                   "or below the final line you wish to include in the run. "
                   "This tag does not end an entry so a tale tag (# t>) is still required at the end of an entry. "
                   "This is so that multiple run tags can be used per entry.",

        "# ol>": "One Liner: The one line tag can be used inside or outside of an entry and are not indexed. "
                 "Content on the left of # ol> becomes the content of the tag and what is written after the # ol> "
                 "becomes the point of the tag. "
                 "Indentation is 4 spaces for point and 8 for content.",

        "# ole>": "One Liner Entry: The one liner entry works just like the one liner tag (# ol>) with the exception "
                  "that # ole> is indexed and will initiate a new numbered entry. "
                  "Indentation is 4 spaces for point and 8 for content.",

        "# end>": "End Doc: The end doc tag indicates to typedocs that this is the end of the "
                  "file that is being documented. Tags should not be used after this point and "
                  "no content after the # end> will be documented. # end> Must be at the end of the content "
                  "being documented or the algorithm will not function correctly. "
                  "It is good convention to identify where you would like a document to end and place the # end> "
                  "there before begin to document the content. If you are documenting as you go, just place # end>"
                  "at the end of the file and then proceed.",

        "# c>": "Comment Tag: The comment tag marks comments explicitly so they can be assigned a line number "
                "and later be added to the documentation following all entries sorted in the order they occur. "
                "Comments marked by the # c> will not show up in document entries, only in the comments section.",

        "# dc>": "Development Comments: Unlike the comment tag (# c>), development comments will not be included "
                 "in the documentation. These are useful for personal notes that you dont want in your documentation. "
                 "These comments are then saved in the same root directory that you have chosen to send "
                 "your documentation saved in this path format 'doc_root/doc_name_dc'.",

        "# n>": "Note Tag: Similarly to the one liner tag (# ol>) the not tag can be used inside or out of an entry. "
                "The two differences are that note tags have no pre-defined indentation or new lines, "
                "and they only write what appears on the right of the not tag. Note tags are one line only, "
                "for the multi-line version use (# mln>) and  close with (mln/t).",

        "# mln>": "Multi-line Note Tag: The multiline not tag does what the note tag (# n>) "
                  "does but for multiple lines. When using the multi-line tag the # mln> goes above the note block. "
                  "Each line in the block should start with # and a space like this '# text goes here' to appease the "
                  "pep 8 style guide for Python. Both the space and the line will be removed when the document is "
                  "created. If the # and space are not in place what ever two characters that are there will be "
                  "deleted. If the # mln> is not closed with (# mln/t>) the algorithm will continue to read lines "
                  "until the file is fully read ignoring all additional tags, including the end tag (# end>). "
                  "So be sure to properly close the multi-line note tag.",

        "# mln/t": "Multi-line Note Closing Tag: The multi-line note closing tag is used to "
                   "close a multi-line not tag (# mln>). This tag ensures the algorithm knows you finished writing "
                   "note lines. Otherwise the algorithm will continue to read lines until the file is fully read "
                   "ignoring all additional tags."

    }

    if tag.lower() == "all":
        return tag_dict
    elif tag.lower() == "list":
        return tags
    else:
        if tag in tag_dict:
            return f"{tag_dict[tag]}"
        else:
            return None


about_tag("# rt>")
