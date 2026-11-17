# AI-Powered Customer Feedback Analysis Using Prompt Engineering

An AI-powered customer feedback analysis project that explores how prompt engineering can improve the quality of AI-generated business insights, customer feedback summaries, sentiment classifications, and business recommendations.

The project combines **Python, Prompt Engineering, ChatGPT, and Microsoft Power BI** to transform customer feedback into actionable business insights.

## Project Overview

Customer feedback provides valuable information about customer satisfaction, product quality, and service performance. However, analysing large volumes of customer reviews manually can be time-consuming.

This project investigates how carefully designed prompts can help automate and improve customer feedback analysis.

Four prompt engineering tasks were implemented and evaluated:

1. Data Analysis
2. Summarization
3. Sentiment Classification
4. Business Content Generation

Each task was tested using an initial prompt (Version 1) and an improved prompt (Version 2). Their outputs were compared using a structured evaluation framework.

## Project Objectives

- Analyse customer feedback and identify satisfaction patterns.
- Design effective prompts for different customer feedback tasks.
- Compare initial and improved prompt performance.
- Evaluate AI-generated outputs using predefined quality criteria.
- Generate practical business recommendations.
- Develop an interactive Power BI dashboard to visualize customer feedback insights.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data preprocessing and evaluation |
| Pandas | Dataset preparation and analysis |
| NumPy | Numerical operations |
| Scikit-learn | Evaluation support |
| ChatGPT | Manual prompt testing and AI-generated outputs |
| Microsoft Power BI | Interactive dashboard development |
| Git and GitHub | Version control and project management |

## Dataset Description

The project uses a **synthetic e-commerce customer feedback dataset containing 1,000 reviews**.

The dataset includes:

- Review ID
- Review Date
- Product Category
- Product Name
- Customer Rating
- Feedback Text
- Reference Sentiment Label
- Feedback Channel

Five product categories are represented:

- Electronics
- Clothing
- Home & Kitchen
- Beauty & Personal Care
- Books & Stationery

**Note:** The dataset is synthetically generated for educational and experimental purposes. It does not represent actual customer transactions or real business records.

## Prompt Engineering Methodology

Four prompt engineering tasks were developed. Each task contains two prompt versions.

| Task | Initial Prompt | Improved Prompt |
|---|---|---|
| Data Analysis | V1 | V2 |
| Summarization | V1 | V2 |
| Classification | V1 | V2 |
| Content Generation | V1 | V2 |

The improved prompts introduced clearer instructions, defined roles, structured output requirements, accuracy constraints, and task-specific guidelines.

### Prompt Evaluation Criteria

Each prompt output was evaluated using five criteria on a scale of 1 to 5:

- Accuracy
- Relevance
- Completeness
- Clarity
- Instruction Following

The average score was calculated to compare the performance of the initial and improved prompts.

## Prompt Evaluation Results

| Experiment | Initial (V1) | Improved (V2) | Improvement |
|---|---:|---:|---:|
| Classification | 4.0 | 5.0 | +1.0 |
| Content Generation | 4.8 | 4.8 | 0.0 |
| Data Analysis | 4.6 | 4.8 | +0.2 |
| Summarization | 4.2 | 5.0 | +0.8 |
| **Overall Average** | **4.4** | **4.9** | **+0.5** |

The evaluation indicates that the improved prompts achieved a higher overall average score.

Classification and summarization showed the largest improvements, while content generation maintained the same score.

**Evaluation note:** Scores were assigned using a human-assessed rubric and represent the results of these project experiments, rather than an objective benchmark.

## Customer Feedback Analysis Results

The analysis of the 1,000-review dataset produced the following findings:

| Metric | Result |
|---|---:|
| Total Reviews | 1,000 |
| Average Customer Rating | 3.35 / 5 |
| Positive Feedback | 506 (50.6%) |
| Negative Feedback | 276 (27.6%) |
| Neutral Feedback | 218 (21.8%) |

### Average Rating by Product Category

| Product Category | Average Rating |
|---|---:|
| Beauty & Personal Care | 3.46 |
| Electronics | 3.44 |
| Home & Kitchen | 3.35 |
| Books & Stationery | 3.31 |
| Clothing | 3.19 |

Clothing recorded the lowest average rating, while Beauty & Personal Care recorded the highest.

## Power BI Dashboard

An interactive Power BI dashboard was developed to present the customer feedback analysis results.

### Dashboard Features

- KPI cards displaying total reviews, average rating, positive feedback, and negative feedback.
- Customer sentiment distribution.
- Average customer rating by product category.
- Customer reviews by feedback channel.
- Customer rating distribution.
- Monthly customer review trends.
- Interactive slicers for product category, sentiment, and review date.

### Dashboard Preview

![Customer Feedback Analysis Power BI Dashboard](powerbi/dashboard.png)

The complete Power BI dashboard file is available in the `powerbi` folder:

`Customer_Feedback_Analysis_Dashboard.pbix`

## Project Structure

```text
AI-Prompt-Engineering/
│
├── dataset/
│   ├── customer_feedback_dataset.csv
│   └── processed_dataset.csv
│
├── prompts/
│   ├── data_analysis.txt
│   ├── summarization.txt
│   ├── classification.txt
│   └── content_generation.txt
│
├── src/
│   ├── data_preprocessing.py
│   ├── prompt_manager.py
│   ├── prepare_manual_prompts.py
│   ├── evaluate_prompts.py
│   └── ai_engine.py
│
├── outputs/
│   ├── initial_outputs/
│   ├── improved_outputs/
│   ├── manual_prompts/
│   ├── prompt_evaluation.csv
│   ├── prompt_comparison.csv
│   └── prompt_comparison.png
│
├── powerbi/
│   ├── Customer_Feedback_Analysis_Dashboard.pbix
│   └── image.png
│
├── requirements.txt
└── .gitignore
```

## Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/Shavindi0426/AI-Prompt-Engineering.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Prompt-Engineering
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Data Preprocessing

```bash
python src/data_preprocessing.py
```

### 6. Generate Manual Prompt Files

```bash
python src/prepare_manual_prompts.py
```

The generated initial and improved prompts are stored in the `outputs/manual_prompts/` directory.

### 7. Test Prompts

Copy the generated prompts into ChatGPT to perform the manual prompt experiments. Save the generated responses in their respective output folders.

### 8. Evaluate Prompt Performance

```bash
python src/evaluate_prompts.py
```

The evaluation results and comparison visualizations are stored in the `outputs/` directory.

### 9. View the Power BI Dashboard

Open the `.pbix` file in Microsoft Power BI Desktop.

## Key Learning Outcomes

Through this project, the following areas were explored:

- Practical prompt engineering techniques.
- Differences between initial and improved prompts.
- AI-generated customer feedback analysis.
- Sentiment classification and text summarization.
- Evaluation of AI output quality.
- Data preprocessing and visualization using Python.
- Interactive business intelligence dashboard development.
- Translating customer feedback into actionable business recommendations.

## Future Improvements

Potential future enhancements include:

- Integrating an AI API for automated prompt execution.
- Expanding the dataset with real customer feedback.
- Implementing automated sentiment evaluation.
- Developing real-time customer feedback monitoring.
- Adding advanced customer satisfaction metrics.

## Author

**Shavindi Athukorala**

Data Science Undergraduate | SLIIT

GitHub: [Shavindi0426](https://github.com/Shavindi0426)

---

*This project was developed for educational purposes as part of an individual Prompt Engineering assignment.*
