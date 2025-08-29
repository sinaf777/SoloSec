
# ✅ 2-Week Cybersecurity Learning Platform Roadmap (Django-Based)

## 🛠️ Tech Stack (All Free)
- **Backend** → Django (Python)  
- **Frontend** → Django Templates + Tailwind CSS (via Django-Tailwind or CDN)  
- **Database** → SQLite (dev) → PostgreSQL (production, free on Render/Railway)  
- **Authentication** → Django built-in `auth` system (extended user model)  
- **Deployment** → Render (free tier) or Railway (free tier)  
- **Version Control** → GitHub (to connect with Render)  
- **Styling/UI** → Tailwind CSS + DaisyUI (components, e.g. buttons, cards)  

---

# 📅 Timeline with Checkboxes

## 🔹 Week 1 – Core Platform (MVP)

### Day 1–2 → Setup & User System
- [ ] Install **Django** (`django-admin startproject platform`)  
- [ ] Create apps: `users`, `rooms`, `challenges`  
- [ ] Configure **Tailwind CSS** (or use CDN for simplicity)  
- [ ] Extend Django `User` model → add `score` field (IntegerField default=0)  
- [ ] Create **register, login, logout** views + templates  
- [ ] Profile page → show username, score, solved challenges  

**Deliverable:** Users can register/login/logout, have a profile with score.  

---

### Day 3–4 → Challenges
- [ ] Create **Challenge model**:  
  - `title`  
  - `category` (Web, Crypto, etc.)  
  - `difficulty` (Easy, Medium, Hard)  
  - `description`  
  - `points`  
  - `flag`  
- [ ] Create **Challenge list page**  
- [ ] Challenge detail page with submission form  
- [ ] Backend checks `flag`: award points if correct  
- [ ] Update user’s score + solved list  

**Deliverable:** Users can solve challenges by submitting flags → score updates.  

---

### Day 5 → Rooms (Courses)
- [ ] Create **Room model**:  
  - `title`  
  - `description`  
  - `content` (Markdown)  
  - `difficulty`  
  - `points`  
- [ ] Connect Rooms ↔ Challenges (ManyToMany)  
- [ ] Room list page  
- [ ] Room detail page (content + linked challenges)  

**Deliverable:** Rooms act as guided courses.  

---

### Day 6 → Leaderboard
- [ ] Create **Leaderboard view** → order users by score  
- [ ] Template: show rank, username, score  
- [ ] Add link in navbar  

**Deliverable:** Users see global rankings.  

---

### Day 7 → Polish & Test
- [ ] Test registration → solving challenge → leaderboard update  
- [ ] Add challenges and rooms in admin panel  
- [ ] Apply Tailwind CSS for base styling  

**Deliverable:** MVP ready — like a mini TryHackMe.  

---

## 🔹 Week 2 – Gamification, Polish & Deployment

### Day 8–9 → Progress Tracking & Scoring
- [ ] Extend profile → show list of solved challenges  
- [ ] Add difficulty-based scoring: Easy=10, Medium=20, Hard=30  
- [ ] Add badges system (optional)  

**Deliverable:** User progress feels gamified.  

---

### Day 10 → Room Flow
- [ ] Add navigation inside rooms (Prev/Next buttons)  
- [ ] Progress bar (percentage of challenges solved)  

**Deliverable:** Rooms feel like TryHackMe walkthroughs.  

---

### Day 11 → UI Polish
- [ ] Install **DaisyUI**  
- [ ] Redesign with components: navbar, cards, progress bars, tables  

**Deliverable:** Platform looks clean and modern.  

---

### Day 12 → Deployment
- [ ] Create GitHub repo → push project  
- [ ] Setup **Postgres DB** on Render/Railway  
- [ ] Deploy Django app on Render  
- [ ] Configure static files (Whitenoise or S3 if needed)  
- [ ] Setup free domain (Render subdomain or Freenom)  

**Deliverable:** Publicly accessible platform.  

---

### Day 13 → Final Testing
- [ ] Register multiple accounts  
- [ ] Test leaderboard accuracy  
- [ ] Test progress tracking  
- [ ] Ensure flags are secure (not exposed in source)  

**Deliverable:** Stable, production-ready MVP.  

---

### Day 14 → Launch 🚀
- [ ] Add 5 Rooms (guides)  
- [ ] Add 10–15 Challenges (Web, Crypto, Forensics)  
- [ ] Share with testers  
- [ ] Gather feedback  

**Deliverable:** Beta launch 🎉  

---

# 📦 Final Scope in 2 Weeks
- ✅ User auth & profiles  
- ✅ Challenges (flag submission, scoring)  
- ✅ Rooms (courses linked to challenges)  
- ✅ Leaderboard  
- ✅ Progress tracking  
- ✅ Deployed online for free  