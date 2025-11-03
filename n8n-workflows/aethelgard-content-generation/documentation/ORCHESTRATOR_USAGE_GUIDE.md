# Aethelgard Master Orchestrator - Usage Guide

**Purpose:** Automate multi-layer content generation without manual intervention
**Created:** November 2, 2025

---

## 🎯 Problem This Solves

**WITHOUT Orchestrator (Manual Process):**
```
1. Trigger Layer 1 → Wait → Get file ID from Drive
2. Trigger Layer 2 with file ID → Wait → Get file ID
3. Trigger RAG with file ID → Wait
4. Trigger Layer 3 with file ID → Wait
5. Repeat for EACH of 72 concepts (288 manual steps!)
```

**WITH Orchestrator (Automated):**
```
1. Trigger orchestrator once
2. ☕ Get coffee
3. All layers generated automatically for all concepts
```

---

## 📋 How It Works

### **Workflow Flow:**

```
Webhook Trigger
    ↓
Read Curriculum + Progress Tracker
    ↓
Select Pending Concepts (or specific ones)
    ↓
FOR EACH CONCEPT:
    ↓
    Trigger Layer 1 → Wait 10s
    ↓
    IF layer2 requested → Trigger Layer 2 → Wait 15s
    ↓
    IF rag requested → Trigger RAG (parallel)
    ↓
    IF layer3 requested → Trigger Layer 3 → Wait 20s
    ↓
NEXT CONCEPT
    ↓
Respond with Summary
```

### **Key Features:**

✅ **Auto-chaining:** Automatically passes file IDs between workflows
✅ **Batch processing:** Process multiple concepts in one trigger
✅ **Selective layers:** Choose which layers to generate
✅ **Progress tracking:** Skips already completed concepts
✅ **Configurable waits:** Adjust timing for your n8n instance speed

---

## ⚙️ Setup Instructions

### **Step 1: Update n8n URLs**

In the orchestrator workflow, find and replace `YOUR_N8N_INSTANCE` with your actual n8n URL:

**5 HTTP Request nodes to update:**

1. **"Trigger Layer 1 Generation"** node:
   ```
   URL: https://YOUR_N8N_INSTANCE/webhook/aethelgard-generate
   Replace with: https://qnc-asheesh.app.n8n.cloud/webhook/aethelgard-generate
   ```

2. **"Trigger Layer 2"** node:
   ```
   URL: https://YOUR_N8N_INSTANCE/webhook/aethelgard-generate-layer2
   ```

3. **"Trigger RAG Enrichment"** node:
   ```
   URL: https://YOUR_N8N_INSTANCE/webhook/aethelgard-enrich-rag
   ```

4. **"Trigger Layer 3"** node:
   ```
   URL: https://YOUR_N8N_INSTANCE/webhook/aethelgard-generate-layer3
   ```

5. **Authentication:** Set up n8n API authentication (or remove auth if same instance)

---

### **Step 2: Configure Wait Times**

Adjust wait times based on your Gemini API speed:

- **"Wait for Layer 1":** Default 10s (Layer 1 takes ~45-60s, but triggers async)
- **"Wait for Layer 2":** Default 15s (Layer 2 takes ~60-90s)
- **"Wait for Layer 3":** Default 20s (Layer 3 takes ~90-120s)

**Why wait times?**
- Workflows trigger via HTTP and return immediately
- Wait times give workflows time to complete before next trigger
- If workflows fail, increase wait times

**Optimal settings:**
- Fast n8n instance: 5s / 10s / 15s
- Standard: 10s / 15s / 20s (default)
- Slow/free tier: 20s / 30s / 40s

---

### **Step 3: Import to n8n**

1. Go to n8n → Workflows
2. Click "Import from File"
3. Select `Aethelgard Master Orchestrator.json`
4. Configure Google Drive credentials (same as other workflows)
5. Update n8n URLs (Step 1)
6. Save workflow
7. **Activate workflow** (toggle switch to ON)

---

## 🚀 Usage Options

### **Option 1: Single Concept (Test Mode)**

**Use Case:** Test the orchestrator with 1 concept

```bash
POST https://your-n8n.app.n8n.cloud/webhook/aethelgard-orchestrator

Body:
{
  "mode": "single",
  "concepts": ["00-01"],
  "layers": ["layer1", "layer2", "rag", "layer3"]
}
```

**What happens:**
- Generates all 4 layers for concept "00-01 Why Anaconda?"
- Takes ~5 minutes total
- Returns summary when complete

---

### **Option 2: Batch Processing (5 Concepts)**

**Use Case:** Generate content for next 5 pending concepts

```bash
POST https://your-n8n.app.n8n.cloud/webhook/aethelgard-orchestrator

Body:
{
  "mode": "batch",
  "batchSize": 5,
  "layers": ["layer1", "layer2", "rag"]
}
```

**What happens:**
- Finds 5 concepts not yet completed
- Generates Layer 1, Layer 2, RAG for each (skips Layer 3)
- Takes ~25 minutes total
- Perfect for daily runs

