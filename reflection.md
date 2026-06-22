# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
At the first run the game seemed fine. I input my guesses and it kept giving me hints. Once the answer was revealed is when I noticed that there were issues.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  Hints kept saying to go lower even though the answer was higher.
  The "new game" button would not start a new game

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|guessed 1|"Go Higher" or "Correct Answer"|"Go Lower"|"none"|
|pressed "new game"|Game is restarted and I can play again|Does not work| "none"|
|changed difficulty|Change the range|Range is not correct or out of bounds|"none"|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI wanted to make sure we compared ints when checking to see if the secret is higher and lower. I verified it by reading the code then doing a pytest.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
For the 2 that I did I did not encounter a wrong suggestion. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
once test passed I went to launch the site and play the game myself trying to find the same bugs.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I was trying to break the game by guessing out of bounds. I guessed 1000 and it say to go lower which is great because I do need to go lower but AI and I did not count for edge cases like out of bounds.
- Did AI help you design or understand any tests? How?
The AI helped me understand that it can miss stuff like edge cases. I tested it out myself and had to find out the hard way.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
