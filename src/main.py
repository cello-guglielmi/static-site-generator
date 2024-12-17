from text_node import TextType, TextNode
from markdown_html_conversion import markdown_to_htmlnode
from test_suite import test2
import os, shutil, re

FROM = 'content'
DEST = 'public'
TEMPLATE = 'template.html'

def copy_contents(src, dst):
    src_subcontents = os.listdir(src)
    for item in src_subcontents:
        item_path = os.path.join(src, item)
        if os.path.isfile(item_path):
            print(f"Copying file: {item_path} to {dst}")
            shutil.copy(item_path, dst)
        else:
            subfolder = os.path.join(dst, item)
            print(f'Creating directory: {subfolder}')
            os.mkdir(subfolder)
            copy_contents(item_path, subfolder)


def copy_to_public():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(root_dir, 'static')
    public_dir = os.path.join(root_dir, 'public')
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)
    copy_contents(static_dir, public_dir)


def extract_title(markdown):
    header1 = re.match(r'# (.*?)\s*$', markdown, re.MULTILINE)
    if not header1:
        raise Exception('No title found under Header-1 format "# Text"')
    return header1.group(1)


def generate_page(from_path, template_path, dest_path): 
    print(f'Generating page from {from_path} to {dest_path}, using {template_path}.')

    with open(from_path) as file:
        content = file.read()
    with open(template_path) as file:
        template = file.read()

    page_title = extract_title(content)
    page_content = markdown_to_htmlnode(content).to_html()
    html_page = template.replace('{{ Title }}', page_title).replace('{{ Content }}', page_content)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    file_root, file_ext = os.path.splitext(dest_path)
    if file_ext == '.md':
        dest_path = file_root + '.html'
    with open(dest_path, 'w') as file:
        file.write(html_page)
    return


def generate_pages_recursive(from_dir, template_path, dest_dir):
    subcontents = os.listdir(from_dir)
    #print(subcontents)
    for item in subcontents:
        src_path = os.path.join(from_dir, item)
        dest_path = os.path.join(dest_dir, item)
        #print(src_path)
        #print(template_path)
        #print(dest_path)
        if os.path.isdir(src_path):
            os.mkdir(dest_path)
            generate_pages_recursive(src_path, template_path, dest_path)
        else:
            generate_page(src_path, template_path, dest_path)



def main():
    testnode = TextNode('This is a text node', TextType.BOLD, 'https://www.google.com')
    print(testnode)

if __name__=='__main__':
    copy_to_public()
    #generate_page('content/index.md', 'template.html', 'public/index.html')
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #                root     /      src     /     main.py
    from_dir = os.path.join(root_dir, FROM)
    dest_dir = os.path.join(root_dir, DEST)
    template_path = os.path.join(root_dir, TEMPLATE)
    generate_pages_recursive(from_dir, template_path, dest_dir)