import re

def replace_multiline_strings(lines):
    text = "\n".join(lines)  # 将行列表转换为单个字符串以便处理
    # 使用正则表达式匹配 ''' 或 """ 之间的所有内容，包括多行
    # re.DOTALL 使得 . 匹配包括换行符在内的所有字符
    text = re.sub(r"'''(.*?)'''|\"\"\"(.*?)\"\"\"", '', text, flags=re.DOTALL)
    return text.split('\n\n')  # 将处理后的字符串再次分割为行列表

def parse_python_script(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # 处理多行字符串，去除多行字符串内容
    lines = replace_multiline_strings(lines)
    # 保存每个部分的数据
    sections = []
    current_section = None
    code_block = []
    section_id = 1

    is_in_comment_block = False
    comment_lines = []
    collecting_code = False  # 用于指示是否开始收集代码行

    for line_num, line in enumerate(lines, start=1):
        line_stripped = line.strip().strip('\n')
        if line_stripped.startswith('#'):
            # 检测到注释行，开始或继续注释块
            if current_section and collecting_code:
                # 保存代码块，并重置

                # Remove trailing empty lines from code block
                while code_block and code_block[-1]['content'].strip() == '':
                    code_block.pop()
                current_section['code'] = code_block
                sections.append(current_section)
                section_id += 1
                code_block = []

            # 创建新的 section
            current_section = {'id': f'section-{section_id}', 'title': '', 'description': '', 'lang': 'python',
                               'code': []}

            is_in_comment_block = True
            collecting_code = False  # 结束代码收集

            # 提取注释内容，考虑空注释行
            comment_line = repr(line_stripped[1:].strip())[1:-1] if len(line_stripped) > 1 else '\n'
            comment_lines.append(comment_line)

        else:
            if is_in_comment_block:
                # 处理收集的注释块
                full_comment = ''.join(comment_lines)
                if comment_lines[0].startswith('#'):
                    title_level = len(re.match(r'^#+', comment_lines[0]).group(0))
                    current_section['title'] = comment_lines[0][title_level:].strip()
                current_section['description'] = full_comment
                comment_lines = []
                is_in_comment_block = False

            if line_stripped == '' and not collecting_code:
                # 忽略代码块前的空行
                continue

            # 开始收集代码行
            collecting_code = True
            code_block.append({'line_num': str(line_num), 'content': line.rstrip()})

    # 检查是否有未处理的注释块
    if is_in_comment_block and comment_lines:
        full_comment = ''.join(comment_lines)
        if comment_lines[0].startswith('#'):
            title_level = len(re.match(r'^#+', comment_lines[0]).group(0))
            current_section['title'] = comment_lines[0][title_level:].strip()
        current_section['description'] = full_comment

    # 保存最后一个代码块
    if current_section:
        current_section['code'] = code_block
        sections.append(current_section)

    return sections


# 使用方式：


