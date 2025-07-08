# --- Libraries ---
from bs4 import BeautifulSoup
import re

# --- HTML Cleaning ---
def clean_html(raw_html):
    """
    Remove HTML tags from a raw string while preserving line breaks.

    Parameters:
        raw_html (str): The raw HTML string from a ruling.

    Returns:
        str: Cleaned text with HTML tags removed.
    """
    if not raw_html or not isinstance(raw_html, str):
        return ""
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text(separator="\n").strip()

# --- Core Text Extraction & Cleaning ---
def extract_decision_section(ruling_text):
    """
    Extract the main decision section from a court ruling using heuristics.

    Parameters:
        ruling_text (str): Full cleaned text of a court ruling.

    Returns:
        str or None: Extracted decision section, or None if no section is found.
    """
    if not ruling_text or not isinstance(ruling_text, str):
        return None

    lines = [line.strip() for line in ruling_text.strip().splitlines() if line.strip()]
    
    start_idx = None
    # Find start marker using a list of patterns
    start_patterns = ["decision & order"]
    fallback_patterns = ["appeal", "judgment", "in an action"]

    for i, line in enumerate(lines):
        if any(p in line.lower() for p in start_patterns):
            start_idx = i + 1
            break
    if start_idx is None:
        for i, line in enumerate(lines):
            if any(line.lower().startswith(p) for p in fallback_patterns):
                start_idx = i
                break
    if start_idx is None:
        return None

    # Find end marker
    end_idx = len(lines)
    end_patterns = ["j.p.", "jj.", "this constitutes", "entered:"]
    for i in range(start_idx, len(lines)):
        line = lines[i]
        if any(p in line.lower() for p in end_patterns):
            end_idx = i
            break
            
    return "\n".join(lines[start_idx:end_idx]).strip()

def clean_and_format_decision(text):
    """
    A single, robust function to clean and format decision text.
    Removes editorial noise and adds paragraph breaks for readability.

    Parameters:
        text (str): The text to be cleaned.

    Returns:
        str: The processed text.
    """
    if not text:
        return ""

    # Basic cleaning: remove editorial markers like [*1]
    text = re.sub(r'\[\*\d+\]', '', text)
    
    # Flatten the text by replacing all newlines and multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text).strip()

    # Add paragraph breaks after key legal transitions for readability
    # The (.*?) part is a non-greedy capture of everything until the next pattern or end of string.
    break_phrases = [
        r'(ORDERED that.*?)',
        r'(Here,.*?)',
        r'(Accordingly,.*?)',
        r'(The defendant appeals\.)',
        r'(The defendant contends that.*?)'
    ]
    for pattern in break_phrases:
        # Use re.sub with a function to handle matches and add newlines
        text = re.sub(pattern, lambda m: '\n\n' + m.group(1).strip(), text, flags=re.IGNORECASE)

    return text.strip()


# --- Party Information Extraction & Cleaning ---
def extract_party_block(text):
    """
    Extracts party names using the [*1] marker as an anchor.
    Stops when it encounters common counsel/address patterns or a major heading.

    Parameters:
        text (str): Cleaned ruling text.

    Returns:
        str: Combined party string, or empty if not found.
    """
    if not text:
        return ""

    # Find the block of text starting from [*1]
    # We use re.DOTALL so that '.' matches newlines
    match = re.search(r'\[\*1\](.*)', text, re.DOTALL | re.IGNORECASE)
    if not match:
        return ""

    potential_party_text = match.group(1)
    lines = [line.strip() for line in potential_party_text.splitlines() if line.strip()]

    party_lines = []
    # Loop through the lines and collect them until we hit a stop word
    for line in lines:
        line_lower = line.lower()
        
        # Define the "stop signs" that indicate the party block has ended
        if ("of counsel" in line_lower or 
            "decided and entered:" in line_lower or 
            "decision & order" in line_lower):
            break
            
        party_lines.append(line)

    # Join the collected lines and clean up any extra whitespace
    return " ".join(party_lines).strip()
        
def clean_party_line(party_line):
    """Remove common prefixes like 'In the Matter of' from party line."""
    if not party_line:
        return ""
    # Use regex to remove the prefix and any extra whitespace at the start
    return re.sub(r'^\s*in the matter of\s*', '', party_line, flags=re.IGNORECASE).strip()
