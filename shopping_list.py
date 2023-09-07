import glob, re
import sys

def shopping_list( file_list ):
    shop_list = []
    for filename in file_list:
        with open(filename, 'r') as f:
            for line in f:
              match = re.search("\*\ \[\ \]", line)
              if match:
                shop_list.append(line)
    return shop_list
    
if __name__ == '__main__':
    file_list = sys.argv[1:]
    if not file_list:
        file_list = glob.glob("experiences/*.md")

    with open("shopping_list.md", 'w') as shop_file:
        shop_file.write(f"""# Liste de courses pour *La science pour les nuls*

{"".join(shopping_list( file_list ))}""")

