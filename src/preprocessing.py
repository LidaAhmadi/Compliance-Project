#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import re


# In[2]:


def clean_html(raw_html):
    """
    Remove HTML tags from a raw ruling while preserving line breaks.

    Parameters:
        raw_html (str): The raw HTML string from a ruling.

    Returns:
        str: Cleaned text with HTML tags removed and logical breaks preserved.
    """
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text(separator="\n").strip()


# In[3]:


def extract_decision_section(ruling_text):
    """
    Extract the main decision (opinion) section from a court ruling.

    This function searches for common structural markers like "DECISION & ORDER",
    or fallback patterns such as "APPEAL..." or "Judgment..." to find the start
    of the decision. It then identifies the likely end based on judge signatures 
    or closing phrases.

    Parameters:
        ruling_text (str): Full cleaned text of a court ruling.

    Returns:
        str or None: Extracted decision section, or None if no section is found.
    """
    if not ruling_text or not isinstance(ruling_text, str):
        return None

    # Normalize line breaks and remove empty lines
    lines = ruling_text.strip().splitlines()
    clean_lines = [line.strip() for line in lines if line.strip()]
    
    # --- Step 1: Identify start of decision text ---
    start_idx = None
    for i, line in enumerate(clean_lines):
        if "DECISION & ORDER" in line.upper():
            start_idx = i + 1
            break
    if start_idx is None:
        for i, line in enumerate(clean_lines):
            if line.upper().startswith("APPEAL") or line.lower().startswith("judgment"):
                start_idx = i
                break
    if start_idx is None:
        return None

    # --- Step 2: Identify end of decision text ---
    end_idx = len(clean_lines)
    for i in range(start_idx, len(clean_lines)):
        line = clean_lines[i]
        if ("J.P." in line or "JJ." in line or 
            "THIS CONSTITUTES" in line.upper() or 
            "ENTERED:" in line.upper()):
            end_idx = i
            break

    # --- Step 3: Return joined block ---
    return "\n".join(clean_lines[start_idx:end_idx]).strip()


# In[4]:


def clean_decision_text(text):
    """
    Light cleaning for legal decision sections, suitable for semantic search and LLM tasks.
    - Preserves legal citations and structure
    - Removes editorial footnotes like [*1]
    - Flattens formatting without damaging semantic content
    """
    
    # Remove editorial markers such as [*1], [*2], which do not carry semantic meaningimport re

def clean_and_format_decision(text):
    """
    Clean and lightly format a legal decision text for downstream NLP tasks.
    - Removes editorial noise
    - Preserves legal citations
    - Adds paragraph breaks at key transitions
    """

    # --- CLEANING ---

    # Remove editorial markers like [*1], [*2]
    text = re.sub(r'\[\*\d+\]', '', text)

    # Replace multiple blank lines with a double newline
    text = re.sub(r'\n\s*\n+', '\n\n', text)

    # Replace remaining newlines with spaces to flatten paragraph content
    text = re.sub(r'\n+', ' ', text)

    # Normalize extra spaces
    text = re.sub(r'\s{2,}', ' ', text)

    # Strip leading/trailing whitespace
    text = text.strip()


    # --- FORMATTING FOR DISPLAY ---

    # Add paragraph breaks after key legal transitions
    break_phrases = [
        r'(ORDERED that.*?)', 
        r'(Here,.*?)',
        r'(Accordingly,.*?)',
        r'(The defendant appeals\.)',
        r'(The defendant contends that.*?)'
    ]
    for pattern in break_phrases:
        text = re.sub(pattern, r'\n\n\1', text, flags=re.IGNORECASE)

    return text

    text = re.sub(r'\[\*\d+\]', '', text)

    # Replace multiple blank lines with a double newline (preserves paragraph boundaries)
    text = re.sub(r'\n\s*\n+', '\n\n', text)
    
    # Replace remaining line breaks with space to join wrapped sentences into full paragraphs
    text = re.sub(r'\n+', ' ', text)

    # Replace multiple spaces with a single space to normalize spacing
    text = re.sub(r'\s{2,}', ' ', text)

    # Remove leading and trailing whitespace
    return text.strip()


# In[5]:


def extract_party_block(text):
    """
    Extract party names using the [*1] marker and nearby lines.

    Parameters:
        text (str): Cleaned ruling text

    Returns:
        str: Combined party string in "A v B" format, or empty if not found
    """
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    
    for i, line in enumerate(lines):
        if '[*1]' in line:
            party1 = line.replace('[*1]', '').strip()
            # Look ahead to skip possible blank lines and capture "v" pattern
            if i + 2 < len(lines):
                party2 = lines[i + 2].strip()
                return f"{party1} v {party2}"
            break

    return ""


# In[6]:


def clean_party_line(party_line):
    """Remove common prefixes like 'In the Matter of' from party line."""
    return party_line.replace("In the Matter of ", "").strip()


# In[ ]:




