# Aspyre AI – MVP

Aspyre AI is an education platform that helps **teachers** generate lessons and quizzes with AI and gives **students** a simple, adaptive way to learn from that content.

This repo contains the **MVP version** of Aspyre AI: a dual-portal web app with basic AI-powered features that will grow into the full Aspyre EDU platform over time.

---

## 🎯 Goal of the MVP

Build a working product that shows:

- Teachers can quickly **create and manage AI-generated lessons and quizzes**
- Students can **view assigned lessons, take quizzes, and ask an AI tutor questions**
- The system can support both sides (teacher + student) with a clean, realistic architecture

This MVP is meant to be:
- A **learning project** (for me as a developer),
- A **real demo** for pilots (Boys & Girls Club, schools, etc.),
- A **foundation** for future features like deployable AI tutors and advanced analytics.

---

## ✨ Core Features (MVP)

### 🧑‍🏫 Teacher Portal – “Aspyre for Educators”

- Sign up / log in as a **teacher**
- Simple **dashboard** showing “My Lessons”
- **Create lesson from prompt**  
  - Enter a topic + grade level  
  - Backend uses AI to generate a structured lesson
- **Create lesson from upload** (planned MVP feature)  
  - Upload a file (PDF/slides/text)  
  - Backend extracts text & generates a lesson
- **Generate quizzes** from a lesson  
  - Auto-creates basic multiple-choice questions
- Assign lessons/quizzes to students (class or via code)
- View basic stats: how many students viewed/completed a lesson

---

### 👩‍🎓 Student Portal – “Aspyre for Learners”

- Sign up / log in as a **student**
- Join a teacher/class (e.g., using a code)
- **View assigned lessons**
- **Take quizzes** and see instant scores + correct answers
- **Ask questions to a basic AI tutor**  
  - Under each lesson, students can type questions  
  - AI responds using the lesson content as context

---

### 🤖 AI Features (MVP Level)

- **Lesson Generator**  
  - Input: topic or extracted text  
  - Output: structured explanations, sections, and examples
- **Quiz Generator**  
  - Input: lesson text  
  - Output: 3–5 multiple-choice questions with correct answers
- **Basic AI Tutor (Q&A Chat)**  
  - Input: student question + lesson context  
  - Output: clear, step-by-step explanation

This is a **simplified version** of the future “teacher-deployed AI tutors” system.

---

## 🧱 Tech Stack

**Frontend**
- [Next.js](https://nextjs.org/) (React)
- TypeScript (later, optional)
- Tailwind CSS + basic component library (e.g., shadcn/ui)

**Backend**
- [FastAPI](https://fastapi.tiangolo.com/) (Python)
- Uvicorn (ASGI server)

**Database & Auth**
- PostgreSQL (via Supabase / Neon / Railway)
- Role-based auth: `teacher` and `student`

**AI Integration**
- OpenAI API (for lessons, quizzes, and tutor responses)

**Hosting (Planned)**
- Frontend: Vercel
- Backend: Render / Railway
- Database: Supabase / Neon

---

## 🏗️ High-Level Architecture

```text
           ┌────────────────────┐
           │    Teacher UI      │
           │ (Next.js frontend) │
           └────────┬───────────┘
                    │
                    │  HTTPS (REST API)
                    ▼
            ┌────────────────────┐
            │   FastAPI Backend  │
            ├────────────────────┤
            │ Auth & Roles       │
            │ Lesson & Quiz APIs │
            │ Tutor Q&A API      │
            └────────┬───────────┘
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
┌──────────────┐        ┌────────────────┐
│ PostgreSQL   │        │ OpenAI API     │
│ (users,      │        │ (AI generation │
│ lessons,     │        │  & tutoring)   │
│ quizzes, etc)│        └────────────────┘
└──────────────┘

           ┌────────────────────┐
           │   Student UI       │
           │ (Next.js frontend) │
           └────────────────────┘
