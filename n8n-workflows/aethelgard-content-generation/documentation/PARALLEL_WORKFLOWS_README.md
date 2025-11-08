# Aethelgard Parallel Content Generation Workflows

**Created:** November 2, 2025
**Purpose:** Automated multi-layer content generation system for Aethelgard Academy
**Tech Stack:** n8n + Google Gemini + Google Drive

---

## 📊 System Overview

This is a **parallel workflow system** for generating educational content in multiple formats simultaneously:

```
Layer 1 (Base) ──→ Layer 2 (Adult Learning) ──→ Layer 3 (Story Mode)
       ↓
  RAG Enrichment (parallel to all layers)
```

### **4 Workflows:**

1. **Layer 1 Content Generator** (ORIGINAL) - Base factual content (PSW framework)
2. **Layer 2 Adult Learning Transformer** (NEW) - Andragogy-optimized content
3. **RAG Enrichment Engine** (NEW) - Semantic metadata for AXIS AI retrieval
4. **Layer 3 Story Mode Generator** (NEW) - Narrative-driven Aethelgard RPG format

---

## 🎯 Workflow Purposes

### **1. Layer 1: Base Content Generator**
**File:** `Aethelgard Layer 1 Content Generator.json`
**Webhook:** `aethelgard-generate`
**Output Folder:** `layer1_base_content/` (Google Drive ID: `1YOw-1Cx61CL23UGm9jxFtn70XUON-OjN`)

**What It Does:**
- Reads curriculum context and completed concepts tracker
- Builds PSW (Problem-System-Win) educational content
- Generates neutral, factual Python learning materials
- Includes code examples, exercises, metadata
- Saves JSON to Google Drive

**Content Structure:**
```json
{
  "conceptId": "00-02",
  "conceptName": "Installing Anaconda",
  "domain": "Python Environment & Setup",
  "layer": 1,
  "content": {
    "problem": { ... },
    "system": { ... },
    "win": { ... },
    "exercises": [ ... ]
  }
}
```

---

### **2. Layer 2: Adult Learning Transformer**
**File:** `Aethelgard Layer 2 Adult Learning Transformer.json`
**Webhook:** `aethelgard-generate-layer2`
**Input:** Layer 1 JSON file
**Output Folder:** `layer2_adult_learning/` (Google Drive)

**What It Does:**
- Reads Layer 1 content as input
- Applies Malcolm Knowles' 6 principles of andragogy
- Adds career context, professional scenarios, competency markers
- Transforms passive explanations into discovery-based learning
- Adds reflection prompts and real-world stakes

**Key Transformations:**
- ✅ **Self-Concept:** Emphasizes learner autonomy
- ✅ **Experience:** Leverages prior knowledge
- ✅ **Readiness:** Connects to career relevance
- ✅ **Orientation:** Problem-centered approach
- ✅ **Motivation:** Intrinsic motivators (competence, purpose)
- ✅ **Need to Know:** Explicit "why" statements

**Enhanced Structure:**
```json
{
  "conceptId": "00-02",
  "layer": 2,
  "content": {
    "problem": {
      ...original fields,
      "careerContext": "Junior devs need this for...",
      "realWorldStakes": "Without this, you'll face...",
      "immediateApplicability": "Use within 24 hours by..."
    },
    "system": {
      ...original fields,
      "mentalModel": "Conceptual framework...",
      "decisionFramework": "When to use X vs Y...",
      "professionalPatterns": ["Expert pattern 1", ...]
    },
    "win": {
      ...original fields,
      "competencyMarkers": ["Observable mastery signs..."],
      "portfolioProjects": ["Project ideas..."],
      "interviewReadiness": "How to discuss in interviews..."
    }
  }
}
```

---

### **3. RAG Enrichment Engine**
**File:** `Aethelgard RAG Enrichment Engine.json`
**Webhook:** `aethelgard-enrich-rag`
**Input:** Layer 1, 2, or 3 JSON file
**Output Folder:** `rag_enriched/` (Google Drive)

**What It Does:**
- Adds semantic metadata WITHOUT changing educational content
- Generates tags, keywords, chunks, mode adaptations
- Optimizes content for vector database retrieval
- Maps error patterns for troubleshooting queries
- Creates Q&A pairs for RAG system

