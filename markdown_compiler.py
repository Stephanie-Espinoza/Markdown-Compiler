
################################################################################
#
# The functions in this section operate on only a single line of text at a time.
#
################################################################################


from cgitb import text


def compile_headers(line):
    '''
    Convert markdown headers into <h1>,<h2>,etc tags.

    >>> compile_headers('# This is the main header')
    '<h1> This is the main header</h1>'
    >>> compile_headers('## This is a sub-header')
    '<h2> This is a sub-header</h2>'
    >>> compile_headers('### This is a sub-header')
    '<h3> This is a sub-header</h3>'
    >>> compile_headers('#### This is a sub-header')
    '<h4> This is a sub-header</h4>'
    >>> compile_headers('##### This is a sub-header')
    '<h5> This is a sub-header</h5>'
    >>> compile_headers('###### This is a sub-header')
    '<h6> This is a sub-header</h6>'
    >>> compile_headers('      # this is not a header')
    '      # this is not a header'
    '''

    if line[:6]=='######':
        nl = '<h6>' + line[6:] + '</h6>'
    elif line[:5]=='#####':
        nl = '<h5>' + line[5:] + '</h5>'
    elif line[:4]=='####':
        nl = '<h4>' + line[4:] + '</h4>'
    elif line[:3]=='###':
        nl = '<h3>' + line[3:] + '</h3>'
    elif line[:2]=='##':
        nl = '<h2>' + line[2:] + '</h2>'
    elif line[:1]=='#':
        nl = '<h1>' + line[1:] + '</h1>'
    else:
        nl = line
    return nl 




def compile_italic_star(line):
    '''
    Convert "*italic*" into "<i>italic</i>".

    >>> compile_italic_star('*This is italic!* This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_star('*This is italic!*')
    '<i>This is italic!</i>'
    >>> compile_italic_star('This is *italic*!')
    'This is <i>italic</i>!'
    >>> compile_italic_star('This is not *italic!')
    'This is not *italic!'
    >>> compile_italic_star('*')
    '*'
    '''

    accumulator = ''
    inside_italic_tag = False 
    i_count = 1
    i_total_count = 0

    for c in line:
        if c == '*':
            i_total_count = i_total_count + 1

    for c in line:
        if c == '*':
            inside_italic_tag = True 
        if c == '*':
            inside_italic_tag = False
        if c != '*' and inside_italic_tag==False:
            accumulator += c 
        if c == '*' and inside_italic_tag == False:
            if i_total_count%2==0:
                i_count = i_count + 1 
                if i_count%2==0:
                    nc = c.replace('*',"<i>")
                    accumulator += nc 
                if i_count%2==1:
                    nc2 = c.replace('*',"</i>")
                    accumulator += nc2
            else:
                return line 
    return accumulator




def compile_italic_underscore(line):
    '''
    Convert "_italic_" into "<i>italic</i>".

    >>> compile_italic_underscore('_This is italic!_ This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_underscore('_This is italic!_')
    '<i>This is italic!</i>'
    >>> compile_italic_underscore('This is _italic_!')
    'This is <i>italic</i>!'
    >>> compile_italic_underscore('This is not _italic!')
    'This is not _italic!'
    >>> compile_italic_underscore('_')
    '_'
    '''


    accumulator = ''
    inside_italic_tag = False 
    i_count = 1
    i_total_count = 0

    for c in line:
        if c == '_':
            i_total_count = i_total_count + 1

    for c in line:
        if c == '_':
            inside_italic_tag = True 
        if c == '_':
            inside_italic_tag = False
        if c != '_' and inside_italic_tag==False:
            accumulator += c 
        if c == '_' and inside_italic_tag == False:
            if i_total_count%2==0:
                i_count = i_count + 1 
                if i_count%2==0:
                    nc = c.replace('_',"<i>")
                    accumulator += nc 
                if i_count%2==1:
                    nc2 = c.replace('_',"</i>")
                    accumulator += nc2
            else:
                return line 
    return accumulator



