#!/usr/bin/env python3

import json

import os

# Position-specific value map (directly in the script)

TYPE_CODE_MAP = {

    "--": "Transaction is not initiated",

    "00":  "Purchase",

    "01": "Refund",

    "02":  "Void",

    "03":  "Void return",

}   

VALUE_MAP = {

    "1": {

    "-": "Chip card is not inserted",

    "I": "Chip card is inserted",

    "R": "Chip card is removed"

    },

    "2": {

    "-": "EMV process is not started",

    "S": "EMV process is started"

    },

    "3": {

    "-": "Incomplete",

    "C": "Completed",

    "A": "Completed with approval",

    "D": "Completed with decline",

    "E": "Error or incomplete data",

    "F": "Fallback to MSR (unsupported)"

    },

    "4": {

    "-": "Unselected",

    "M": "Manually selected",

    "A": "Automatically selected"

    },

    "5": {

    "-": "Unselected",

    "M": "Manually selected",

    "A": "Automatically selected"

    },

    "6": {

    "-": "Unconfirmed",

    "A": "Confirmation accepted",

    "R": "Confirmation rejected"

    },

    "7": {

    "-": "Rewards request is not received",

    "R": "Rewards request is received",

    "S": "Rewards response sent"

    },

    "8": {

    "-": "Payment type request is not received",

    "R": "Payment type request is received",

    "S": "Payment type response sent"

    },

    "9": {

    "-": "Amount unconfirmed",

    "A": "Amount confirmation accepted",

    "R": "Confirmation rejected"

    },

    "10": {

    "-": "This is not the last PIN try",

    "L": "This is the last PIN try"

    },

    "11": {

    "-": "Offline PIN is not entered",

    "P": "Offline PIN is entered",

    "B": "PIN bypassed"

    },

    "12": {

    "-": "Account type is not selected",

    "C": "Checking account type is selected",

    "S": "Savings account type is selected"

    },

    "13": {

    "-": "Authorization request is not sent",

    "S": "Authorization request is sent",

    "F": "Authorization request failed to send"

    },

    "14": {

    "-": "Authorization response is not received",

    "R": "Authorization response is received",

    "T": "Internal terminal timeout on authorization response",

    "H": "Register indication of no Host available; down or timeout"

    },

    "15": {

    "-": "Confirmation response is unsent",

    "S": "Confirmation response is sent",

    "F": "Confirmation response failed to send"

    },

    "16": {

    "-": "Transaction is not canceled",

    "C": "Transaction is canceled"

    },

    "17": {

    "-": "Card data is not invalid or is not detected",

    "I": "Card data is invalid but fallback is allowed",

    "N": "Card data invalid, fallback data not allowed due to being an Interac debit transaction"

    },

    "18": {

    "-": "Card or application block is not detected",

    "A": "Application is blocked",

    "B": "Card is blocked"

    },

    "19": {

    "-": "No fatal error is detected",

    "F": "Fatal error is detected",

    "K": "Track-2 data consistency failed",

    "O": "User interface timeout",

    "X": "EMV card application is expired",

    "C": "Cashback error (such as, cashback amount > current transaction maximum cashback amount)",

    "B": "Cashback requested before PIN-entry, but PIN bypassed",

    "T": "More than three taps",

    "M": "MSD card not supported"

    },

    "20": {

    "-": "No premature card removal detected",

    "R": "Premature card removal detected"

    },

    "21": {

    "-": "No status is available",

    "N": "Card is not supported (such as, application ID not found)"

    },

    "22": {

    "-": "No MAC verification performed in transaction",

    "P": "MAC verification passed",

    "F": "MAC verification failed"

    },

    "23": {

    "-": "Post confirmation wait is not started",

    "S": "Post confirmation wait started"

    },

    "24": {

    "-": "No signature request is detected and started ",

    "S": "Signature request is detected and started ",

    "E": "Signature request is complete ",

    "R": "Paper signature requested"

    },

    "25": {

    "-": "Transaction preparation response not sent",

    "S": "Transaction preparation response sent",

    "F": "Transaction preparation response failed to send"

    },

    "26": {

    "-": "EMV flow is not suspended",

    "1": "EMV flow is suspended",

    "0": "EMV flow resumed"

    },

    "27": {

    "-": "Initialized state at start of transaction",

    "R": "PIN entry request. Flag set to R at start of the first online PIN entry",

    "C": "PIN entry canceled, having failed due to invalid PIN. It remains set as R if manually canceled by the Cancel button",

    "A": "PIN block is accepted and valid. Updated when host returns T8A = 00 or other transaction approval",

    "B": "PIN bypassed. Can be bypassed via Cancel button or card removal",

    "E": "PIN entry failed for any error (including PIN entry timeout)",

    "I": "PIN entered is invalid. Updated when host returns T8A = 55. PIN entry restarts, but the flag remains set to I until updated (rather than resetting to -)",

    "D": "PIN not verified. Updated when host returns T8A = 05 or other transaction declined notification"

    },

    "28": {

    "0": "Post-PIN cash back Enables cashback amount selection after PIN entry.",

    "2": "Process CVM",

    "3": "Contact Flow Complete Marks the true end of the EMV flow after all transaction steps are complete.",

    "A": "Start Transaction The EMV transaction started. Used for POS information; suspend not required.",

    "B": "Select language service Language selection is performed on the terminal. Used for POS information; suspend not required.",

    "C": "Select AID service Application ID selection is performed on the terminal. Used for POS information; suspend not required.",

    "D": "Cardholder AID confirmation Cardholder confirms the application selection. Used for POS information; suspend not required.",

    "E": "Application final selection Sets EMV proprietary tags during the transaction. Suspend is required to set data.    Note: If the card has more than one application, and the first application is not supported but the second one is supported, the suspend step is sent for the second, supported application only.",

    "F": "Get amount application selection Sets the transaction total amount. The transaction should be suspended during this step to set the transaction total amount using the 13.x message. Avoid updating tags mid-flow.",

    "G": "Set proprietary tags at application selection Supports dynamic currency conversion. Sets EMV proprietary tags during the transaction. Suspend is required to set data. Suspend is required to enable synchronization.",

    "H": "Read application data PAN ready (to stop for partial EMV) Stops a partial EMV transaction. The application is suspended, and the 33.09 Set Tag Data message can be used with command A (Request AAC for partial EMV transaction). Used in an optimized Quick Chip transaction.",

    "I": "Set payment type Non-EMV step to set the payment type.",

    "J": "Get cashback amount Non-EMV step to get the cashback amount. Used in an optimized Quick Chip cashback transaction.",

    "K": "Read application data change amount Changes the transaction total amount using the 13.x message. Two suspend steps are needed for the final amount confirmation.",

    "L": "Amount confirmation Non-EMV step to confirm the amount.",

    "M": "Account selection Non-EMV step to select the account type (checking or savings).",

    "N": "Offline PIN entry Used for offline entry; the cardholder must enter their PIN. Used for POS information.",

    "O": "Online PIN entry Used for online entry; the cardholder must enter their PIN. Used for POS information.",

    "P": "Last transaction data request Bypasses the last EMV transaction data to the application. For example: To pass the last transaction data in the same batch performed using the same card.",

    "Q": "Terminal action analysis (to stop for partial EMV) Stops a partial EMV transaction. The 33.09 Set Tag Data message can be used with command A (Request AAC for partial EMV transaction).",

    "R": "Online authorization response in progress Suspend step used after the 33.03 Authorization Request Message is sent and before waiting on the 33.04 2nd Gen AC Request message, allowing on-demand control. Use this step to send online on-demand PIN retries without generating a new cryptogram for each try.",

    "S": "EMV stop Transaction ended. Used for POS information.",

    "T": "CMV Modification Modify terminal capabilities after Confirm Aid and before Select App, if configured.",

    "U": "Completion Status. End of transaction control. Allows users to:,    Ignore a card decline, and the terminal displays approval    Display custom messages instead of or with approved/declined status    Provide custom display and/or beeps (using the 51.x Beep Message to prompt a cardholder to remove the card    Resuming during this step returns the screen to transaction results.    Notes:    1. Do not use reset messages when suspended at Step U. Instead, use the 33.09 Set Tag Data Message to resume or skip. Then, reset messages can be used.    2. In a specific scenario, a blank form displays until a reset message is sent. If the card is removed after the 33.09J (skip) and Please Remove Card message is displayed following the use of custom display(s) at Step U, a blank form is displayed until a reset message is received from the POS. This blank form can be modified using the 70.x Update Form Element if the form includes dynamic prompts.",

    "V": "External Application Selection Suspends an Optimized Quick-Chip transaction with external AID selection so the POS can send on-demand custom form(s)."

    },

    "29": {

    "-": "Reserved"

    },

    "30": {

    "-": "Reserved"

    },

    "31": {

    "-": "Initialized at start state (before cashback request is set)",

    "R": "Cash back requested (when configuration is set)",

    "C": "Cash back accepted (after the cashback value is set by the POS)"

    },

    "32": {

    "-": "Contactless transaction not yet started",

    "1": "Contactless transaction started",

    "0": "Contactless transaction stopped"

    },

    "33": {

    "-": "No error",

    "C": "Collision detected",

    "R": "Re-tap required"

    }

}

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

