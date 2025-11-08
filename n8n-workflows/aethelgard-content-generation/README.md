# Aethelgard Content Generation Workflows

**Purpose:** Multi-layer AI content generation system for educational Python curriculum

---

## Structure

```
aethelgard-content-generation/
├── current/           # Latest working workflows
├── iterations/        # Development versions & older iterations
└── documentation/     # Usage guides and curriculum docs
```

---

## Current Workflows (Production-Ready)

### **Master Orchestrator**
- **File:** `Aethelgard Master Orchestrator FINAL.json`
- **Purpose:** Coordinates all content generation layers
- **Usage:** See documentation/ORCHESTRATOR_USAGE_GUIDE.md

### **Layer 1: Content Generator**
- **File:** `Layer_1_SIMPLE_QUALITY_FOCUSED.json`
- **Purpose:** Core educational content generation
- **Features:** Problem-System-Win framework, quality-focused output

### **Layer 2: Adult Learning Transformer**
- **File:** `Aethelgard Layer 2 Adult Learning Transformer.json`
- **Purpose:** Transforms content for adult learning principles
- **Features:** Experiential learning, real-world applications

### **Layer 3: Story Mode Generator**
- **File:** `Aethelgard Layer 3 Story Mode Generator.json`
- **Purpose:** Creates narrative-driven learning experiences
- **Features:** Story-based concept delivery

### **RAG Enrichment Engine**
- **File:** `Aethelgard RAG Enrichment Engine.json`
- **Purpose:** Enhances content with curriculum context
- **Features:** Retrieval-augmented generation for consistency

---

## Documentation

- **ORCHESTRATOR_USAGE_GUIDE.md** - How to use the orchestrator system
- **PARALLEL_WORKFLOWS_README.md** - Parallel workflow architecture
- **AETHELGARD_PYTHON_CURRICULUM_COMPREHENSIVE.md** - Complete curriculum structure

---

## Iterations

Development versions showing the evolution of the workflow system. Kept for reference and learning purposes.

---

## Tech Stack

- n8n (workflow automation)
- OpenAI API (GPT-4o-latest)
- LlamaIndex (RAG system)
- LanceDB (vector database)

---

## Related Projects

- **Aethelgard Academy** - Main learning platform (React + TypeScript)
- **Aethelgard Research Portal** - Backend content API (FastAPI)
- **Aethelgard Concept Generator** - Gradio RAG application

---

**Last Updated:** November 2025
