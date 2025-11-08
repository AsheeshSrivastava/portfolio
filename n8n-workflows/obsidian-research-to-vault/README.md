# AI Agent - Obsidian Research to Vault
**n8n AI Agent Workflow**

**Project:** Personal Knowledge Management Automation
**Purpose:** Automated research with AI agents → Obsidian vault integration
**Status:** Production-ready
**Tech Stack:** n8n + AI Agents + Obsidian Integration

---

## 📋 OVERVIEW

**What This Workflow Does:**
- Accepts research query or topic as input
- Deploys AI agent to research the topic autonomously
- Agent searches web, gathers information, evaluates sources
- Synthesizes findings into structured markdown notes
- Saves directly to Obsidian vault with proper formatting
- Maintains PKM (Personal Knowledge Management) structure

**Use Cases:**
- Quick research on new topics
- Learning and note-taking automation
- Building knowledge base systematically
- Capturing research with proper citations
- Maintaining consistent note structure

---

## 🎯 FEATURES

### AI Agent Intelligence
- **Autonomous Research**: Agent decides which sources to check
- **Source Evaluation**: Ranks reliability and relevance
- **Synthesis**: Combines multiple sources into coherent notes
- **Fact-Checking**: Cross-references information

### Obsidian Integration
- **Direct Vault Write**: Saves notes directly to your Obsidian vault
- **Markdown Formatting**: Properly formatted with headers, lists, links
- **Metadata**: Adds frontmatter (date, tags, source URLs)
- **Linking**: Can create wiki-links to related notes

### PKM Best Practices
- **Atomic Notes**: Each topic as separate note
- **Consistent Structure**: Template-based formatting
- **Tags & Categories**: Automatic categorization
- **Source Attribution**: All sources cited and linked

---

## 📁 FILES

### Current Production Version
```
current/
└── AI Agent - Obsidian Research to Vault.json
```

**File:** `AI Agent - Obsidian Research to Vault.json`
- **Size:** 3.5 KB
- **Nodes:** ~6-8 nodes (trigger, AI agent, markdown formatter, Obsidian write)
- **Status:** Working, production-ready

### Iterations
```
iterations/
└── (Future versions will be stored here)
```

---

## 🔧 SETUP GUIDE

### Prerequisites

**Required:**
1. **n8n** - Workflow platform
   - Cloud: https://app.n8n.cloud
   - Self-hosted: https://n8n.io/self-hosted

2. **Obsidian** - Note-taking app
   - Download: https://obsidian.md
   - Vault setup: Create or use existing vault

3. **AI Provider API**
   - OpenAI (recommended)
   - Anthropic Claude
   - Or other LLM with agent capabilities

**Optional:**
4. **Obsidian Sync** or **Git** - For vault backup
5. **Web Search API** - For enhanced research (Tavily, Google, Bing)

### Installation Steps

**Step 1: Import Workflow**
1. Open n8n dashboard
2. Click "Import from File"
3. Select `current/AI Agent - Obsidian Research to Vault.json`
4. Workflow loads with all nodes

**Step 2: Configure AI Agent**
1. Add OpenAI/Anthropic credentials in n8n
2. Link to AI Agent node
3. Configure agent settings:
   - Model: GPT-4 or Claude (for best reasoning)
   - Temperature: 0.3-0.5 (balanced)
   - Max tokens: 2000-4000 (comprehensive notes)

**Step 3: Configure Obsidian Integration**

**Option A: File System (Local n8n)**
1. Use "Write File" node
2. Set path to Obsidian vault folder
3. Example: `C:/Users/YourName/Documents/ObsidianVault/Research/`

**Option B: Obsidian Local REST API Plugin**
1. Install "Local REST API" plugin in Obsidian
2. Enable and configure API key
3. Use HTTP Request node in n8n
4. POST to: `http://localhost:27124/vault/{{vault-name}}/{{file-path}}`

**Option C: Obsidian Git + Webhook**
1. Use Obsidian Git plugin
2. Write file to vault via n8n
3. Trigger git commit via webhook

**Step 4: Test**
1. Run workflow with sample query: "Explain quantum computing"
2. Check Obsidian vault for new note
3. Verify formatting and content quality
4. Adjust parameters as needed

---

## 🚀 HOW TO USE

### Manual Execution

**Quick Research:**
1. Open workflow in n8n
2. Trigger with topic/query input
3. Example: "What are design patterns in software engineering?"
4. Agent researches, synthesizes, saves to vault
5. Open Obsidian to see new note

### Webhook Trigger

**From External Apps:**
1. Configure Webhook node as trigger
2. Get webhook URL from n8n
3. Call from any app/script:
   ```bash
   curl -X POST https://your-n8n-instance.com/webhook/research \
        -H "Content-Type: application/json" \
        -d '{"query": "Explain transformer models in AI"}'
   ```
4. Note appears in Obsidian automatically

### Obsidian Command

**Direct from Obsidian:**
1. Install "Advanced URI" plugin in Obsidian
2. Create Obsidian command that calls n8n webhook
3. Research from within Obsidian with hotkey

---

## 📊 WORKFLOW STRUCTURE

**Typical Node Flow:**
```
Manual Trigger / Webhook
    ↓
Get Research Query
    ↓
AI Agent (Research)
    ├── Web Search
    ├── Source Evaluation
    ├── Fact Gathering
    └── Synthesis
    ↓
Format as Markdown
    ├── Add Frontmatter
    ├── Structure Content
    └── Add Citations
    ↓
Write to Obsidian Vault
    ↓
Success Notification
```

**Key Nodes:**
- **Trigger**: Manual, Webhook, or Schedule
- **AI Agent**: Autonomous research
- **Markdown Formatter**: Template-based formatting
- **Write File / HTTP Request**: Save to vault
- **Notification**: Confirm completion