---

### **Option 3: Specific Concepts**

**Use Case:** Generate specific concepts you choose

```bash
POST https://your-n8n.app.n8n.cloud/webhook/aethelgard-orchestrator

Body:
{
  "mode": "batch",
  "concepts": ["00-01", "00-02", "00-04", "01-01", "01-02"],
  "layers": ["layer1", "layer2"]
}
```

**What happens:**
- Generates only Layer 1 and Layer 2 for listed concepts
- Skips RAG and Layer 3
- You control exactly which concepts to process

---

### **Option 4: Layer 1 Only (Fast Batch)**

**Use Case:** Generate all Layer 1 content quickly, add layers later

```bash
POST https://your-n8n.app.n8n.cloud/webhook/aethelgard-orchestrator

Body:
{
  "mode": "batch",
  "batchSize": 72,
  "layers": ["layer1"]
}
```

**What happens:**
- Generates Layer 1 for ALL 72 concepts
- Takes ~1-1.5 hours
- Then run again with `["layer2", "rag", "layer3"]` later

---

### **Option 5: Complete All Pending**

**Use Case:** Generate everything for all concepts not yet done

```bash
POST https://your-n8n.app.n8n.cloud/webhook/aethelgard-orchestrator

Body:
{
  "mode": "batch",
  "batchSize": 72,
  "layers": ["layer1", "layer2", "rag", "layer3"]
}
```

**What happens:**
- Processes ALL pending concepts
- All 4 layers for each
- Takes ~6 hours for 72 concepts
- **Best for: Weekend batch run**

---

## 📅 Automation Strategies

### **Strategy 1: Daily Scheduled Batches**

**Goal:** Generate 5-10 concepts per day automatically

**Setup:**

1. **Add Schedule Trigger to Orchestrator:**
   - In n8n, add **"Schedule Trigger"** node at the beginning
   - Set to run daily at 3 AM
   - Connect to "Read Curriculum" node

2. **Configuration:**
   ```json
   {
     "mode": "batch",
     "batchSize": 6,
     "layers": ["layer1", "layer2", "rag"]
   }
   ```

3. **Timeline:**
   - 6 concepts/day × 17 days = 102 concepts (more than 72!)
   - Complete all content before subscription expires ✅

**Pros:**
- Set and forget
- Spreads workload over days
- Can review daily batches

**Cons:**
- Takes 12-17 days
- Less control over specific concepts

---

### **Strategy 2: Weekend Mega-Batch**

**Goal:** Generate ALL content in one weekend

**Setup:**

1. **Saturday Morning:** Run full Layer 1 batch
   ```json
   {
     "mode": "batch",
     "batchSize": 72,
     "layers": ["layer1"]
   }
   ```
   Duration: ~1.5 hours

2. **Saturday Afternoon:** Review Layer 1 outputs (3-4 hours)

3. **Saturday Evening:** Run Layer 2 + RAG batch
   ```json
   {
     "mode": "batch",
     "batchSize": 72,
     "layers": ["layer2", "rag"]
   }
   ```
   Duration: ~2 hours

4. **Sunday Morning:** Review Layer 2/RAG (2-3 hours)

5. **Sunday Afternoon:** Run Layer 3 for top 30 concepts
   ```json
   {
     "mode": "batch",
     "concepts": ["00-01", "00-02", ..., "top 30 IDs"],
     "layers": ["layer3"]
   }
   ```
   Duration: ~1 hour

**Pros:**
- Done in 2 days
- Maximum focus
- Can adjust on the fly

**Cons:**
- Intense weekend
- All-or-nothing approach

---

### **Strategy 3: Manual Triggered (No Scheduling)**

**Goal:** Full control, trigger when ready

**Setup:**

1. **Keep orchestrator unscheduled** (webhook trigger only)

2. **Use Postman/Insomnia/cURL to trigger:**
   - Save different request templates
   - Trigger manually when you have time
   - Perfect for testing and iteration

3. **Example workflow:**
   - Day 1: Generate 10 concepts (Layer 1 only)
   - Day 2: Review, then trigger Layer 2+RAG for those 10
   - Day 3: Generate next 10 concepts (Layer 1)
   - Repeat...

**Pros:**
- Full control
- Review between batches
- Adjust based on quality

**Cons:**
- Requires manual intervention
- Easy to forget/delay

---

## 🎯 Recommended Approach for Your 17-Day Timeline

Based on your **17 days left** and **72 concepts** to generate:

### **RECOMMENDED: Hybrid Strategy**

**Week 1 (Days 1-7): Fast Batch + Review**

**Day 1:** Generate all 72 Layer 1
```json
{
  "mode": "batch",
  "batchSize": 72,
  "layers": ["layer1"]
}
```
Duration: 1.5 hours

**Days 2-3:** Review Layer 1 quality
- Read 10-15 samples
- Check for errors/issues
- Note any prompt improvements needed

