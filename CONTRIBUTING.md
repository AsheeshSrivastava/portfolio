# Contributing to Portfolio

Thank you for your interest in contributing to the portfolio!

## 📋 Portfolio Structure

This repository is a **collection of independent projects** organized using Git submodules. It serves as a showcase of AI Engineering, Full-Stack Development, and Automation projects.

```
portfolio/
├── apps/           # 7 independent application submodules
├── projects/       # Major projects (Aethelgard Academy)
├── n8n-workflows/  # Automation workflow documentation
├── README.md       # Portfolio overview
├── LICENSE         # License for portfolio documentation
└── CONTRIBUTING.md # This file
```

## 🎯 Types of Contributions

### 1. Portfolio Documentation Improvements

**What:** Improvements to README.md, documentation structure, or navigation.

**Examples:**
- Clarifying project descriptions
- Fixing typos or broken links
- Improving navigation structure
- Adding missing sections
- Updating project statistics

**How to Contribute:**
1. Fork the repository
2. Make changes to documentation files
3. Submit a pull request with clear description
4. Ensure all submodule links still work

### 2. Adding New Projects

**What:** Adding new projects to the portfolio as submodules.

**Requirements:**
- Project must have its own GitHub repository
- Project must have comprehensive documentation
- Project must have proper licensing (preferably AGPL-3.0)
- Project must align with portfolio themes (AI Engineering, Full-Stack, Automation)

**How to Add:**
1. Ensure your project repository is ready (README, LICENSE, etc.)
2. Fork this portfolio repository
3. Add your project as a submodule:
   ```bash
   git submodule add <your-repo-url> apps/<project-name>
   ```
4. Update README.md to include your project
5. Submit pull request with project details

### 3. Reporting Issues

**What:** Report broken links, outdated information, or documentation errors.

**How to Report:**
1. Open an issue on GitHub
2. Provide clear description of the problem
3. Include links/screenshots if applicable
4. Suggest fix if possible

## 🛠️ Technical Guidelines

### Markdown Standards

- Use proper Markdown formatting
- Include links to external resources
- Use badges consistently (shields.io)
- Maintain consistent emoji usage (✅, 🔨, 📦, etc.)

### Project Links

All project links should include:
- GitHub repository link
- Live demo link (if deployed)
- Tech stack summary
- Key features (3-5 bullet points)
- Current status (✅ Complete, 🔨 In Development, 📦 Repository Ready)

### Submodule Management

⚠️ **Important:** Do NOT modify submodule contents directly in this repository.

To contribute to individual projects:
1. Navigate to the project's own repository
2. Follow that project's CONTRIBUTING.md guidelines
3. Submit contributions directly to that repository

This portfolio repository only tracks the submodule references, not the actual project code.

## 📂 Submodule Structure

### Apps (7 submodules)

Each app is an independent repository:

1. **quest-crossfire-linkedin-app** - AI LinkedIn post generator (Vercel/Node.js)
2. **aethelgard-concept-generator** - RAG application (Gradio/Python)
3. **quest-crossfire-chatbot** - Multi-persona chatbot (Streamlit/Python)
4. **obsidian-ai-assistant** - Knowledge base AI (Streamlit/Python)
5. **aethelgard-research-portal** - Backend API (FastAPI/Python)
6. **expense-tracker-ai** - Expense tracking (Next.js/TypeScript)
7. **question-forge** - Question quality assessment (Python/Gradio)

### Projects (1 private submodule)

1. **aethelgard-saga** (Aethelgard Academy) - Private interactive learning platform (React/TypeScript)

### n8n Workflows (4 workflow collections)

Documentation-only (no submodules):
1. **linkedin-job-automation** - Automated job applications
2. **newsletter-generation** - AI newsletter generation
3. **obsidian-research-to-vault** - Research automation
4. **aethelgard-content-generation** - Educational content pipeline

## 🔄 Pull Request Process

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/portfolio.git
   cd portfolio
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-improvement
   ```

3. **Make your changes**
   - Update documentation
   - Fix links
   - Add new project (as submodule)
   - Improve structure

4. **Test all links**
   - Verify all external links work
   - Check submodule links point to correct repositories
   - Ensure live demo links are valid

5. **Commit changes**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-improvement
   ```

7. **Submit pull request**
   - Clear title describing change
   - Detailed description of what and why
   - Link to any related issues
   - Screenshots if visual changes

## ✅ Quality Checklist

Before submitting PR:
- [ ] All links work (no 404s)
- [ ] Markdown properly formatted
- [ ] Consistent style with existing documentation
- [ ] No personal information exposed
- [ ] Submodules correctly referenced (if added)
- [ ] README.md updated (if adding project)
- [ ] No merge conflicts

## 🚫 What NOT to Contribute

- ❌ Modifications to submodule code (contribute directly to those repos)
- ❌ Personal information or credentials
- ❌ Spam or promotional content
- ❌ Off-topic projects (must align with portfolio themes)
- ❌ Projects without proper licensing

## 📄 License

By contributing, you agree that your contributions will be licensed under **AGPL-3.0**.

This means:
- Your documentation contributions remain open source
- Derivative works must also be AGPL-3.0
- Network use triggers source disclosure requirement
- Commercial use is allowed (with license compliance)

## 🏷️ Trademark Notice

**QUEST AND CROSSFIRE™**, **AETHELGARD ACADEMY™**, and **AETHELGARD AXIS™** are trademarks (Filed - awaiting certification).

When contributing:
- ✅ You may reference trademarks in documentation
- ❌ You may NOT claim ownership of trademarks
- ❌ You may NOT use trademarks for your own projects without permission

## 📧 Contact

**Asheesh Ranjan Srivastava**
- Email: asheeshsrivastava9@gmail.com
- LinkedIn: [linkedin.com/in/asheesh-ranjan-srivastava](https://www.linkedin.com/in/asheesh-ranjan-srivastava/)
- GitHub: [github.com/AsheeshSrivastava](https://github.com/AsheeshSrivastava)

For questions about:
- **Individual projects**: Visit that project's repository
- **Portfolio structure**: Open an issue or email
- **Collaboration opportunities**: Email or LinkedIn

## 🙏 Thank You

Thank you for helping improve this portfolio! Every contribution, no matter how small, is appreciated.

---

**Built with AI assistance from Claude Code (Anthropic)**

**◇ Where chaos becomes clarity. Small fixes, big clarity.**
