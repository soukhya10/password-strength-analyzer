import sys
import string

# Ensure standard output and error streams use UTF-8 encoding.
# This prevents UnicodeEncodeError on Windows terminals when printing emojis (🔐) and checkmarks (✓, ✗).
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
if sys.stderr.encoding.lower() != 'utf-8':
    try:
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass


# We try to import colorama for beautifully colored terminal outputs.
# To keep the application beginner-friendly and extremely robust, we provide
# a fallback in case colorama is not installed, so the script still runs perfectly.
try:
    from colorama import init, Fore, Style
    # init() ensures colored outputs work correctly on Windows command prompts
    init(autoreset=True)
except ImportError:
    # If colorama is not installed, we mock the color objects with empty strings
    # so that the code runs without raising errors and prints normal text.
    class DummyColor:
        def __getattr__(self, name):
            return ""
    Fore = DummyColor()
    Style = DummyColor()


def check_password_strength(password):
    """
    Evaluates the strength of a given password based on length, 
    casing, numbers, and special characters.
    
    Returns a dictionary containing evaluation results, the final score, 
    the strength classification, and suggestions for improvement.
    """
    # 1. Define the criteria checklist
    checks = {
        "length_8": len(password) >= 8,
        "length_12": len(password) >= 12, # Bonus for extra security
        "has_upper": any(char.isupper() for char in password),
        "has_lower": any(char.islower() for char in password),
        "has_digit": any(char.isdigit() for char in password),
        "has_special": any(char in string.punctuation or (not char.isalnum() and not char.isspace()) for char in password)
    }

    # 2. Calculate the score
    # We assign 1 point for each met criteria (max 5 points)
    # Note: we use checks["length_8"] for basic length scoring. If a password is 12+ chars,
    # it gets the length point and qualifies as exceptionally strong.
    score = 0
    if checks["length_8"]:
        score += 1
    if checks["has_upper"]:
        score += 1
    if checks["has_lower"]:
        score += 1
    if checks["has_digit"]:
        score += 1
    if checks["has_special"]:
        score += 1

    # 3. Classify password strength
    # Security Rule: If a password is less than 8 characters, it is fundamentally 
    # vulnerable to brute force and is ALWAYS classified as Weak, regardless of other complexity.
    if len(password) < 8:
        strength = "Weak"
    elif score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    # 4. Generate actionable improvement suggestions
    suggestions = []
    if len(password) < 8:
        suggestions.append(f"Make your password longer. It should be at least {Fore.CYAN}8 characters{Style.RESET_ALL} (ideally {Fore.CYAN}12 or more{Style.RESET_ALL}).")
    elif len(password) < 12:
        suggestions.append(f"Consider extending your password to {Fore.CYAN}12+ characters{Style.RESET_ALL} for maximum resistance to modern cracking tools.")
        
    if not checks["has_upper"]:
        suggestions.append("Add at least one uppercase letter (A-Z).")
    if not checks["has_lower"]:
        suggestions.append("Add at least one lowercase letter (a-z).")
    if not checks["has_digit"]:
        suggestions.append("Add at least one number (0-9).")
    if not checks["has_special"]:
        suggestions.append("Add at least one special character (e.g., ! @ # $ % & *).")

    return {
        "checks": checks,
        "score": score,
        "strength": strength,
        "suggestions": suggestions
    }


def print_header():
    """Prints a beautiful title banner in the terminal."""
    print(f"\n{Fore.CYAN}==================================================")
    print(f"{Fore.CYAN}🔐  {Fore.WHITE}{Style.BRIGHT}PASSWORD STRENGTH ANALYZER{Fore.CYAN}  🔐")
    print(f"{Fore.CYAN}=================================================={Style.RESET_ALL}")
    print("Analyze your password strength and get helpful tips to secure it.\n")


def display_results(password, results):
    """Formats and prints the evaluation checklist, score, and suggestions."""
    checks = results["checks"]
    strength = results["strength"]
    suggestions = results["suggestions"]

    print(f"\n{Style.BRIGHT}--- Evaluation Report ---")
    
    # Print checklist with checkmarks [✓] or crosses [✗]
    def print_check_row(label, is_met, detail=""):
        icon = f"{Fore.GREEN}✓{Style.RESET_ALL}" if is_met else f"{Fore.RED}✗{Style.RESET_ALL}"
        detail_str = f" ({detail})" if detail else ""
        print(f"  [{icon}] {label}{detail_str}")

    print_check_row("Length is at least 8 characters", checks["length_8"], f"Current: {len(password)}")
    if checks["length_8"]:
        print_check_row("Length is at least 12 characters (Bonus)", checks["length_12"], f"Current: {len(password)}")
    print_check_row("Contains uppercase letters (A-Z)", checks["has_upper"])
    print_check_row("Contains lowercase letters (a-z)", checks["has_lower"])
    print_check_row("Contains numbers (0-9)", checks["has_digit"])
    print_check_row("Contains special characters (e.g., !, @, #)", checks["has_special"])

    print("\n-------------------------")
    
    # Color-coded strength badge
    if strength == "Strong":
        badge = f"{Fore.GREEN}{Style.BRIGHT}[ STRONG ]{Style.RESET_ALL}"
        color_msg = f"{Fore.GREEN}Excellent! Your password is secure.{Style.RESET_ALL}"
    elif strength == "Medium":
        badge = f"{Fore.YELLOW}{Style.BRIGHT}[ MEDIUM ]{Style.RESET_ALL}"
        color_msg = f"{Fore.YELLOW}Good, but it can be made even stronger.{Style.RESET_ALL}"
    else:
        badge = f"{Fore.RED}{Style.BRIGHT}[ WEAK ]{Style.RESET_ALL}"
        color_msg = f"{Fore.RED}Warning: This password is weak and vulnerable!{Style.RESET_ALL}"

    print(f"Overall Strength: {badge}")
    print(f"Security Rating:  {color_msg}")
    print("-------------------------")

    # Display suggestions if there are any
    if suggestions:
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}Suggestions to improve your password:{Style.RESET_ALL}")
        for suggestion in suggestions:
            print(f"  • {suggestion}")
    else:
        print(f"\n{Fore.GREEN}✨ Outstanding! No further improvements needed.{Style.RESET_ALL}")
        
    print("\n" + "=" * 50 + "\n")


def main():
    """Main program execution loop."""
    print_header()
    
    while True:
        try:
            # Prompt the user for input
            # We strip whitespace but keep the characters intact
            user_input = input(f"{Fore.GREEN}Enter a password to analyze (or type 'exit' to quit): {Style.RESET_ALL}")
            
            # Check for quit command
            if user_input.strip().lower() == 'exit':
                print(f"\n{Fore.CYAN}Thank you for using Password Strength Analyzer. Stay safe online!{Style.RESET_ALL}")
                break
                
            # Handle empty inputs gracefully
            if not user_input:
                print(f"{Fore.RED}Password cannot be empty. Please try again.{Style.RESET_ALL}\n")
                continue
                
            # Perform evaluation and print results
            results = check_password_strength(user_input)
            display_results(user_input, results)
            
        except (KeyboardInterrupt, SystemExit):
            # Graceful exit on Ctrl+C or terminal close signals
            print(f"\n\n{Fore.CYAN}Exiting... Stay secure!{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}\n")


if __name__ == "__main__":
    main()
