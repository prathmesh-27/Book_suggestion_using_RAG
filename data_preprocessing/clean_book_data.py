import re
import pandas as pd

def extract_year(date_str):
    """Extracts the year from a date or returns empty None if not found."""
    if not isinstance(date_str, str):
        return None  # or pd.NA

    # Search for 4-digit year
    match = re.search(r"\b(\d{4})\b", date_str)
    return int(match.group(1)) if match else None


def extract_genre_set(raw_str):
    """Extracts genre names only, removing code prefixes"""
    if not isinstance(raw_str, str):
        return set()
    
    # Remove braces and split entries
    items = raw_str.strip('{}').split(',')
    # print(items)

    genres = []
    for item in items:
        parts = item.strip().split(' ', 1)
        if len(parts) == 2:
            genre = parts[1].strip().lower()
            # Decode unicode escapes like u00e0 → à
            genre = bytes(genre, 'utf-8').decode('unicode_escape')
            genres.append(genre)
    
    return set(genres)

def parse_text_file(filepath):
    """Reads and parses the raw book text file into structured records."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read().strip()

    entries = re.split(r"\n(?=\d+\t)", text)

    data = []

    for entry in entries:
        lines = entry.strip().split('\t')
        
        fields = []
        
        for line in lines:
            line = line.strip()
            if line != "":
                fields.append(line)

        if len(fields) < 5:
            continue  # Skip invalid

        try:
            book_id = fields[0]
            title = fields[2]
            author = fields[3]
            publish_year = extract_year(fields[4]) if len(fields) > 4 else ""
            genres = extract_genre_set(lines[5]) if len(lines) > 5 and lines[5].startswith("{") else ""


            summary_start_index = 6 if genres else 5 if publish_year else 4
            summary = "\t".join(lines[summary_start_index:]).replace('\n', ' ').strip()

            data.append({
                "id": book_id,
                "title": title,
                "author": author,
                "publish_year": publish_year,
                "genres": ', '.join(genres),
                "summary": summary.strip()
            })
        except Exception as e:
            print(f"Error parsing entry: {fields}\n{e}")
            continue

    return pd.DataFrame(data)

def save_to_csv(df, output_path):
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"CSV file saved to: {output_path}")
    
if __name__ == "__main__":
    INPUT_FILE = "dataset/booksummaries.txt"         # change this to your filename
    OUTPUT_FILE = "dataset/book_summary.csv"

    df = parse_text_file(INPUT_FILE)
    save_to_csv(df, OUTPUT_FILE)