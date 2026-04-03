# Personal Assistant Agent (n8n + Streamlit)
## Overview
This project is a **Personal Assistant Agent** built using **n8n** for workflow orchestration and **Streamlit** for the user interface.  
It acts like a reliable executive assistant, capable of handling:

- Information lookup
- Calendar management
- Email reading and replying
- Task and to-do management
- Notes creation and updates
- Expense tracking and budgeting

The agent is powered by a structured **system prompt** (PRD‑style) and integrates with Google services (Calendar, Gmail, Docs, Tasks, Sheets).

---

## Features
- 💬 **Chat Interface**: Streamlit app (`App.py`) provides a conversational UI.
- 🔗 **Workflow Orchestration**: n8n handles tool execution via webhooks.
- 📅 **Calendar Management**: Create, fetch, and manage events.
- 📧 **Email Management**: Read, summarize, and reply to Gmail messages.
- ✅ **Task Management**: Create, fetch, and delete tasks.
- 📝 **Notes Management**: Create and update notes in Google Docs.
- 💰 **Expense Tracking**: Add expenses and calculate budgets in Google Sheets.
- 🌐 **Information Lookup**: Use web search when internal knowledge is insufficient.