def interpret_line(input_str, value_map, mode=1):

    if len(input_str) < 2:

        return "Input too short."

    type_code = input_str[:2]

    body = input_str[2:]

    type_meaning = TYPE_CODE_MAP.get(type_code, "Unknown type code")

    result = [f"\nType Code '{type_code}': {type_meaning}"]

    for i, char in enumerate(body, start=1):

        if mode == 2 and char == "-":

            continue

    meaning = value_map.get(str(i), {}).get(char, "Unknown")

    if mode == 3 and char == "-":

        result.append(f"{i:2}. {char}")

    else:

        result.append(f"{i:2}. {char}  → {meaning}")

        return "\n".join(result)

def choose_mode():

    print("\nChoose an option:\n")

    print("1. Show all characters with definitions")

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

def show_history(history, value_map, mode):
    if not history:
        print("\n📜 History is empty.\n")
        return
    print("\n📜 Full History (type back to exit, !<number> to re-run):\n")
    while True:
        for idx, item in enumerate(history, 1):
            print(f"{idx:2}. {item}")
            print(interpret_line(item, value_map, mode))
            print("-" * 40)
        cmd = input("History (type back to exit, !<number> to re-run)> ").strip().lower()
        if cmd == "back":
            print("\nReturning to main input...\n")
            break
        elif cmd.startswith("!"):
            try:
                num = int(cmd[1:])
                if 1 <= num <= len(history):
                    chosen = history[num-1]
                    print(f"\nRe-running input #{num}: {chosen}\n")
                    print(interpret_line(chosen, value_map, mode))
                    print("-" * 40)
                else:
                    print(f"Invalid number. Choose between 1 and {len(history)}.")
            except ValueError:
                print("Invalid command format. Use !<number> to re-run.")
        else:
            print("Type 'back' to return or !<number> to re-run a past input.")


