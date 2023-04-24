import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]

sidebar_file = open('_sidebar.md', 'w')

# for file in files:
# 	if ".md" in file:
# 		name = file.split(".md")
# 		file = file.replace(" ", "%20")
# 		sidebar_file.write( f"* [{name[0]}]({file})\n" )

def join(path, item):
    if path == '.':
        return item
    return os.path.join(path, item)

def print_file_tree(path='.', level=0):
    items = os.listdir(path)
    for item in items:
        if level==0 and item!="baguwen":
            continue
        fill_path = join(path, item)
        print('|' * level, '-', item)
        if os.path.isfile(fill_path):
            if ".md" in item:
                name = item.split(".md")
                file = item.replace(" ", "%20")
                sidebar_file.write(' ' * level*2 +'-'+ f" [{name[0]}]({fill_path})\n" )
        if os.path.isdir(fill_path):
            if item == "img":
                continue
            sidebar_file.write(' ' * level*2 +'-'+ f" {item}\n" )
            print_file_tree(fill_path, level + 1)

print_file_tree()
sidebar_file.close()