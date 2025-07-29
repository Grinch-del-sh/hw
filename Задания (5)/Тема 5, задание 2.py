word = "programming"
vowels = {'a', 'e', 'i', 'o', 'u'}
vowel_count = 0
consonant_count = 0
vowel_stats = {v:0 for v in vowels}

for letter in word:
    if letter in vowels:
        vowel_count += 1
        vowel_stats[letter] += 1
    else:
        consonant_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")

for v in sorted(vowel_stats):
    print(f"{v}: {vowel_stats[v] if vowel_stats[v] > 0 else False}")