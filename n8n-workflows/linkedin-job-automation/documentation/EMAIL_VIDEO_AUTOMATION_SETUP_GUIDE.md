# 🚀 Email + Video Job Automation - Setup Guide
**Created:** October 30, 2025 - Day 4 Final System
**For:** Asheesh Ranjan Srivastava
**Goal:** Complete hands-free job automation with video resumes

---

## 📋 What You Need Before Starting

### **Already Completed:**
- ✅ LinkedIn Profile optimized for AI PM roles
- ✅ 10 LinkedIn Job Alerts set up (sending daily emails)
- ✅ Google Sheet created: "Asheesh Job Search 2026"
- ✅ OpenAI API key (from `.streamlit/secrets.toml`)
- ✅ HeyGen yearly subscription

### **Need to Complete:**
- [ ] Create HeyGen Avatar (one-time, 30 minutes)
- [ ] Get HeyGen API Key
- [ ] Get Avatar ID
- [ ] Import workflow to n8n
- [ ] Connect all credentials
- [ ] Test with sample jobs

---

## 🎬 STEP 1: Create Your HeyGen Avatar (CRITICAL FIRST!)

This is the MOST IMPORTANT step. Everything else is quick, but avatar creation takes time.

### **1A: Record Your Avatar Video**

**Go to:** https://app.heygen.com/

**Click:** "Avatars" → "Create Avatar" or "Instant Avatar"

