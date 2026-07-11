![Python](https://img.shields.io/badge/Python-3.11-blue)
![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-orange)
![Google GenAI SDK](https://img.shields.io/badge/Google-GenAI%20SDK-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

# 🤖 AI Coding Agent

> **A beginner-friendly AI coding assistant that leverages Gemini Tool Calling to reason about code, interact with project files, execute Python programs, and autonomously perform coding tasks through specialized tools.**

---

## 📖 Overview

Modern AI coding assistants can generate impressive code, but understanding **how they actually work under the hood** is a completely different challenge.

This project was built to explore the fundamentals of **Agentic AI** by implementing a coding agent capable of interacting directly with a local project. Rather than simply responding with text, the agent follows an iterative workflow where it reasons about the user's request, selects appropriate tools, performs actions, and synthesizes the results into a final response.

The primary objective of this project was not to build the smartest coding assistant, but to understand the architecture behind modern AI agents—including **System Prompts**, **Tool Calling**, **Tool Schemas**, **conversation history**, and **modular agent workflows**.

---

## ✨ Key Features

The agent can autonomously:

- 📂 Inspect project files and directories
- 🌳 Explore project hierarchy using a recursive directory tree
- 📖 Read source code files
- ✍️ Create and modify files
- ▶️ Execute Python programs
- 🧠 Perform multi-step reasoning using Gemini Tool Calling
- ✅ Validate code changes by executing the updated project

---

## 💡 Why Not Just Use ChatGPT?

Unlike a conventional chatbot, this agent interacts directly with a project's working directory.

Instead of manually:

- Copying source code
- Running programs
- Testing changes
- Pasting error messages back into a chat

the agent performs these tasks autonomously using specialized tools, allowing it to inspect, modify, and validate projects with minimal manual intervention.

This project focuses on demonstrating **how AI agents combine reasoning with external tools**, rather than simply generating code.

---

## 🚀 Custom Improvement

After completing the original implementation, I wanted to contribute something beyond the tutorial.

While testing the agent, I noticed that understanding a project's hierarchy was often the first step before identifying relevant files. Repeatedly listing individual directories was inefficient and only provided a local view of the project.

To address this, I designed and implemented a **Recursive Directory Tree Tool** that generates a structured view of the agent's working directory.

Instead of navigating folders one by one, the agent can first visualize the project's hierarchy, enabling it to understand unfamiliar codebases more efficiently before deciding which files to inspect or modify.

Although the feature itself is relatively small, it demonstrates how extending an agent with carefully designed tools can significantly improve its reasoning workflow and project navigation.

---

## 📚 What I Learned

Building this project helped me understand several core concepts behind modern AI agents, including:

- 🧠 Designing effective **System Prompts**
- 🔧 Implementing **Tool Calling** and **Tool Schemas**
- 🗂️ Managing conversation history across multiple reasoning steps
- 🏗️ Building modular, maintainable Python applications
- 🔁 Applying recursion to solve real-world navigation problems
- ⚙️ Working with Python's `subprocess` module
- 🤖 Understanding how LLMs interact with external tools instead of relying solely on generated text
- 📉 Appreciating the impact of API quotas during iterative development

---

## 🗺️ Roadmap

Planned improvements include:

- [ ] Replace Gemini with a local LLM using Ollama
- [ ] Add support for safe terminal command execution with user approval
- [ ] Expand the available toolset for software engineering tasks
- [ ] Build a React-based graphical interface
- [ ] Explore multi-agent workflows for more advanced task planning

---

## 🙏 Acknowledgements

This project was inspired by the excellent collaboration tutorial by **freeCodeCamp** and **Boot.dev**.

The tutorial provided a strong foundation for understanding AI coding agents, while this implementation served as an opportunity to explore the underlying architecture, experiment with additional features, and deepen my understanding of Agentic AI.