**RAG Metadata Added:**
```json
{
  "conceptId": "00-02",
  "originalContent": { ...preserves all original content... },
  "ragMetadata": {
    "semanticTags": [
      "environment-management",
      "package-installation",
      "conda-setup",
      ...
    ],
    "questionKeywords": [
      "How do I install Anaconda?",
      "What is conda?",
      "Why won't conda work?",
      ...
    ],
    "chunks": [
      {
        "chunkId": "00-02-chunk-01",
        "chunkTitle": "Step-by-Step Installation",
        "startContext": "Go to the official...",
        "endContext": "...click Finish.",
        "semanticSummary": "Complete Anaconda installation procedure",
        "questionsCovered": ["How to install?", "Where to download?", ...]
      }
    ],
    "axisAdaptations": {
      "coachMode": {
        "preferredChunks": ["00-02-chunk-01"],
        "retrievalPriority": "step-by-step",
        "voiceTone": "supportive"
      },
      "socraticMode": {
        "guidingQuestions": [
          "Why do you think Anaconda needs admin access?",
          "What would happen if you skipped the PATH option?",
          ...
        ]
      }
    },
    "errorPatterns": [
      {
        "errorText": "conda: command not found",
        "symptom": "Terminal doesn't recognize conda",
        "relevantChunk": "00-02-chunk-03",
        "quickFix": "Add Anaconda to PATH during installation"
      }
    ],
    "difficultyLayers": {
      "basic": { "simplifiedExplanation": "ELI5 version..." },
      "intermediate": { "fullExplanation": "Standard version..." },
      "advanced": { "edgeCases": [...], "internals": "..." }
    }
  }
}
```

---

### **4. Layer 3: Story Mode Generator**
**File:** `Aethelgard Layer 3 Story Mode Generator.json`
**Webhook:** `aethelgard-generate-layer3`
**Input:** Layer 2 JSON file
**Output Folder:** `layer3_story_mode/` (Google Drive)

**What It Does:**
- Transforms educational content into narrative RPG format
- Uses Aethelgard universe lore and characters
- Frames learning as quests, code as spellcasting
- Maintains technical accuracy while adding immersive story
- Character-driven mentorship (Master Conda, Professor Pythia, etc.)

**Key Characters:**
- **Master Conda:** Environment Artificer (teaches conda, environments)
- **Professor Pythia:** Data Weaver (teaches data manipulation)
- **Sergeant Syntax:** Logic Architect (teaches control flow)
- **Alchemist Ada:** Error Handler (teaches debugging)

**Story Structure:**
```json
{
  "conceptId": "00-02",
  "layer": 3,
  "content": {
    "questHook": {
      "character": "Master Conda",
      "characterDialogue": "Ah, young apprentice! Welcome to my guild...",
      "storyProblem": "The guild faces chaos—projects mixing dangerous magical ingredients...",
      "firstMission": "Learn the Sanctuary Creation Spell..."
    },
    "guidedJourney": {
      "magicSystemExplanation": "In Aethelgard, code is magic. Each command is an incantation...",
      "mentorGuidance": "Master Conda strokes his beard. 'My dear apprentice...'",
      "spellcasting": [
        {
          "spellName": "Sanctuary Creation Spell",
          "incantation": "conda create --name my_project python=3.9",
          "spellExplanation": "As you speak these words, magical energy swirls...",
          "manifestation": "A protected space manifests in the Anaconda Realm...",
          "masterAsks": "What would happen if you used python=2.7?"
        }
      ]
    },
    "trials": [
      {
        "trialName": "The First Guild Mission",
        "scenario": "Your first task: create a sanctuary for a data analysis project...",
        "challenge": "Cast the environment creation spell correctly...",
        "masterFeedback": "Well done, apprentice! You've created your first isolated sanctuary..."
      }
    ],
    "questCompletion": {
      "characterCelebration": "Master Conda beams with pride...",
      "newPowersUnlocked": ["Create isolated environments", "Manage project dependencies"],
      "titleEarned": "Apprentice Environment Mage",
      "nextQuestTeaser": "But creating sanctuaries is just the beginning..."
    }
  }
}
```

---

## 🔧 Configuration Guide

### **Prerequisites:**
1. n8n Cloud or self-hosted instance
2. Google Cloud Project with Drive API enabled
3. Google Gemini API key
4. Google Drive folder structure created

### **Google Drive Setup:**

Create this folder structure in Google Drive:

```
Aethelgard_Content_Generation/
├── _metadata/
│   ├── curriculum_context.json       (ID: 1e-rI0IPdAbzFVrre_QhdgDjiS3h1h1yj)
│   └── completed_concepts.json       (ID: 1nyKt5ZkrB1GivZVR7LfD6IRIIOrUBJLj)
├── layer1_base_content/              (ID: 1YOw-1Cx61CL23UGm9jxFtn70XUON-OjN)
├── layer2_adult_learning/            (ID: REPLACE_WITH_YOUR_ID)
├── layer3_story_mode/                (ID: REPLACE_WITH_YOUR_ID)
└── rag_enriched/                     (ID: REPLACE_WITH_YOUR_ID)
```

**Get Folder IDs:**
1. Open folder in Google Drive
2. URL format: `https://drive.google.com/drive/folders/{FOLDER_ID}`
3. Copy the `{FOLDER_ID}` part