**Recording Requirements:**
- **Length:** 2-3 minutes
- **Position:** Look directly at camera
- **Background:** Neutral, clean
- **Lighting:** Bright, even (no shadows on face)
- **Audio:** Clear (use headphones mic or external mic)
- **Orientation:** Landscape mode (16:9)
- **Clothing:** Professional (what you'd wear to interview)
- **Expression:** Neutral to slightly positive

### **1B: What to Say in Recording**

**Use this exact script (optimized for your profile):**

```
Hello, my name is Asheesh Ranjan Srivastava. I'm an AI product
builder with systems thinking and AI collaboration expertise.

I have six years of experience in data-driven program leadership,
where I've trained over four hundred professionals and led
cross-functional teams.

Currently, I'm building Quest and Crossfire, an AI-powered learning
platform. I've shipped production applications including a
multi-persona chatbot and an Obsidian AI assistant.

My technical skills include Python, OpenAI API, Hugging Face
Transformers, Streamlit, n8n automation, and Power BI.

I combine systems thinking with AI-native development to architect
products that help people learn and grow. My approach focuses on
vision, user needs, and architecture, while partnering with AI for
implementation.

I'm seeking AI Product Manager roles where I can build products that
create clarity from complexity. Thank you for considering my
application.

I have experience with data analysis and MIS design, having created
interactive dashboards and optimized workflows in previous roles.

At Piramal Foundation, I led a ten-member team and facilitated
training for program leaders across five states. This experience
taught me how to coordinate cross-functional teams and design
capacity-building systems.

My recent projects demonstrate my AI-native approach. The multi-model
text summarization system achieved eighty-three percent cost reduction
through intelligent caching. The multi-persona chatbot features real-time
streaming and personality switching.

I'm currently completing my Master of Science in Computer Science with
focus on AI and Machine Learning at Woolf University, alongside the
OutSkill AI Engineering Bootcamp.

My philosophy is captured in Quest and Crossfire's tagline: "Small
fixes, big clarity." I believe in building evolving systems that turn
chaos into progress.

I'm available from January twenty twenty-six for remote-first or
hybrid roles, with openness to relocation for the right opportunity.

Thank you for your time and consideration. I look forward to discussing
how I can contribute to your team.
```

**Tips:**
- Speak naturally, don't rush
- Pause slightly between paragraphs
- Smile occasionally
- Make eye contact with camera
- Practice once before recording

### **1C: Upload and Wait**

1. Upload video to HeyGen
2. **Processing time:** 15-30 minutes
3. You'll get email when ready
4. Meanwhile, continue with Steps 2-3 below!

---

## 🔑 STEP 2: Get HeyGen Credentials

### **2A: Get API Key**

**While avatar processes:**
1. In HeyGen dashboard: https://app.heygen.com/
2. Click **"Settings"** (gear icon)
3. Click **"API"** tab
4. Click **"Generate API Key"** or **"Create API Key"**
5. **Copy the key** (starts with something like `hg_...`)
6. **Save it securely** - you'll need this for n8n!

### **2B: Get Avatar ID**

**Once avatar is created:**
1. Go to **"Avatars"** section
2. Click on your newly created avatar
3. Look for **"Avatar ID"** in the details
4. OR copy from URL (example: `avatar_abc123xyz`)
5. **Save this ID** - you'll need it for workflow!

---

## 📊 STEP 3: Update Google Sheet

Your sheet needs 2 new columns for video automation.

**Sheet ID:** `1xMELeUYUcGrqctnCQSWOuB586k1NHth0mgLhUVRu6EI`

### **Option A: Manual Update**
1. Open sheet: https://docs.google.com/spreadsheets/d/1xMELeUYUcGrqctnCQSWOuB586k1NHth0mgLhUVRu6EI/
2. Add two new columns at the end:
   - **Column K:** "Video Script"
   - **Column L:** "Video URL"
3. Done!

### **Option B: Upload New Template**
1. Download: `Job_Tracking_Sheet_Template_With_Video.csv`
2. Create new sheet OR replace existing headers
3. Headers should be:
```
Title | Job Description | Link | Date | Rating | Company Name | Benefits | Location | Match Explanation | Cover Letter | Video Script | Video URL
```

---

## 🔧 STEP 4: Import Workflow to n8n

**File to import:** `Asheesh_Complete_Email_Video_Automation.json`

### **Import Process:**
1. Open n8n cloud: https://app.n8n.cloud/
2. Click **"Workflows"** in sidebar
3. Click **"+ Add workflow"**
4. Click **"⋮"** (three dots menu) → **"Import from File"**
5. Select: `Asheesh_Complete_Email_Video_Automation.json`
6. Workflow loads with all nodes!

---

## 🔌 STEP 5: Connect All Credentials

You need to connect 4 different services. Go through each node:

### **5A: Gmail Nodes (2 nodes)**

**Nodes:** "Read LinkedIn Alert Emails" + "Mark Email as Read"

1. Click on "Read LinkedIn Alert Emails" node
2. Under **"Credentials"**, click dropdown
3. If Gmail already connected: Select it
4. If NOT connected:
   - Click **"Create New Credential"**
   - Choose **"OAuth2"**
   - Click **"Connect my account"**
   - Sign in with Google
   - Grant permissions
5. **Repeat for "Mark Email as Read" node** (can reuse same credential)

### **5B: OpenAI Nodes (4 nodes)**

**Nodes:**
- "Extract Job Data"
- "Rate Job Match"
- "Generate Cover Letter"
- "Create Video Script"

**For EACH node:**
1. Click the node
2. Under **"Credentials"**, click dropdown
3. If OpenAI already connected: Select it
4. If NOT connected:
   - Click **"Create New Credential"**
   - Paste your OpenAI API key
   - Test connection
5. **Reuse same credential for all 4 nodes!**

### **5C: HeyGen Nodes (2 nodes)**

**Nodes:**
- "Generate Video (HeyGen)"
- "Check Video Status"

**For EACH node:**
1. Click the node
2. You'll see **"Headers"** section with `X-Api-Key`
3. **IMPORTANT:** Replace `{{ $credentials.heygenApi.apiKey }}` with your actual HeyGen API key
4. OR create credential:
   - In n8n, go to **"Credentials"** menu
   - Click **"+ Add Credential"**
   - Search for **"HTTP Header Auth"**
   - Name: "HeyGen API"
   - Header Name: `X-Api-Key`
   - Header Value: `YOUR_HEYGEN_API_KEY`
   - Save
   - Then select this credential in nodes

**Also update Avatar ID:**
1. In "Generate Video (HeyGen)" node
2. Find the body parameters
3. Look for `"avatar_id": "YOUR_AVATAR_ID_HERE"`
4. Replace with your actual Avatar ID from Step 2B

### **5D: Google Sheets Nodes (2 nodes)**

**Nodes:**
- "Save to Google Sheet"
- "Save to Sheet (No Video)"

**For EACH node:**
1. Click the node
2. Under **"Credentials"**, select your Google account
3. **Document ID** should already be: `1xMELeUYUcGrqctnCQSWOuB586k1NHth0mgLhUVRu6EI`
4. If not, paste it manually
5. **Sheet Name:** Select "Sheet1" from dropdown

---

## ✅ STEP 6: Test the Workflow

**IMPORTANT:** Start with small test, then scale up!

### **6A: First Test (Manual Trigger)**

Before scheduling, test manually:

1. **Add Manual Trigger (temporary):**
   - Add a "Manual Trigger" node
   - Connect it to "Read LinkedIn Alert Emails"
   - This lets you test without waiting for 3 AM

2. **Limit to 1 job first:**
   - In "Extract Job URLs" code node
   - Change last line to: `return [uniqueUrls[0]].map(...)` (processes only first URL)
   - This tests end-to-end with single job

3. **Click "Execute Workflow"**

4. **Watch it run!**

**What should happen:**
- Reads your LinkedIn alert emails ✅
- Extracts job URLs ✅
- Scrapes first job ✅
- Extracts data with OpenAI ✅
- Rates the job 0-5 ✅
- Generates cover letter ✅
- Creates video script ✅
- IF rating >= 4: Generates video ✅
- Saves to Google Sheet ✅
- Marks email as read ✅

### **6B: Second Test (Without Video)**

Test with a low-rated job to verify the "no video" path:

1. Process a job you know will score < 4
2. Verify it saves with "Rating < 4 - No video generated" in Video URL column

### **6C: Third Test (Full Batch)**

Once single job works:

1. Remove the URL limit in "Extract Job URLs" code
2. Test with 3-5 jobs
3. Verify all save correctly
4. Check video generation for high-rated jobs

---

## ⏰ STEP 7: Enable Scheduling

Once testing is successful, activate daily automation:

### **7A: Enable Schedule Trigger**

1. Click on "Schedule (Daily 3 AM)" node
2. Verify cron expression: `0 3 * * *` (means 3 AM daily)
3. **To change time:**
   - `0 7 * * *` = 7 AM
   - `0 21 * * *` = 9 PM
   - `0 3 * * *` = 3 AM (recommended - runs while you sleep!)

### **7B: Remove Manual Trigger**

1. Delete the temporary manual trigger node (if you added one)
2. Schedule trigger is now the entry point

### **7C: Activate Workflow**

1. Click **"Active"** toggle in top-right
2. Workflow is now LIVE! ✅
3. Will run automatically every day at 3 AM

---

## 🎯 How It Works Daily

**Every day at 3 AM:**

```
1. Reads unread LinkedIn alert emails
2. Extracts all job URLs from emails
3. For each job:
   a. Scrapes the job page
   b. Extracts structured data (title, company, description, etc.)
   c. Rates 0-5 based on YOUR profile
   d. Generates personalized cover letter in YOUR voice
   e. Creates 60-90 second video script
   f. IF rating >= 4: Generates HeyGen video
   g. Saves all to Google Sheet
4. Marks emails as read
5. You wake up to processed jobs! ☕
```

**Your morning routine:**
1. Open Google Sheet
2. Sort by "Rating" (highest first)
3. Review 4-5 star jobs
4. Watch videos (if generated)
5. Customize cover letters slightly
6. Apply!

---

## 📊 Understanding the Rating System

**How jobs are scored (0-5 scale):**

**Skills Match (0-2 points):**
- 2 points: Perfect match (systems thinking, AI/ML, product architecture)
- 1 point: Partial match
- 0 points: No match

**Experience Level (0-1 points):**
- 1 point: 4-8 years required (mid-senior roles)
- 0 points: Too junior (<2 years) or too senior (10+ years)

**Work Location (0-1 points):**
- 1 point: Remote or hybrid
- 0 points: Fully on-site

**Role Alignment (0-1 points):**
- 1 point: Program leadership, product, AI/ML roles
- 0 points: Pure engineering or unrelated

**Technical Skills (0-1 points):**
- 1 point: Python, AI/ML, systems thinking, product architecture
- 0 points: Different tech stack

**Company/Sector (0-1 points):**
- 1 point: Ed-Tech, AI-first, learning products, startup/scale-up
- 0 points: Different sector

**Bonuses:**
- +0.5: AI Product Manager or Technical PM role
- +0.5: Startup/scale-up environment

**What ratings mean:**
- **5 stars:** Dream job - apply immediately! 🎯
- **4-4.5 stars:** Excellent match - high priority
- **3-3.5 stars:** Good match - review carefully
- **2-2.5 stars:** Possible match - low priority
- **0-1.5 stars:** Poor match - skip

---

## 🎬 Video Generation Strategy

**Videos are ONLY generated for 4-5 star jobs!**

**Why this strategy:**
1. **Saves HeyGen credits** (even with subscription, there are limits)
2. **Saves time** (each video takes 2-5 minutes to generate)
3. **Focus on quality** (videos for best matches only)
4. **Still automated** (you don't manually decide)

**Expected numbers (per month):**
- Total jobs processed: 200-400
- 4-5 star jobs: 40-80 (20%)
- Videos generated: 40-80
- Time saved: 50+ hours

**For 3-star jobs:**
- Still get cover letter ✅
- Still get video script ✅
- Just no video file
- You can manually create video later if interested

---

## 💰 Cost Analysis

**Monthly costs (assuming 300 jobs):**

**OpenAI API:**
- Job scraping: 300 jobs × $0.001 = $0.30
- Rating: 300 jobs × $0.0005 = $0.15
- Cover letter: 300 jobs × $0.002 = $0.60
- Video script: 300 jobs × $0.001 = $0.30
- **Total OpenAI:** ~$1.35/month

**HeyGen:**
- Video generation: 60 videos (4-5 star jobs)
- Cost: $0 (included in your yearly subscription!) ✅

**Total:** ~$1.35/month for COMPLETE automation! 🎉

---

## 🚨 Troubleshooting

### **"No emails found"**
- Check Gmail filter: `from:jobs-listings@linkedin.com is:unread subject:"new jobs"`
- Verify you have unread LinkedIn alert emails
- Check if n8n has Gmail permissions

### **"OpenAI API error"**
- Check API key is correct
- Check OpenAI account has credits ($5 minimum recommended)
- Check rate limits not exceeded
- Try switching from gpt-4o-mini to gpt-4 if context window error

### **"HeyGen video generation failed"**
- Verify Avatar ID is correct
- Check HeyGen API key is valid
- Check HeyGen account has video credits
- Verify avatar is fully processed (not still creating)

### **"Video status stuck at 'processing'"**
- HeyGen videos take 2-5 minutes
- Workflow polls every 30 seconds (max 10 tries = 5 minutes)
- If still stuck, check HeyGen dashboard manually

### **"Google Sheets not saving"**
- Verify Sheet ID is correct
- Check column names match exactly (case-sensitive!)
- Verify Google account has edit permissions
- Check if sheet has been deleted or moved

### **"Jobs rated incorrectly"**
- Review rating explanation in Match Explanation column
- Adjust scoring criteria in "Rate Job Match" node
- Test with known good/bad jobs to calibrate

### **"Cover letters too generic"**
- Add more specific examples to your profile in prompt
- Include stories/projects in system message
- Review and manually edit before sending

---

## 🎯 Expected Results

**By mid-December (45 days of automation):**

**Jobs processed:**
- 10 LinkedIn alerts × 5 jobs/day avg = 50 jobs/day
- 50 jobs × 45 days = 2,250 jobs seen
- Realistic processing: 200-400 jobs (deduplicated)

**High-quality matches:**
- 4-5 star jobs: 40-80 jobs
- 3-star jobs: 60-100 jobs
- Total good matches: 100-180 jobs

**Application materials ready:**
- 200+ cover letters written
- 200+ video scripts created
- 40-80 video resumes generated
- All organized in one spreadsheet

**Time saved:**
- Manual research: 15 min/job × 200 jobs = 50 hours
- Cover letter writing: 30 min/job × 200 jobs = 100 hours
- **Total saved: 150 hours!**

**Your effort:**
- Weekly reviews: 1-2 hours (Sundays)
- Customizing applications: 10 min/job
- Total time: 10-15 hours over 2 months

**ROI: 150 hours saved vs 15 hours invested = 10x return!** 🚀

---

## 📈 Success Metrics to Track

**Track these in your sheet:**

1. **Processing metrics:**
   - Jobs processed per week
   - Rating distribution (how many 4-5 stars?)
   - Video generation success rate

2. **Application metrics:**
   - Applications sent per week
   - Response rate (callbacks/interviews)
   - Response rate WITH video vs WITHOUT

3. **Hypothesis to test:**
   - Applications WITH video: Expected 10-15% response
   - Applications WITHOUT video: Expected 3-5% response
   - **Video advantage: 2-3x better response rate**

4. **Quality metrics:**
   - Are 4-5 star jobs actually good matches?
   - Are cover letters high quality?
   - Do video scripts sound natural?

**Adjust workflow based on data!**

---

## 🎓 This Project Demonstrates

**For your bootcamp portfolio:**

1. ✅ **Email automation** (Gmail API integration)
2. ✅ **Web scraping** (HTTP requests + parsing)
3. ✅ **AI text generation** (OpenAI API, 4 different prompts)
4. ✅ **AI video generation** (HeyGen API integration)
5. ✅ **Workflow orchestration** (n8n, 15+ nodes)
6. ✅ **Data storage** (Google Sheets API)
7. ✅ **Conditional logic** (IF nodes for video generation)
8. ✅ **Polling/waiting** (video status checks)
9. ✅ **Scheduling** (cron-based automation)
10. ✅ **Error handling** (graceful failures)
11. ✅ **Production deployment** (runs unattended)
12. ✅ **Real-world impact** (actual job search automation)

**This is senior-level automation engineering!** 🏆

---

## 📝 Customization Options

### **Change Schedule:**
Edit "Schedule (Daily 3 AM)" node:
- `0 7 * * *` = 7 AM daily
- `0 3 * * 1` = 3 AM every Monday
- `0 21 * * 0,3` = 9 PM Sundays and Wednesdays

### **Change Video Threshold:**
Edit "IF Rating >= 4" node:
- Change `4` to `4.5` (only top jobs get videos)
- Change to `3.5` (more jobs get videos)

### **Change Rating Criteria:**
Edit "Rate Job Match" node prompt:
- Adjust point values
- Add new criteria
- Change what matters most

### **Change Cover Letter Style:**
Edit "Generate Cover Letter" node prompt:
- Make more formal or casual
- Add specific stories
- Change length
- Adjust tone

### **Change Video Script Length:**
Edit "Create Video Script" node prompt:
- Change from "60-90 seconds" to "45-60 seconds" (shorter)
- Change to "90-120 seconds" (longer)
- Adjust word count target

---

## 🎬 Next Steps After Setup

**Immediate (Tonight):**
- [x] Record HeyGen avatar video
- [x] Upload and wait for processing
- [ ] Get HeyGen API key
- [ ] Get Avatar ID
- [ ] Import workflow
- [ ] Connect all credentials
- [ ] Test with 1 job

**Tomorrow:**
- [ ] Test with 5 jobs
- [ ] Verify video generation works
- [ ] Check cover letter quality
- [ ] Activate scheduling
- [ ] Let it run!

**This Weekend:**
- [ ] Review first week's results
- [ ] Adjust rating criteria if needed
- [ ] Test video quality
- [ ] Apply to top matches

**Next 2 Months:**
- [ ] Weekly reviews (Sundays)
- [ ] Track success metrics
- [ ] Refine based on results
- [ ] Focus on studying! 📚

---

## 🏆 Your Competitive Advantage

**Most candidates:**
- Manually search for jobs daily (30+ min)
- Generic cover letters (or no cover letter)
- No video resume
- Apply to 2-3 jobs per week
- Miss opportunities

**YOU with this system:**
- Automated job discovery (0 min daily)
- Personalized cover letters (AI-generated, your voice)
- Professional video resumes (AI-generated, your face)
- Apply to 5-10 jobs per week
- Never miss relevant opportunities
- Stand out from 99% of applicants

**This system IS your competitive advantage!** 💪

---

**Ready to automate your job search! 🚀**

**© 2025 QUEST AND CROSSFIRE™**
*"Small fixes, big clarity"*