def compile_strikethrough(line):
    '''
    Convert "~~strikethrough~~" to "<ins>strikethrough</ins>".

    >>> compile_strikethrough('~~This is strikethrough!~~ This is not strikethrough.')
    '<ins>This is strikethrough!</ins> This is not strikethrough.'
    >>> compile_strikethrough('~~This is strikethrough!~~')
    '<ins>This is strikethrough!</ins>'
    >>> compile_strikethrough('This is ~~strikethrough~~!')
    'This is <ins>strikethrough</ins>!'
    >>> compile_strikethrough('This is not ~~strikethrough!')
    'This is not ~~strikethrough!'
    >>> compile_strikethrough('~~')
    '~~'
    '''

    if line == '~~':
        return line 
    x = line.count('~~')
    if x==1:
        return line 
    else: 
        r = line.replace('~~','<ins>',1)
        r2 = r.replace('~~','</ins>',1)
        return r2



def compile_bold_stars(line):
    '''
    Convert "**bold**" to "<b>bold</b>".

    >>> compile_bold_stars('**This is bold!** This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_stars('**This is bold!**')
    '<b>This is bold!</b>'
    >>> compile_bold_stars('This is **bold**!')
    'This is <b>bold</b>!'
    >>> compile_bold_stars('This is not **bold!')
    'This is not **bold!'
    >>> compile_bold_stars('**')
    '**'
    '''

    if line == '**':
        return line 
    x = line.count('**')
    if x==1:
        return line 
    else: 
        r = line.replace('**','<b>',1)
        r2 = r.replace('**','</b>',1)
        return r2


def compile_bold_underscore(line):
    '''
    Convert "__bold__" to "<b>bold</b>".

    >>> compile_bold_underscore('__This is bold!__ This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_underscore('__This is bold!__')
    '<b>This is bold!</b>'
    >>> compile_bold_underscore('This is __bold__!')
    'This is <b>bold</b>!'
    >>> compile_bold_underscore('This is not __bold!')
    'This is not __bold!'
    >>> compile_bold_underscore('__')
    '__'
    '''

    if line == '__':
        return line 
    x = line.count('__')
    if x==1:
        return line 
    else: 
        r = line.replace('__','<b>',1)
        r2 = r.replace('__','</b>',1)
        return r2



def compile_code_inline(line):
    '''
    Add <code> tags.

    >>> compile_code_inline('You can use backticks like this (`1+2`) to include code in the middle of text.')
    'You can use backticks like this (<code>1+2</code>) to include code in the middle of text.'
    >>> compile_code_inline('This is inline code: `1+2`')
    'This is inline code: <code>1+2</code>'
    >>> compile_code_inline('`1+2`')
    '<code>1+2</code>'
    >>> compile_code_inline('This example has html within the code: `<b>bold!</b>`')
    'This example has html within the code: <code>&lt;b&gt;bold!&lt;/b&gt;</code>'
    >>> compile_code_inline('this example has a math formula in the  code: `1 + 2 < 4`')
    'this example has a math formula in the  code: <code>1 + 2 &lt; 4</code>'
    >>> compile_code_inline('this example has a <b>math formula</b> in the  code: `1 + 2 < 4`')
    'this example has a <b>math formula</b> in the  code: <code>1 + 2 &lt; 4</code>'
    >>> compile_code_inline('```')
    '```'
    >>> compile_code_inline('```python3')
    '```python3'
    '''

    accumulator = ''
    inside_code_tag = False 
    i_count = 1
    i_total_count = 0

    for c in line:
        if c == '`':
            i_total_count = i_total_count + 1

    for c in line:
        if c == '`' and i_count%2==1:
            inside_code_tag = True 
        if c == '`' and i_count%2==0:
            inside_code_tag = True
        if c == '>' and inside_code_tag==True:
            new_bt = c.replace('>',"&gt;")
            accumulator += new_bt
        if c == '<' and inside_code_tag==True:
            new_lt = c.replace('<',"&lt;")
            accumulator += new_lt
        if c != '`' and inside_code_tag==False:
            accumulator += c 
        if c != '`' and c != '<' and c != '>' and inside_code_tag==True:
            accumulator += c 
        if c == '`' and inside_code_tag == True:
            if i_total_count%2==0:
                i_count = i_count + 1 
                if i_count%2==0:
                    nc = c.replace('`',"<code>")
                    accumulator += nc 
                if i_count%2==1:
                    nc2 = c.replace('`',"</code>")
                    accumulator += nc2
            else:
                return line 
    return accumulator