**Day 4:** Generate all 72 Layer 2 + RAG
```json
{
  "mode": "batch",
  "batchSize": 72,
  "layers": ["layer2", "rag"]
}
```
Duration: 2-3 hours

**Days 5-7:** Review Layer 2/RAG quality
- Test RAG metadata usefulness
- Check adult learning enhancements
- Validate semantic tags

---

**Week 2 (Days 8-14): Story Mode + Polishing**

**Day 8:** Generate Layer 3 for top 30 concepts
```json
{
  "mode": "batch",
  "concepts": ["list of 30 important concept IDs"],
  "layers": ["layer3"]
}
```
Duration: 1-2 hours

**Days 9-11:** Review story mode quality
- Check narrative consistency
- Verify technical accuracy maintained
- Test with 2-3 beta users

**Days 12-14:** Regenerate any poor-quality content
```json
{
  "mode": "batch",
  "concepts": ["IDs that need regeneration"],
  "layers": ["layer1", "layer2"]
}
```

---

**Week 3 (Days 15-17): Buffer + Final Polish**

- Final quality checks
- Export to production format
- Prepare for AXIS integration
- 🎉 Celebrate completion before subscription expires!

---

## 🔧 Troubleshooting

### **"Workflow takes too long / times out"**

**Solution:** Increase wait times in orchestrator
- Edit "Wait for Layer X" nodes
- Change from 10s → 30s or 60s
- Or trigger smaller batches (batchSize: 3 instead of 5)

---

### **"File ID not found" errors**

**Problem:** Next workflow triggered before previous one saved to Drive

**Solutions:**
1. Increase wait times (primary fix)
2. Add "Check file exists" logic before triggering next layer
3. Reduce batch size to avoid Google Drive API rate limits

---

### **"Some concepts skipped"**

**Problem:** Progress tracker not updated properly

**Solution:**
- Manually check Google Drive folder
- Update progress tracker JSON manually
- Or use `"concepts": ["specific-ids"]` to force regeneration

---

### **"RAG/Layer 3 generation fails"**

**Problem:** Input file not found or corrupted

**Solutions:**
1. Check previous layer completed successfully
2. Verify Google Drive folder IDs correct
3. Test individual workflows first before orchestrator
4. Check n8n execution logs for specific error

---

## 📊 Cost & Performance

### **With Orchestrator:**

**Single Concept (All Layers):**
- Layer 1: 45s
- Wait: 10s
- Layer 2: 60s
- Wait: 15s
- RAG: 30s (parallel)
- Layer 3: 90s
- Wait: 20s
- **Total: ~5 minutes per concept**

**72 Concepts (All Layers):**
- Total time: ~6 hours
- Gemini API calls: ~288 (72 × 4 layers)
- Cost: FREE (within Gemini 1.5 Flash free tier: 1,500 req/day)

### **Optimization Tips:**

1. **Run Layer 1 for all concepts first** (1.5 hours)
   - Then review quality before continuing
   - Saves time if prompt needs adjustment

2. **Use parallel execution** (advanced)
   - Trigger 5-10 concepts simultaneously
   - Requires n8n Pro plan (parallel execution)
   - Can complete 72 concepts in ~1 hour

3. **Skip Layer 3 initially** (focus on Layer 1+2+RAG)
   - Story mode is optional enhancement
   - Can always generate Layer 3 later for top concepts

---

## 🎓 Learning Curve

**First time using orchestrator:**
- Test with 1 concept first
- Check outputs manually
- Adjust wait times if needed
- Then scale to 5, then 10, then full batch

**After 2-3 successful runs:**
- You'll understand timing
- Can predict completion times
- Comfortable with batch processing

---

## 🚀 Next Steps

1. **Import orchestrator workflow** to n8n
2. **Update n8n URLs** in HTTP Request nodes
3. **Test with 1 concept:** `{"mode": "single", "concepts": ["00-01"], "layers": ["layer1"]}`
4. **Review output** in Google Drive
5. **Scale to 5 concepts:** `{"mode": "batch", "batchSize": 5, "layers": ["layer1", "layer2"]}`
6. **Choose automation strategy** (Daily / Weekend / Manual)
7. **Execute full batch** before Nov 18 deadline

---

## ✅ Benefits Summary

**WITH Orchestrator:**
- ✅ 288 manual steps → 1 API call
- ✅ 6 hours of manual work → Automated
- ✅ No forgotten concepts
- ✅ Consistent quality (same prompts)
- ✅ Progress tracking automatic
- ✅ Can schedule for off-hours
- ✅ Focus on review, not triggering

**WITHOUT Orchestrator:**
- ❌ 288 manual triggers required
- ❌ High chance of errors
- ❌ Tedious copy-paste of file IDs
- ❌ Easy to lose track of progress
- ❌ Full-time job for 2-3 days

---

**The orchestrator is your automation multiplier!** 🚀

Set it up once, use it for all 72 concepts, and maximize your Gemini subscription ROI with minimal manual work.
