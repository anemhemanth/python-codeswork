messages = [
    "lewis: Good morning everyone!",
    "verstappen: Morning Lewis! Ready for today’s webinar?",
    "Charles: Morning! I’ve been reviewing my resume all night.",
    "lewis: That’s great! Hope you all land amazing roles soon.",
    "verstappen: You too, Charles! Let’s keep pushing.",
    "Charles: We should plan a mock interview session this weekend.",
    "lewis: Are we connecting today for the LinkedIn workshop?",
    "verstappen: Yes, it starts at 5 PM.",
    "Charles: Perfect, I’ve registered already.",
    "lewis: This message was deleted",
    "verstappen: What should I prepare for the mock interview?",
    "Charles: Brush up on behavioral questions and STAR format.",
    "lewis: Got it! I’ll also revise my project highlights.",
    "verstappen: Awesome!",
    "Charles: This message was deleted",
    "lewis: Who else is joining the session?",
    "verstappen: I think Dave and Emma confirmed.",
    "Charles: Great! More perspectives will help.",
    "lewis: Let’s finalize the agenda and share resources."
]
total_messages = 0
users = []
word_count = 0
longest_msg = ""
user_msg_count = []
user_words = []
questions = []
deleted_count = 0
unique_msgs = []
mention_count = 0

for msg in messages:
    total_messages += 1
    colon_pos = -1
    for i in range(len(msg)):
        if msg[i] == ":":
            colon_pos = i
            break

    user = msg[:colon_pos]
    content = msg[colon_pos+2:]
    found = False
    for u in users:
        if u == user:
            found = True
            break
    if not found:
        users += [user]
        user_msg_count += [0]
        user_words += [[]]

    for i in range(len(users)):
        if users[i] == user:
            user_msg_count[i] += 1
            word = ""
            for ch in content + " ":
                if ch != " ":
                    word += ch
                else:
                    user_words[i] += [word.lower()]
                    word_count += 1
                    word = ""
            break

    if len(content) > len(longest_msg):
        longest_msg = msg

    if "?" in content:
        questions += [msg]

    if content == "This message was deleted":
        deleted_count += 1

    is_duplicate = False
    for m in unique_msgs:
        if m == msg:
            is_duplicate = True
            break
    if not is_duplicate:
        unique_msgs += [msg]

print("1. Total messages:", total_messages)
print("2. Unique users:", users)
print("3. Total words:", word_count)
print("4. Average words per message:", round(word_count / total_messages, 2))
print("5. Longest message:", longest_msg)
max_count = 0
max_user = ""
for i in range(len(users)):
    if user_msg_count[i] > max_count:
        max_count = user_msg_count[i]
        max_user = users[i]
print("6. Most active user:", max_user, "(", max_count, "messages )")

for i in range(len(users)):
    if users[i] == "verstappen":
        print("7. Messages sent by verstappen:", user_msg_count[i])

charles_index = -1
for i in range(len(users)):
    if users[i] == "Charles":
        charles_index = i
        break

word_freq = []
word_list = []
for w in user_words[charles_index]:
    found = False
    for i in range(len(word_list)):
        if word_list[i] == w:
            word_freq[i] += 1
            found = True
            break
    if not found:
        word_list += [w]
        word_freq += [1]

max_freq = 0
common_word = ""
for i in range(len(word_list)):
    if word_freq[i] > max_freq:
        max_freq = word_freq[i]
        common_word = word_list[i]
print("Most frequent word used by Charles:", '"' + common_word + '"')

first = ""
last = ""
found = False
for msg in messages:
    if msg.startswith("lewis:"):
        if not found:
            first = msg
            found = True
        last = msg
print("First message by lewis:", first)
print("   Last message by lewis:", last)


found_dave = False
for u in users:
    if u == "Dave":
        found_dave = True
        break
if not found_dave:
    print("User 'Dave' not found in the chat.")

all_words = []
word_freq = []
for uw in user_words:
    for w in uw:
        found = False
        for i in range(len(all_words)):
            if all_words[i] == w:
                word_freq[i] += 1
                found = True
                break
        if not found:
            all_words += [w]
            word_freq += [1]

repeated = []
for i in range(len(all_words)):
    if word_freq[i] > 1:
        repeated += [all_words[i]]
print("Common repeated words:", repeated)

max_avg = 0
max_user = ""
for i in range(len(users)):
    avg = len(user_words[i]) / user_msg_count[i]
    if avg > max_avg:
        max_avg = avg
        max_user = users[i]
print("User with longest average message:", max_user, "(avg", round(max_avg, 2), "words)")

mention_count = 0
for msg in messages:
    if "lewis" in msg and not msg.startswith("lewis:"):
        mention_count += 1
print("Messages mentioning 'lewis':", mention_count)
print("Unique messages count:", len(unique_msgs))

sorted_msgs = unique_msgs[:]
for i in range(len(sorted_msgs)):
    for j in range(i+1, len(sorted_msgs)):
        if sorted_msgs[i] > sorted_msgs[j]:
            temp = sorted_msgs[i]
            sorted_msgs[i] = sorted_msgs[j]
            sorted_msgs[j] = temp
print("Sorted messages:")
for msg in sorted_msgs:
    print(msg)

print("Questions asked:")
for q in questions:
    print(q)

reply_count = 0
for i in range(1, len(messages)):
    if messages[i].startswith("verstappen:") and messages[i-1].startswith("lewis:"):
        reply_count += 1
print("Reply ratio from verstappen to lewis:", reply_count, "replies")
print("Deleted messages found:", deleted_count)