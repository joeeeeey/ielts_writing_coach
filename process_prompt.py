import argparse
import re

def replace_tags(file_path, compress):
    # Define the replacements for compression and decompression
    if compress:
        replacements = {
            r'<span style="color:red; font-weight:bold;">': '#1#',
            r'</span>': '#2#'
        }
    else:
        replacements = {
            r'#1#': '<span style="color:red; font-weight:bold;">',
            r'#2#': '</span>'
        }
    
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Perform replacements based on the replacement dictionary
    for old, new in replacements.items():
        content = re.sub(re.escape(old), new, content)
    
    # Output the modified content
    return content

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Compress or decompress HTML tags in a file.')
    parser.add_argument('compress', type=int, help='Compress flag (1 for compress, 0 for decompress)')
    parser.add_argument('file_path', type=str, help='Path to the file to be processed')
    args = parser.parse_args()
    
    # Convert compress to boolean
    compress = bool(args.compress)
    
    # Replace tags based on compress value
    result = replace_tags(args.file_path, compress)
    
    # Print the result to stdout
    # rewrite the file
    with open(args.file_path, 'w', encoding='utf-8') as file:
        file.write(result)
    print(result)

if __name__ == '__main__':
    main()


# python process_prompt.py 1 output.txt