def compile_links(line):
    '''
    Add <a> tags.

    >>> compile_links('Click on the [course webpage](https://github.com/mikeizbicki/cmc-csci040)!')
    'Click on the <a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>!'
    >>> compile_links('[course webpage](https://github.com/mikeizbicki/cmc-csci040)')
    '<a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>'
    >>> compile_links('this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)')
    'this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)'
    >>> compile_links('this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040')
    'this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040'
    '''

    accumulator = ''
    name = ''

    position_bracket = line.find(']') 

    inside_name = False
    i_total_count = 0
    # check if the one that follow is bracket 

    for c in line:
        if c == '(' or c==')':
            i_total_count = i_total_count + 1

    if i_total_count<2:
        return line

    if line[position_bracket +1] != '(':
        return line

    for c in line:
        if c == '[':
            inside_name = True 
        if c == ']':
            inside_name = False
        if c != '[' and c != ']' and inside_name==True:
            name += c
        if c != '(' and c != ')' and c != '[' and c != ']' and inside_name==False:
            accumulator += c 
        if c == '(':
            no = c.replace('(','<a href="')
            accumulator += no
        if c == ')': 
            nc=c.replace(')','">')
            tnc_end = '</a>'
            tnc = nc + name + tnc_end
            accumulator += tnc
    return accumulator



def compile_images(line):
    '''
    Add <img> tags.

    >>> compile_images('[Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    '[Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)'
    >>> compile_images('![Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    '<img src="https://avatars1.githubusercontent.com/u/1052630?v=2&s=460" alt="Mike Izbicki" />'
    >>> compile_images('This is an image of Mike Izbicki: ![Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    'This is an image of Mike Izbicki: <img src="https://avatars1.githubusercontent.com/u/1052630?v=2&s=460" alt="Mike Izbicki" />'
    '''


    start_bracket=line.find('[')
    end_bracket=line.find(']')
    start_parent=line.find('(')
    end_parent=line.find(')')
    if line[start_bracket-1]=="!":
        if start_bracket>-1 and end_bracket>-1 and start_parent>-1 and end_parent>-1:
            if start_bracket<end_bracket and end_bracket+1==start_parent and start_parent<end_parent:
                line = line[:start_bracket-1]+'<img src="' + line[start_parent+1:end_parent]+'" alt="'+line[start_bracket +1:end_bracket]+'" />'+line[end_parent+1:]
    return line



################################################################################
#
# This next section contains only one function that calls the functions in the previous section.
# This is the "brains" of our application right here.
#
################################################################################


