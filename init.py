import os
import mimetypes


def construct_query(file_path):
    # 获取文件名和编程语言
    file_name = os.path.basename(file_path)
    language, _ = mimetypes.guess_type(file_path)
    if not language:
        raise ValueError("Unknown programming language.")

    # 构造查询字符串
    query = "q="
    keywords = ["filename:" + file_name, "language:" + language]
    query += "+".join(keywords)

    # 添加文件大小范围限制
    file_size = os.path.getsize(file_path)
    min_size = int(file_size * 0.7)
    max_size = int(file_size * 1.3)
    size_range = f"size:{min_size}..{max_size}"
    query += f"+{size_range}"

    # 过滤特殊字符
    special_chars = ['.', ',', ':', ';', 'l', '\\l', '~', "'", '"', '=', '*', '!', '\'', '?', '#', '$', '&', '+', '^',
                     'I', '<', '>', '(', ')', '{', '}', '[', ']']
    file_contents = open(file_path, 'r').read()
    for char in special_chars:
        file_contents = file_contents.replace(char, '')

    # 添加代码语句
    code_snippet = " ".join(file_contents.split()[-10:])
    query += f"+{code_snippet}"

    return query
