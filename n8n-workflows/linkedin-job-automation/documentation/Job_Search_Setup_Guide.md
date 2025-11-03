# LinkedIn Job Automation - Setup Guide for Asheesh
**Created:** October 30, 2025
**For:** AI Product Manager & Technical PM Job Search (January 2026)

---

## 📦 What I Created For You

### **1. Asheesh_LinkedIn_Job_Automation.json**
- Customized n8n workflow with YOUR profile
- Ratings based on YOUR job criteria
- Cover letters in YOUR voice
- Ready to import into n8n

### **2. Asheesh_Resume_Summary_for_n8n.txt**
- Your complete professional profile
- Formatted for AI job matching
- Use this for reference or updates

### **3. This Setup Guide**
- How to set up RSS feeds
- How to import the workflow
- How to connect Google Sheets
- How to run and customize

---

## 🎯 Your Job Search Criteria

**Target Roles:**
- AI Product Manager
- Technical Product Manager (AI/ML)
- AI Solutions Architect
- Ed-Tech Product Roles

**Salary:** ₹8-12 LPA
**Location:** Remote-first or Lucknow | Willing to relocate
**Start Date:** January 2026

**Key Skills to Match:**
- Systems Thinking
- AI-Native Development
- Product Architecture
- Python & AI/ML
- Team Leadership

---

## 🔍 Step 1: Create LinkedIn Job RSS Feeds

### **Option A: Use RSS.app (Recommended)**

**1. Go to https://rss.app/**

**2. Create RSS Feed for Each Search:**

**Search 1: AI Product Manager India**
- LinkedIn URL: `https://www.linkedin.com/jobs/search/?keywords=AI%20Product%20Manager&location=India`
- Paste into RSS.app
- Get your RSS feed URL

**Search 2: Technical Product Manager AI ML India**
- LinkedIn URL: `https://www.linkedin.com/jobs/search/?keywords=Technical%20Product%20Manager%20AI%20ML&location=India`
- Convert to RSS feed

**Search 3: AI Solutions Architect India Remote**
- LinkedIn URL: `https://www.linkedin.com/jobs/search/?keywords=AI%20Solutions%20Architect&location=India&f_WT=2`
- Convert to RSS feed

**Search 4: Product Manager Ed-Tech India**
- LinkedIn URL: `https://www.linkedin.com/jobs/search/?keywords=Product%20Manager%20EdTech&location=India`
- Convert to RSS feed

**Search 5: Product Manager AI Startup India**
- LinkedIn URL: `https://www.linkedin.com/jobs/search/?keywords=Product%20Manager%20AI%20Startup&location=India`
- Convert to RSS feed

**3. Save All Your RSS Feed URLs**

Example format:
```
AI PM: https://rss.app/feeds/ABC123.xml
Tech PM AI: https://rss.app/feeds/DEF456.xml
AI Solutions: https://rss.app/feeds/GHI789.xml
Ed-Tech PM: https://rss.app/feeds/JKL012.xml
AI Startup: https://rss.app/feeds/MNO345.xml
```

---

### **Option B: Use LinkedIn's Native RSS (Advanced)**

Some LinkedIn job searches have RSS built-in. Check if URL ends with `.rss`

---

## 📊 Step 2: Create Google Sheet for Job Tracking

**1. Create New Google Sheet:**
- Name: "Asheesh Job Listings 2026"
- Share with your n8n Google account

**2. Add Column Headers (Row 1):**
```
Title | Job Description | Link | Date | Rating | Company Name | Benefits | Location | Match Explanation | Cover Letter
```

**3. Get Sheet ID:**
- From URL: `https://docs.google.com/spreadsheets/d/[SHEET_ID_HERE]/edit`
- Copy the SHEET_ID part
- You'll need this for n8n

---

## 🚀 Step 3: Import Workflow to n8n

**1. In n8n Dashboard:**
- Click "+ New Workflow" (or open existing)
- Click "..." menu (three dots)
- Select "Import from File"
- Choose: `Asheesh_LinkedIn_Job_Automation.json`

**2. Workflow Will Load With:**
- Manual Trigger node
- RSS Read node
- Limit node (5 jobs at a time)
- HTTP Request node
- 3 OpenAI nodes (job scraper, rating, cover letter)
- Google Sheets node

---

## 🔧 Step 4: Configure the Workflow

### **4A: Update RSS Feed URL**

**Find the "RSS Read" node:**
1. Click on it
2. Update URL field with YOUR first RSS feed URL
3. Example: `https://rss.app/feeds/YOUR_FEED_ID.xml`

**For Multiple Feeds (Advanced):**
- You can add more RSS Read nodes
- Or use a Loop node to cycle through multiple feeds
- Start with one feed first!

---

### **4B: Connect OpenAI API**

