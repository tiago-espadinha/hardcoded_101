"""
CLI: Word Count Tool.
Features: reads a text file, outputs total words, unique words, top 10 most frequent,
          average word length, longest word, number of sentences.
"""
import sys
import re
from collections import Counter
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <filename>")
        return

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: {file_path} not found")
        return

    text = file_path.read_text()
    
    # Simple split for words
    words = re.findall(r"\b\w+\b", text.lower())
    sentences = re.split(r"[.!?]+", text)
    sentences = [s for s in sentences if s.strip()]

    if not words:
        print("No words found in file.")
        return

    total_words = len(words)
    unique_words = len(set(words))
    word_counts = Counter(words)
    avg_len = sum(len(w) for w in words) / total_words
    longest_word = max(words, key=len)

    print(f"File: {file_path.name}")
    print("-" * 20)
    print(f"Total words:     {total_words}")
    print(f"Unique words:    {unique_words}")
    print(f"Sentences:       {len(sentences)}")
    print(f"Average length:  {avg_len:.2f}")
    print(f"Longest word:    '{longest_word}' ({len(longest_word)})")
    print("\nTop 10 Most Frequent:")
    for word, count in word_counts.most_common(10):
        print(f"  {word}: {count}")

if __name__ == "__main__":
    main()