### **Import Workflows:**

**For Each Workflow:**
1. Open n8n
2. Click Workflows → Import from File
3. Select JSON file
4. Configure credentials (Google Drive OAuth, Gemini API)
5. Update folder IDs in nodes

**Nodes to Update:**

#### **Layer 1 (Original - already configured):**
- ✅ No changes needed (already working)

#### **Layer 2 Transformer:**
- **"Read Layer 1 Content" node:** Set `INPUT_LAYER1_FILE_ID` to specific Layer 1 output file
- **"Save Layer 2 JSON to Drive" node:** Replace `FOLDER_ID_FOR_LAYER2` with your folder ID

#### **RAG Enrichment:**
- **"Read Base Content" node:** Set `INPUT_BASE_CONTENT_FILE_ID` to any layer's output
- **"Save RAG-Enriched JSON to Drive" node:** Replace `FOLDER_ID_FOR_RAG_ENRICHED` with your folder ID

#### **Layer 3 Story Mode:**
- **"Read Layer 2 Content" node:** Set `INPUT_LAYER2_FILE_ID` to Layer 2 output file
- **"Save Layer 3 Story to Drive" node:** Replace `FOLDER_ID_FOR_LAYER3` with your folder ID

---

## 🚀 Usage Examples

### **Sequential Generation (Recommended):**

**Step 1: Generate Layer 1 (Base Content)**
```bash
POST https://your-n8n.app.n8n.cloud/webhook/aethelgard-generate
Body:
{
  "conceptId": "00-02",
  "conceptName": "Installing Anaconda",
  "domain": "Python Environment & Setup",
  "subdomain": "Environment Setup"
}
```

**Step 2: Generate Layer 2 (Adult Learning)**
After Layer 1 completes, note the file ID from Google Drive.

```bash
POST https://your-n8n.app.n8n.cloud/webhook/aethelgard-generate-layer2
Body:
{
  "conceptId": "00-02",
  "layer1FileId": "1abc...xyz"  // From Drive
}
```

**Step 3: Enrich with RAG Metadata (Parallel)**
Can run on Layer 1 OR Layer 2 output.

```bash
POST https://your-n8n.app.n8n.cloud/webhook/aethelgard-enrich-rag
Body:
{
  "conceptId": "00-02",
  "sourceFileId": "1abc...xyz"  // Layer 1 or 2 file
}
```

**Step 4: Generate Layer 3 (Story Mode)**
After Layer 2 completes:

```bash
POST https://your-n8n.app.n8n.cloud/webhook/aethelgard-generate-layer3
Body:
{
  "conceptId": "00-02",
  "layer2FileId": "1def...xyz"  // From Drive
}
```

---

### **Batch Generation Strategy:**

**Option A: Sequential Pipeline (Highest Quality)**
```
For each concept:
  1. Generate Layer 1
  2. Wait for completion
  3. Generate Layer 2
  4. Wait for completion
  5. Generate Layer 3
  6. Run RAG enrichment on final output
```

**Timeline:** ~4-5 minutes per concept (with Gemini processing)
**Best for:** Final production content, quality over speed

---

**Option B: Parallel Batch (Fastest)**
```
Batch 1 (10 concepts):
  - Generate all Layer 1 in parallel (10 requests)
  - Wait for all to complete

Batch 2:
  - Generate all Layer 2 in parallel (10 requests)
  - Wait for all to complete

Batch 3:
  - Generate all Layer 3 in parallel (10 requests)
  - Simultaneously run RAG enrichment (10 parallel)
```

**Timeline:** ~1.5 hours for 72 concepts (Gemini 1.5 Flash: 1,500 req/day)
**Best for:** Maximizing Gemini subscription ROI (17 days left)

---

**Option C: Hybrid Waterfall (Balanced)**
```
Week 1: Generate all 72 Layer 1 (batch)
Week 2: Generate all 72 Layer 2 (batch) + RAG enrichment (parallel)
Week 3: Generate all 72 Layer 3 (batch)
```

**Timeline:** 3 weeks
**Best for:** Quality + manageable review cycles

---

## 📊 Cost & Performance

### **Gemini API Costs:**
- **Gemini 1.5 Flash:** FREE (1,500 requests/day)
- **Gemini 1.5 Pro:** Included in Ultra subscription (₹25,000)

### **Expected Token Usage per Concept:**

| Workflow | Input Tokens | Output Tokens | Total |
|----------|--------------|---------------|-------|
| Layer 1 | ~1,500 | ~3,000 | ~4,500 |
| Layer 2 | ~3,500 | ~4,500 | ~8,000 |
| RAG Enrichment | ~3,000 | ~2,500 | ~5,500 |
| Layer 3 | ~4,500 | ~5,000 | ~9,500 |
| **Per Concept** | | | **~27,500** |
| **72 Concepts** | | | **~1.98M tokens** |