**For Each OpenAI Node (3 total):**
1. Click the node
2. Find "Credentials" field
3. Select "Create New Credential"
4. Paste your OpenAI API key from `.streamlit/secrets.toml`
5. Test connection
6. Repeat for all 3 OpenAI nodes

**Note:** You can reuse the same credential for all 3 nodes!

---

### **4C: Connect Google Sheets**

**Find "Append or update row in sheet" node:**
1. Click on it
2. Credentials: Use the Google account you already set up
3. Document ID: Click "From list" and select your "Asheesh Job Listings 2026" sheet
4. OR paste the Sheet ID you copied earlier
5. Sheet Name: "Sheet1" (or your sheet name)
6. Column mapping is already configured for you!

---

## ✅ Step 5: Test the Workflow

**1. First Test (Small):**
- Make sure the "Limit" node is set to 5 (limits to 5 jobs)
- Click "Execute workflow" button
- Watch it run!

**What Should Happen:**
1. ✅ Reads 5 recent jobs from RSS feed
2. ✅ Scrapes each job listing details
3. ✅ AI rates how well each job matches YOU (0-5 scale)
4. ✅ AI generates custom cover letter for each
5. ✅ Saves all data to your Google Sheet

**2. Check Your Google Sheet:**
- Should see 5 new rows
- Check the Rating column (0-5)
- Read the Match Explanation
- Review the cover letters!

**3. If It Works:**
- You can increase the Limit (or remove it)
- Add more RSS feeds
- Set it to run on a schedule!

---

## 🎨 How the Rating System Works

**Your Custom Rating Criteria (0-5 scale):**

**2 points:** Skills match perfectly
- Systems thinking, AI/ML, product architecture
- 1 point if partial match

**1 point:** Right experience level
- 4-8 years for mid-senior roles

**1 point:** Remote or hybrid option

**1 point:** Job role aligns with your past
- Program leadership, product, AI/ML

**1 point:** Technical skills align
- Python, AI/ML, systems thinking

**1 point:** Company/sector matches
- Ed-Tech, AI-first, learning products

**Bonus +0.5:** AI PM or Technical PM role
**Bonus +0.5:** Startup/scale-up

**Jobs rated 4-5:** Excellent matches - apply ASAP!
**Jobs rated 3:** Good matches - review carefully
**Jobs rated 0-2:** Poor matches - skip or low priority

---

## 📝 How Cover Letters Are Generated

**Your Cover Letters Will:**
- Show genuine interest in the specific role
- Highlight relevant experience (not just resume bullets)
- Use your voice: reflective, honest, systematic
- Connect your "Small fixes, big clarity" philosophy
- Mention Quest & Crossfire and your projects
- Professional but conversational tone
- 300-400 words maximum

**They Avoid:**
- Generic phrases
- Over-the-top enthusiasm
- Simply listing resume
- Being too formal

---

## 🔄 Step 6: Automate (Optional)

### **Run on Schedule:**

**Add Schedule Trigger Node:**
1. Remove Manual Trigger OR
2. Add Schedule Trigger alongside it
3. Set schedule: Daily at 9 AM
4. Connect to RSS Read node

**Recommended Schedule:**
- **Daily:** If actively job hunting
- **Every 3 days:** For passive search
- **Weekly:** If not urgent

**This will:**
- Automatically check for new jobs
- Rate them against your profile
- Generate cover letters
- Add to your tracking sheet

---

## 🎯 Step 7: Workflow Usage Tips

### **Review Your Matches:**

**In Google Sheet:**
1. Sort by "Rating" (highest first)
2. Read "Match Explanation" for 4-5 rated jobs
3. Click "Link" to view job posting
4. Review the generated cover letter
5. Customize cover letter if needed
6. Apply!

### **Best Practices:**

**For 4-5 Star Matches:**
- Apply within 24-48 hours
- Customize cover letter slightly (add specific company detail)
- Mention any connections or referrals
- Follow up after 1 week

**For 3 Star Matches:**
- Review carefully
- Research company first
- Decide if worth applying
- May need more cover letter customization

**For 0-2 Star Matches:**
- Skip or low priority
- Good for understanding market
- Might apply if desperate or interested despite low match

---

## 🔧 Customization Options

### **Change Rating Criteria:**

Edit the "Message a model" node (rating node):
- Adjust point values
- Add your own criteria
- Change what matters most to you

### **Change Cover Letter Style:**

Edit the "Message a model1" node (cover letter node):
- Make it more formal or casual
- Add specific stories/examples
- Change length (currently 300-400 words)
- Adjust tone

### **Change Job Limit:**

Edit the "Limit" node:
- 5 jobs: Quick testing
- 10 jobs: Daily runs
- 20+ jobs: Weekly comprehensive search
- Remove limit: Process all jobs (expensive!)