def save_history(history, filename):
    with open(filename, "w") as f:
        for line in history:
            f.write(line + "\n")

def interpret_line(input_str, value_map, mode=1):
    if len(input_str) < 2:
        return "Input too short."
    type_code = input_str[:2]
    body = input_str[2:]
    type_meaning = TYPE_CODE_MAP.get(type_code, "Unknown type code")
    result = [f"\nType Code '{type_code}': {type_meaning}"]
    for i, char in enumerate(body, start=1):
        if mode == 2 and char == "-":
            continue
        meaning = value_map.get(str(i), {}).get(char, "Unknown")
        if mode == 3 and char == "-":
            result.append(f"{i:2}. {char}")
        else:
            result.append(f"{i:2}. {char}  → {meaning}")
    return "\n".join(result)

def choose_mode():
    print("\nChoose an option:\n")
    print("1. Show all characters with definitions")
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

def show_history(history, value_map, mode):
    if not history:
        print("\n📜 History is empty.\n")
        return
    print("\n📜 Full History (type back to exit, !<number> to re-run):\n")
    while True:
        for idx, item in enumerate(history, 1):
            print(f"{idx:2}. {item}")
            print(interpret_line(item, value_map, mode))
            print("-" * 40)
        cmd = input("History (type back to exit, !<number> to re-run)> ").strip().lower()
        if cmd == "back":
            print("\nReturning to main input...\n")
            break
        elif cmd.startswith("!"):
            try:
                num = int(cmd[1:])
                if 1 <= num <= len(history):
                    chosen = history[num-1]
                    print(f"\nRe-running input #{num}: {chosen}\n")
                    print(interpret_line(chosen, value_map, mode))
                    print("-" * 40)
                else:
                    print(f"Invalid number. Choose between 1 and {len(history)}.")
            except ValueError:
                print("Invalid command format. Use !<number> to re-run.")
        else:
            print("Type 'back' to return or !<number> to re-run a past input.")

def list_history_files():
    print("\n📁 Available history files:")
    txt_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt')]
    if not txt_files:
        print("No .txt files found in current directory.")
    else:
        for f in txt_files:
            print(f"- {f}")
    print()

def main():
    print("🧾 Printer Interpreter Tool\n")
    # List existing history files first
    list_history_files()
    # Then ask for filename
    history_file = input("Enter history filename (default 'history.txt'): ").strip()
    if not history_file:
        history_file = "history.txt"
    mode = choose_mode()
    history = load_history(history_file)
    try:
        while True:
            if mode == 4:
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
            input_line = input("Input (menu, h/hist for history, ls to list, switch <file>, Ctrl+C to quit): ").strip()
            # handle commands first
            if input_line == "menu":
                mode = choose_mode()
                continue
            if input_line in ["h", "history", "hist"]:
                show_history(history, VALUE_MAP, mode)
                continue
            if input_line == "ls":
                list_history_files()
                continue
            if input_line.startswith("switch"):
                parts = input_line.split(maxsplit=1)
                if len(parts) == 2:
                    new_file = parts[1].strip()
                    if new_file:
                        print(f"Switching to history file: {new_file}")
                        history_file = new_file
                        history = load_history(history_file)
                    else:
                        print("Usage: switch <filename>")
                else:
                    print("Usage: switch <filename>")
                continue
            if not input_line:
                continue
            # split input_line by spaces to process multiple inputs
            inputs = input_line.split()
            for inp in inputs:
                if len(inp) < 2:
                    print(f"Input '{inp}' too short, skipping.\n")
                    continue
                history.append(inp)
                save_history(history, history_file)
                print(f"\nInterpreted Output for: {inp}\n")
                print(interpret_line(inp, VALUE_MAP, mode))
                print("\n" + "=" * 40 + "\n")
    except KeyboardInterrupt:
        print("\nExited.")

if __name__ == "__main__":
    main()