### **Gemini 1.5 Pro Context:** 2M tokens (fits entire dataset!)

### **Generation Speed:**
- **Layer 1:** ~45-60 seconds
- **Layer 2:** ~60-90 seconds
- **RAG Enrichment:** ~30-45 seconds
- **Layer 3:** ~90-120 seconds

**Total per concept:** ~4-5 minutes (sequential)

**72 concepts:**
- Sequential: ~5-6 hours
- Parallel (10 at a time): ~1.5-2 hours

---

## 🎯 Best Practices

### **Content Quality:**
1. **Review Layer 1 outputs** before proceeding to Layer 2
2. **Batch review every 10 concepts** (don't generate all 72 blindly)
3. **Test RAG enrichment on 5 concepts first** (validate metadata quality)
4. **Story Mode is experimental** (may need prompt tuning)

### **Workflow Management:**
1. **Keep track of file IDs** (use spreadsheet to map conceptId → Layer 1 ID → Layer 2 ID → Layer 3 ID)
2. **Tag Google Drive files** with conceptId in filename
3. **Use Progress Tracker** (update after each layer completes)

### **Error Handling:**
- **If Layer 2/3 fails:** Re-run with same input file ID
- **If output is malformed:** Check Gemini response in n8n execution logs
- **If workflow times out:** Increase n8n execution timeout (default: 120s)

### **ROI Maximization (17 Days Left):**
1. **Days 1-3:** Generate all 72 Layer 1 (base content)
2. **Days 4-5:** Review Layer 1, fix any issues
3. **Days 6-10:** Generate all 72 Layer 2 + RAG enrichment
4. **Days 11-12:** Review Layer 2/RAG quality
5. **Days 13-17:** Generate Layer 3 (story mode) for top 30 concepts

---

## 📁 File Naming Convention

**Layer 1:** `{conceptId}.json`
Example: `00-02.json`

**Layer 2:** `{conceptId}_layer2.json`
Example: `00-02_layer2.json`

**RAG Enriched:** `{conceptId}_rag.json`
Example: `00-02_rag.json`

**Layer 3:** `{conceptId}_layer3_story.json`
Example: `00-02_layer3_story.json`

---

## 🐛 Troubleshooting

### **"conceptId is missing" error:**
- Check webhook body includes `conceptId` field
- Verify JSON format is correct

### **"Invalid content data" error:**
- Ensure input file ID is correct Google Drive file ID
- Check file is JSON format (not binary/corrupt)
- Verify Google Drive permissions (workflow can access file)

### **"Prompt too long" warning:**
- Layer 2/3 prompts are long (~6,000 tokens)
- Gemini 1.5 Flash supports up to 128K context (should be fine)
- If fails, switch to Gemini 1.5 Pro

### **RAG metadata missing fields:**
- Review prompt (may need to add examples)
- Gemini sometimes skips optional fields
- Re-run with more explicit JSON structure in prompt

### **Story Mode sounds unnatural:**
- Adjust character voice examples in prompt
- Tune "narrative balance" (currently 60% story, 40% technical)
- Consider using Gemini 1.5 Pro for better narrative quality

---

## 🔮 Future Enhancements

### **Automation Ideas:**
1. **Auto-Chaining:** Layer 1 completion triggers Layer 2 automatically
2. **Quality Scoring:** Add node to evaluate output quality (reject if <7/10)
3. **Human Review Step:** Pause workflow, email for approval, resume
4. **Batch Orchestrator:** Single workflow that manages all 72 concepts

### **Content Improvements:**
1. **Visual Asset Generation:** Add DALL-E node to create diagrams
2. **Video Script Generation:** Add node to create YouTube scripts
3. **Quiz Generation:** Separate workflow for assessment questions
4. **Translation:** Multi-language support (Hindi, Spanish, etc.)

---

## 📞 Support & Maintenance

**Created by:** Asheesh Ranjan Srivastava
**AI Collaboration:** Claude Code (Anthropic)
**Date:** November 2, 2025
**Project:** Aethelgard Academy (Gemini ROI Sprint)

**Session Logs:** `D:\Claude\session_logs\2025-11-02_*.md`

**Related Documentation:**
- `2025-11-02_GEMINI-MASTER-PLAN-16DAY-SPRINT.md`
- `2025-11-02_CHECKPOINT-AETHELGARD-CONTENT-GENERATOR-DESIGN.md`

---

**Status:** ✅ All 4 workflows created and documented
**Ready for:** Configuration → Testing → Batch generation

**Timeline:** 17 days to maximize ₹25,000 Gemini subscription
**Goal:** Generate 72 high-quality Python concepts across 3 layers + RAG metadata

---

**Let's transform educational content at scale! 🚀**
