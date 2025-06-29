import re
import os

def tools_list_to_table(content: str) -> str:
    """
    Converts numbered tool blocks to Markdown table rows, separated by ---- lines.
    Each block should be in the format:
      1. **ToolName**
          - Description
          - URL
    Returns a string with each tool as a Markdown table row.
    """
    # Regex pattern to match each tool block (number, name, description, URL)
    pattern = re.compile(
        r'(\d+)\.\s+\*\*(.+?)\*\*\n\s*-\s+(.+?)\n\s*-\s+(https?://\S+)', re.MULTILINE
    )

    def repl(match):
        # Extract tool name, description, and URL from the match groups
        name = match.group(2).strip()
        desc = match.group(3).strip()
        url = match.group(4).strip()
        # Format as a Markdown table row, followed by a separator
        return f'| [{name}]({url}) | {desc} |\n'

    # Replace all tool blocks in the content with formatted table rows
    table_rows = pattern.sub(repl, content)
    return table_rows

def list_history_files():
    print("\n📁 Available history files:")
    md_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.md')]
    if not md_files:
        print("No .md files found in current directory.")
    else:
        for f in md_files:
            print(f"- {f}")
    print()

def startupTemp():
    """
    Interactive function that prompts the user to paste tool blocks.
    The user can paste multiple lines, and types 'stop' on a line by itself to finish.
    The function then processes the input and writes the formatted table to a file.
    """
    print("Paste your tool blocks below. Type 'stop' on a line by itself to finish.")
    print("Type 'line' to insert a line break in the input.\n")
    lines = []
    while True:
        try:
            line = input()
            if line.strip().lower() == "stop":
                break
            if line.strip().lower() == "line":
                print("this is a line break, continuing input...")
                lines.append("\n\n")
            else:
                lines.append(line)
        except EOFError:
            break
    # Join all input lines into a single string
    lines.append("\n\n")
    content = "\n".join(lines)
    # Convert the tool blocks to Markdown table rows
    table_content = tools_list_to_table(content)
    output_file = "formatted_tools.md"
    # Write the result to the output file
    with open(output_file, "a", encoding="utf-8") as f:
        f.write(table_content)
    print(f"\nConversion complete. Output written to {output_file}")

def load_history(filename):

    if os.path.exists(filename):

        with open(filename, "r") as f:

            lines = [line.strip() for line in f.readlines() if line.strip()]

            return lines

    return []

def save_history(history, filename):

    with open(filename, "w") as f:

        for line in history:

            f.write(line + "\n")

def choose_mode():
    print("\nChoose an option:\n")
    print("1. Convert blocks")
    print("2. Show only letters (ignore dashes '-')")
    print("3. Show all characters but no definitions for '-'")
    print("4. Switch history file")
    choice = input("Enter 1, 2, 3, or 4: ").strip()
    if choice == "2":
        return 2
    elif choice == "3":
        return 3
    elif choice == "4":
        return 4
    else:
        return 1

def main():
    """
    Main entry point for the script.
    Prints a welcome message and (optionally) starts the interactive input.
    """
    print("Welcome to the Markdown Tool Formatter!")
    print("This tool converts numbered tool blocks into a Markdown table format.")
    # Uncomment the next line to enable interactive input:
    print("🧾 Printer Interpreter Tool\n")
    # List existing history files first
    list_history_files()
    # Then ask for filename
    history_file = input("Enter history filename (default 'history.md'): ").strip()
    if not history_file:
        history_file = "history.md"
    mode = choose_mode()
    history = load_history(history_file)
    try:
        while True: 
            if mode == 1:
                startupTemp()
                # print("\n".join(history))
            elif mode == 2:
                # print("".join([c for c in "".join(history) if c.isalpha()]))
                print("not implemented yet")

            elif mode == 3:
                # print("".join([c for c in "".join(history) if c != '-']))
                print("not implemented yet")

            elif mode == 4:
                list_history_files()
                new_file = input("Enter history filename to switch to: ").strip()
                if new_file:
                    print(f"Switching to history file: {new_file}")
                    history_file = new_file
                    history = load_history(history_file)
                else:
                    print("No file entered, staying with current history.")
                mode = choose_mode()
                continue
            if input_line == "menu":
                mode = choose_mode()
                continue
            if input_line in ["h", "history", "hist"]:
                # show_history(history, VALUE_MAP, mode)
                print("not implemented yet")
                continue
            if input_line == "ls":
                list_history_files()
                continue
    except Exception as e:
        print(f"An error occurred: {e}")
    

if __name__ == "__main__":
    main()