def compile_lines(text):
    r'''
    Apply all markdown transformations to the input text.

    >>> compile_lines('This is a **bold** _italic_ `code` test.\nAnd *another line*!\n')
    '<p>\nThis is a <b>bold</b> <i>italic</i> <code>code</code> test.\nAnd <i>another line</i>!\n</p>'

    >>> compile_lines("""
    ... This is a **bold** _italic_ `code` test.
    ... And *another line*!
    ... """)
    '\n<p>\nThis is a <b>bold</b> <i>italic</i> <code>code</code> test.\nAnd <i>another line</i>!\n</p>'

    >>> print(compile_lines("""
    ... This is a **bold** _italic_ `code` test.
    ... And *another line*!
    ... """))
    <BLANKLINE>
    <p>
    This is a <b>bold</b> <i>italic</i> <code>code</code> test.
    And <i>another line</i>!
    </p>

    >>> print(compile_lines("""
    ... *paragraph1*
    ...
    ... **paragraph2**
    ...
    ... `paragraph3`
    ... """))
    <BLANKLINE>
    <p>
    <i>paragraph1</i>
    </p>
    <p>
    <b>paragraph2</b>
    </p>
    <p>
    <code>paragraph3</code>
    </p>


    >>> print(compile_lines("""
    ... ```
    ... x = 1*2 + 3*4
    ... ```
    ... """))
    <BLANKLINE>
    <pre>
    x = 1*2 + 3*4
    </pre>
    <BLANKLINE>

    >>> print(compile_lines("""
    ... Consider the following code block:
    ... ```
    ... x = 1*2 + 3*4
    ... ```
    ... """))
    <BLANKLINE>
    <p>
    Consider the following code block:
    <pre>
    x = 1*2 + 3*4
    </pre>
    </p>

    >>> print(compile_lines("""
    ... Consider the following code block:
    ... ```
    ... x = 1*2 + 3*4
    ... print('x=', x)
    ... ```
    ... And here's another code block:
    ... ```
    ... print(this_is_a_variable)
    ... ```
    ... """))
    <BLANKLINE>
    <p>
    Consider the following code block:
    <pre>
    x = 1*2 + 3*4
    print('x=', x)
    </pre>
    And here's another code block:
    <pre>
    print(this_is_a_variable)
    </pre>
    </p>

    >>> print(compile_lines("""
    ... ```
    ... for i in range(10):
    ...     print('i=',i)
    ... ```
    ... """))
    <BLANKLINE>
    <pre>
    for i in range(10):
        print('i=',i)
    </pre>
    <BLANKLINE>
    '''

    lines = text.split('\n')
    new_lines = []
    c=False 
    in_paragraph = False
    for line in lines:
        if line=='':
            if in_paragraph:
                line='</p>'
                in_paragraph = False
        elif line=='```':
            if c==False:
                line='<pre>'
                c=True
            else: 
                line='</pre>'
                c=False
        elif c==False:
            if line[0] != '#' and not in_paragraph:
                in_paragraph = True
                line = '<p>\n'+line
            line = compile_headers(line)
            line = compile_strikethrough(line)
            line = compile_bold_stars(line)
            line = compile_bold_underscore(line)
            line = compile_italic_star(line)
            line = compile_italic_underscore(line)
            line = compile_code_inline(line)
            line = compile_images(line)
            line = compile_links(line)
        new_lines.append(line)
    new_text = '\n'.join(new_lines)
    return new_text


def markdown_to_html(markdown, add_css):
    '''
    Convert the input markdown into valid HTML,
    optionally adding CSS formatting.

    >>> assert(markdown_to_html('this *is* a _test_', False))
    >>> assert(markdown_to_html('this *is* a _test_', True))
    '''

    html = '''
<html>
<head>
    <style>
    ins { text-decoration: line-through; }
    </style>
    '''
    if add_css:
        html += '''
<link rel="stylesheet" href="https://izbicki.me/css/code.css" />
<link rel="stylesheet" href="https://izbicki.me/css/default.css" />
        '''
    html+='''
</head>
<body>
    '''+compile_lines(markdown)+'''
</body>
</html>
    '''
    return html


def minify(html):
    r'''
    Remove redundant whitespace (spaces and newlines) from the input HTML,
    and convert all whitespace characters into spaces.

    >>> minify('       ')
    ''
    >>> minify('   a    ')
    'a'
    >>> minify('   a    b        c    ')
    'a b c'
    >>> minify('a b c')
    'a b c'
    >>> minify('a\nb\nc')
    'a b c'
    >>> minify('a \nb\n c')
    'a b c'
    >>> minify('a\n\n\n\n\n\n\n\n\n\n\n\n\n\nb\n\n\n\n\n\n\n\n\n\n')
    'a b'
    '''

    h_split = html.split()
    f_return = " ".join(h_split)
    return f_return


def convert_file(input_file, add_css):
    '''
    Convert the input markdown file into an HTML file.
    If the input filename is `README.md`,
    then the output filename will be `README.html`.
    '''

    # validate that the input file is a markdown file
    if input_file[-3:] != '.md':
        raise ValueError('input_file does not end in .md')

    # load the input file
    with open(input_file, 'r') as f:
        markdown = f.read()

    # generate the HTML from the Markdown
    html = markdown_to_html(markdown, add_css)
    html = minify(html)

    # write the output file
    with open(input_file[:-2]+'html', 'w') as f:
        f.write(html)


################################################################################
#
# This final section does not need to be modified at all.
# It connects commands run in the terminal environment to the python functions above.
#
################################################################################

if __name__ == '__main__':

    # process command line arguments
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    parser.add_argument('--add_css', action='store_true')
    args = parser.parse_args()

    # call the main function
    convert_file(args.input_file, args.add_css)
