# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1. Dropdown for Developer Debug was viewable for players

2. After you win, you can't start a new game, even when you press "New Game"

3. Starting new game ignores selected difficulty range. New Game handler always uses a range of 1-100.

4. The Normal difficulty has a larger range than Hard

5. The default difficulty is "Hard"
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code to help me debug issues with the code and refactor the logic. I was also having a lot of problems with setup, so I also used to work those issues too.
One issue it suggested to fix was how New Game button hardcoded the difficulty, without taking into account the selected difficulty.
I didn't actually think it gave me any wrong suggestions. I gave as much context I could (e.g. the README to prevent Claude Code from hallucinating)
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

To test whether the bug was really fixed to verify directly with the app and also the pytest module.
I ran the 
When I ran the tests, it helped me realize that the output format of the tests was of the test was causing all the tests to fail.
## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time the user interacts with the Streamlit app, the session state would reset by rerunning the entire script. This would also cause it to regenerate the secret number.
Its basically like a page refreshing every single time you press a button on the webpage.
I guarded the secret number with an if statement that checks whether or not the secret number is in session state. If not, it will regenerate.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I will take forward is to always read through what the agent worked on and to always ask questions so that I personally understand. Never outsource my understanding.
Whenever I prompt, I will use plan mode to collaborate on a solution before executing the fix.
This project helped see AI, especially coding agents as not only a research assistant but also a partner in the process of coding.