### **Add More RSS Feeds:**

**Option 1:** Replace URL in RSS Read node
**Option 2:** Add multiple RSS Read nodes
**Option 3:** Use Loop node to cycle through list of feeds

---

## 💰 Cost Estimates

**OpenAI API Costs:**
- Per job: ~500-800 tokens (scraping + rating + cover letter)
- Cost per job: ~$0.001-0.002 (very cheap!)
- 100 jobs: ~$0.10-0.20
- 1000 jobs/month: ~$1-2

**With GPT-4o-mini:** Even cheaper!

**Recommendation:**
- Set Limit to 10-20 jobs per run
- Run daily for active search
- Budget: ~$5-10/month for comprehensive search

---

## 🚨 Troubleshooting

### **"RSS feed returns no data"**
- Check if RSS feed URL is valid
- Test URL in browser
- RSS.app free tier may have limits
- Try different RSS service

### **"OpenAI node fails"**
- Check API key is correct
- Check OpenAI account has credits
- Check rate limits not exceeded
- Try GPT-3.5-turbo instead of GPT-4o-mini

### **"Google Sheets not saving"**
- Check credentials are connected
- Check sheet ID is correct
- Check column names match exactly
- Check Google account has edit permissions

### **"Jobs rated incorrectly"**
- Review your profile in the rating node
- Adjust scoring criteria
- Add more specific details about your skills
- Test with known good/bad job matches

### **"Cover letters too generic"**
- Add more personality to your profile
- Include specific stories/examples
- Adjust system prompt for more customization
- Review and manually edit before sending

---

## 📋 Your Customized Job Search Checklist

**Setup (Do Once):**
- [ ] Create 3-5 LinkedIn job RSS feeds (AI PM, Tech PM, etc.)
- [ ] Create Google Sheet "Asheesh Job Listings 2026"
- [ ] Import workflow to n8n
- [ ] Connect OpenAI API (3 nodes)
- [ ] Connect Google Sheets
- [ ] Update RSS feed URL in workflow
- [ ] Test with 5 jobs

**Weekly Routine:**
- [ ] Run workflow (manual or scheduled)
- [ ] Sort sheet by Rating
- [ ] Review 4-5 star matches
- [ ] Research companies
- [ ] Customize cover letters
- [ ] Apply to top matches
- [ ] Track applications

**Monthly Review:**
- [ ] Review rating accuracy
- [ ] Adjust criteria if needed
- [ ] Update RSS feeds (new searches)
- [ ] Update your profile in workflow (new skills/projects)
- [ ] Check OpenAI costs

---

## 🎯 Expected Results

**With This Workflow You Should:**
- ✅ Save 10+ hours/week on job search
- ✅ Never miss relevant opportunities
- ✅ Get personalized cover letters instantly
- ✅ Focus on high-match jobs only
- ✅ Track all applications in one place
- ✅ Apply faster than other candidates

**Success Metrics:**
- 20-30 new jobs reviewed per week
- 5-10 high-match jobs (4-5 stars) per week
- 3-5 applications sent per week
- Higher response rate (targeted applications)

---

## 🚀 Next Steps

**Right Now (In Bootcamp Class):**
1. Follow instructor's workflow demo
2. Learn any additional techniques
3. Ask questions about customization

**After Class Tonight:**
1. Import your customized workflow
2. Create your RSS feeds
3. Set up Google Sheet
4. Test with 5 jobs
5. Review results

**This Weekend:**
1. Add more RSS feeds
2. Customize rating criteria
3. Test cover letter quality
4. Set up automation schedule

**Starting Next Week:**
1. Run daily job searches
2. Apply to high-match jobs
3. Track applications
4. Refine based on results

---

## 📞 Your Workflow Files

**Created in D:\Claude\Profile\:**
1. ✅ `Asheesh_LinkedIn_Job_Automation.json` (Import this to n8n)
2. ✅ `Asheesh_Resume_Summary_for_n8n.txt` (Your profile for reference)
3. ✅ `Job_Search_Setup_Guide.md` (This guide)

---

## 💡 Pro Tips

1. **Start Small:** Test with 5 jobs first, then scale up
2. **Review AI Output:** Always review cover letters before sending
3. **Customize High Matches:** For 5-star jobs, add company-specific details
4. **Track Everything:** Use the sheet to track application status
5. **Update Profile:** As you complete projects, update your profile in the workflow
6. **Multiple Feeds:** Use different RSS feeds for different types of roles
7. **Set Alerts:** Google Sheets can email you when high-rated jobs appear
8. **Learn Patterns:** After 50+ jobs, you'll see what rating criteria matter most

---

**Ready to find your perfect AI Product Manager role!** 🎯🚀

**© 2025 QUEST AND CROSSFIRE™**
*"Small fixes, big clarity"*
