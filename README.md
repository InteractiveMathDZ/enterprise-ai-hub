## Enterprise AI Data Intelligence Hub (ETL, RAG &amp; Agents).  
An end-to-end AI &amp; Data Engineering pipeline integrating automated ETL workflows, pgvector RAG document search, LangChain AI Agents, and interactive analytics dashboards. 


# 🚀 Enterprise AI Data Intelligence Hub (`enterprise-ai-hub`)

منصة متكاملة لـ **هندسة البيانات والذكاء الاصطناعي (AI & Data Engineering Pipeline)** تعتمد كلياً على البنية التحتية المجانية والحسابات السحابية (Cloudflare, GitHub Actions, Supabase/PostgreSQL). 

هدف هذا المشروع هو تقديم نموذج عملي متكامل يجمع بين سحب وتنظيف البيانات، بناء أنظمة استرجاع المعلومات (RAG)، أتمتة المهام عبر وكلاء الذكاء الاصطناعي (AI Agents)، وعرض المؤشرات التحليلية على لوحات قيادية.

---

## 🛠️ التقنيات والبنية التحتية المستخدمة (Tech Stack)

* **Hosting & Edge Computing:** Cloudflare Pages & Cloudflare Workers
* **CI/CD & Automation:** GitHub Actions (Automated ETL)
* **Database & Vector Store:** Supabase (PostgreSQL + `pgvector`)
* **AI & LLM Frameworks:** Gemini API, LangChain / LangGraph, Python
* **Data Engineering:** Python (`pandas`, `pydantic`, `SQLAlchemy`)
* **Data Visualization:** Microsoft Power BI + Interactive Web Dashboard

---

## 📋 المحاور الكبرى للمشروع (الكفاءات التطبيقية)

### 1. Data Engineering & ETL Pipelines
* بناء أنبوب بيانات سنوي/يومي مؤتمت باستخدام **GitHub Actions** لسحب البيانات من مصادر متعددة (APIs/JSON/CSV).
* تنظيف البيانات وتحويلها (Extraction, Cleaning, Transformation) بلغة Python.
* هيكلة البيانات وتخزينها في قاعدة بيانات **Supabase (PostgreSQL)** مع تطبيق الفهارس الحجمية (Indexing).

### 2. Generative AI, LLMs & RAG Implementation
* معالجة النصوص والمستندات واستخراج التضمينات Vector Embeddings باستخدام **Gemini Embeddings**.
* تخزين المتجهات في قاعدة بيانات **Supabase pgvector**.
* بناء محرك البحث والرد المتخصص **Retrieval-Augmented Generation (RAG)** للرد على أسئلة المستندات التقنية والمالية بدقة عالية.

### 3. AI Agent Development & LLM Tooling
* تصميم **وكيل ذكاء اصطناعي (AI Agent)** باستخدام **LangChain / LangGraph**.
* ربط الـ Agent بأدوات خارجية (Tools) لتنفيذ الاستعلامات المباشرة:
  * أداة الاستعلام الذكي عن قاعدة البيانات (Natural Language to SQL).
  * أداة البحث عن المستندات من نظام الـ RAG.
  * أداة جلب بيانات حية من APIs خارجية.

### 4. Data Visualization & Microsoft Power BI
* ربط قاعدة البيانات **Supabase (PostgreSQL)** بمشروع **Microsoft Power BI**.
* تصميم نموذج بيانات مترابط (Data Model) وإنشاء مقاييس DAX تحليليّة.
* بناء لوحة تحكم قيادية (Executive Dashboard) لتحويل النتائج والمعاملات إلى رؤى واستراتيجيات أعمال (Business Insights).

---

## 📂 هيكل المستودع (Project Structure)

```text
txt

enterprise-ai-hub/
├── .github/
│   └── workflows/          # أنبوبة أتمتة الـ ETL المجدولة (GitHub Actions)
├── src/
│   ├── etl/                # سكريبتات استخراج وتنظيف البيانات
│   ├── rag/                # محرك التضمين والبحث بالتشابه Vector Search
│   ├── agents/             # وكيل الذكاء الاصطناعي والأدوات (LangChain Tools)
│   └── api/                # نقطة النهاية المتصلة بـ Cloudflare Workers
├── powerbi/                # تقارير وملفات نماذج Power BI (.pbix)
├── docs/                   # التوثيق والبيانات التوضيحية
├── requirements.txt        # المكتبات البرمجية المطلوب تثبيتها
└── README.md               # التوثيق الرئيسي للمشروع
```

🚦 خطوات البدء وتشغيل المشروع محلياً
1. استنساخ المستودع (Clone Repository)
```bash
bash

git clone [https://github.com/YOUR_USERNAME/enterprise-ai-hub.git](https://github.com/YOUR_USERNAME/enterprise-ai-hub.git)
cd enterprise-ai-hub
```

3. إعداد البيئة الافتراضية
```bash
bash

python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

3. تثبيت الاعتمادات (Dependencies)
```bash
bash

pip install -r requirements.txt
```

5. إعداد متغيرات البيئة (.env)
أنشئ ملف .env في الجذر الرئيسي وقم بضبط المفاتيح التالية:
```env
env

SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
GEMINI_API_KEY=your_gemini_api_key
```

---

🔗 روابط مهمة واستعراض المخرجات
 * تطبيق الـ Dashboard الحي: [رابط Cloudflare Pages]
 * لوحة تفاعلات Power BI: متوفرة في المجلد /powerbi

---


