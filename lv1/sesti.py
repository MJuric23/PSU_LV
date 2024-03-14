ham_messages = []
spam_messages = []

with open("SMSSpamCollection.txt", "r", encoding="utf-8") as file: //utf 8 podrzava sirok spektar znakova i simbola za citanje
    for line in file:
        label, message = line.strip().split('\t')
        if label == 'ham':
            ham_messages.append(message)
        elif label == 'spam':
            spam_messages.append(message)


total_ham_words = sum(len(message.split()) for message in ham_messages)
total_spam_words = sum(len(message.split()) for message in spam_messages)

avg_ham_word_count = total_ham_words / len(ham_messages)
avg_spam_word_count = total_spam_words / len(spam_messages)

print("Prosječan broj riječi u ham porukama:", avg_ham_word_count)
print("Prosječan broj riječi u spam porukama:", avg_spam_word_count)


spam_exclamation_count = sum(message.endswith('!') for message in spam_messages)
print("Broj spam poruka koje završavaju uskličnikom:", spam_exclamation_count)