---

## 📝 NOTE TEMPLATE

**Generated Note Structure:**
```markdown
---
created: 2025-10-31
tags: [research, ai-generated, topic-name]
source: automated-research
---

# Topic Title

## Overview
[Brief summary of topic]

## Key Concepts
- Concept 1
- Concept 2
- Concept 3

## Details
[In-depth explanation with subsections]

### Subtopic 1
[Content]

### Subtopic 2
[Content]

## Examples
[Practical examples if applicable]

## Related Topics
[[Link to related note 1]]
[[Link to related note 2]]

## Sources
1. [Source Title](URL) - Description
2. [Source Title](URL) - Description

## Further Reading
- [Resource 1](URL)
- [Resource 2](URL)

---
*Generated by AI Agent on YYYY-MM-DD*
*Review and expand as needed*
```

---

## 🎓 LEARNING POINTS

**From Personal PKM Practice:**

1. **AI Agent Design**
   - Goal-oriented task breakdown
   - Tool selection and usage
   - Iterative refinement
   - Output validation

2. **Obsidian Integration**
   - Vault structure and organization
   - Markdown best practices
   - Frontmatter and metadata
   - Linking and graph connections

3. **Knowledge Management**
   - Atomic note principle
   - Progressive summarization
   - Zettelkasten method
   - PARA organization

4. **Automation Benefits**
   - Consistent note structure
   - Time savings on research
   - Reduced friction in learning
   - Systematic knowledge building

---

## 🔒 SECURITY & PRIVACY

**Local Data:**
- Workflow writes to local Obsidian vault
- Notes stored on your computer
- No data sent to cloud (except AI API for generation)

**API Usage:**
- AI provider processes research queries
- Web search APIs may log queries
- Review privacy policies of services used

**Vault Backup:**
- Use Obsidian Sync or Git for backup
- Encrypt sensitive notes
- Regular vault backups recommended

---

## 🐛 TROUBLESHOOTING

### Common Issues

**"Cannot Write to Vault"**
- **Cause:** Incorrect file path or permissions
- **Fix:**
  - Check Obsidian vault location
  - Verify n8n has write permissions
  - For cloud n8n, use Obsidian Local REST API plugin

**"AI Agent Timeout"**
- **Cause:** Complex query taking too long
- **Fix:**
  - Simplify query
  - Increase timeout in AI Agent node settings
  - Use faster AI model

**"Note Format Broken"**
- **Cause:** Markdown formatting errors from AI
- **Fix:**
  - Add validation node
  - Use structured output format in AI prompt
  - Post-process with regex

**"Duplicate Notes Created"**
- **Cause:** Same filename already exists
- **Fix:**
  - Add timestamp to filename
  - Check for existing file before writing
  - Implement merge/append logic

---

## 💡 CUSTOMIZATION IDEAS

**Enhancements:**
1. **Daily Notes Integration**: Auto-append research to daily note
2. **Spaced Repetition**: Generate flashcards from notes
3. **Graph Analysis**: Suggest related notes to link
4. **Multi-language**: Research in one language, notes in another
5. **Image Inclusion**: Fetch diagrams and images for visual topics

**Advanced Features:**
- **Collaborative Research**: Share research queue with team
- **Quality Scoring**: Rate and filter sources by credibility
- **Citation Management**: Integration with Zotero
- **Semantic Search**: Find similar notes in vault before creating new ones

---

## 📈 FUTURE IMPROVEMENTS

**Planned:**
- [ ] Add version history to iterations/
- [ ] Create comprehensive documentation folder
- [ ] Build note template library
- [ ] Implement duplicate detection
- [ ] Add source verification step

**Ideas:**
- [ ] Voice input for research queries
- [ ] Mobile app integration
- [ ] Collaborative note editing
- [ ] Auto-tagging based on content
- [ ] Progress tracking dashboard

---

## 📞 RELATED PROJECTS

**Portfolio:**
- Newsletter Generation (D:\Claude\portfolio\n8n-workflows\newsletter-generation)
- LinkedIn Job Automation (D:\Claude\portfolio\n8n-workflows\linkedin-job-automation)
- Obsidian AI Assistant (D:\Claude\portfolio\apps\obsidian-ai-assistant)

**Skills Demonstrated:**
- AI agent orchestration
- Obsidian/PKM best practices
- Markdown generation and formatting
- File system / API integration
- Knowledge base automation

---

## 🎯 QUICK REFERENCE

**File Location:** `D:\Claude\portfolio\n8n-workflows\obsidian-research-to-vault\current\`

**Import to n8n:**
1. Dashboard → "Import from File"
2. Select: `AI Agent - Obsidian Research to Vault.json`
3. Configure AI credentials
4. Set Obsidian vault path or API
5. Test with sample query

**Obsidian Setup:**
- Vault Path: Usually `Documents/ObsidianVault/`
- Plugin: "Local REST API" (for remote n8n)
- Structure: Create `Research/` folder for auto-generated notes

**AI Configuration:**
- Model: GPT-4 or Claude recommended
- Temperature: 0.3 (factual) to 0.7 (creative)
- System Prompt: "You are a research assistant. Gather information on [query] and format as comprehensive markdown note for Obsidian PKM system."

---

**Created:** October 31, 2025
**Last Updated:** October 31, 2025
**Author:** Asheesh Ranjan Srivastava (Zyric)
**Organization:** QUEST AND CROSSFIRE™
**Purpose:** Personal Knowledge Management Automation

---

**© 2025 Asheesh Ranjan Srivastava**
*AI-powered research automation*
*Built for Obsidian PKM workflow*
