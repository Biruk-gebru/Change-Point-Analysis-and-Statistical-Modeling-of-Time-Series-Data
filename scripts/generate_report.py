
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
import os
import pandas as pd

# Report Configuration
REPORT_FILENAME = "/home/karanos/kiam/week11/prod/docs/Interim_Report_Task1.pdf"
AUTHOR = "Biruk Gebru Jember"
TITLE = "Interim Report: Brent Oil Analysis & Change Point Methodology"

# Data Paths
BASE_DIR = "/home/karanos/kiam/week11/prod"
RESULTS_DIR = os.path.join(BASE_DIR, "results")
FIGURES_DIR = os.path.join(RESULTS_DIR, "figures")
EVENTS_CSV = os.path.join(BASE_DIR, "data/events/geopolitical_events.csv")

def add_image(story, filename, caption, styles, width=450, height=140):
    img_path = os.path.join(FIGURES_DIR, filename)
    if os.path.exists(img_path):
        try:
            img = Image(img_path, width=width, height=height)
            story.append(img)
            story.append(Paragraph(caption, styles['Caption']))
        except Exception:
            story.append(Paragraph(f"[Image missing: {filename}]", styles['Normal']))
    else:
        story.append(Paragraph(f"[Image not found: {filename}]", styles['Normal']))

def load_events():
    if os.path.exists(EVENTS_CSV):
        df = pd.read_csv(EVENTS_CSV)
        # Compact table: Date, Event (truncated)
        data = [["Date", "Event"]]
        for _, row in df.iterrows():
             data.append([str(row['Date'])[:10], row['Event'][:50]]) 
        return data
    return [["No Event Data Found"]]

def create_report():
    os.makedirs(os.path.dirname(REPORT_FILENAME), exist_ok=True)
    # Reduced margins to maximize space
    doc = SimpleDocTemplate(REPORT_FILENAME, pagesize=letter,
                            rightMargin=40, leftMargin=40,
                            topMargin=40, bottomMargin=40) 
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', parent=styles['Normal'], alignment=TA_JUSTIFY, spaceAfter=4, leading=11, fontSize=9))
    styles.add(ParagraphStyle(name='SectionHeader', parent=styles['Heading2'], spaceAfter=4, spaceBefore=8, textColor=colors.darkblue, fontSize=11))
    styles.add(ParagraphStyle(name='SubSectionHeader', parent=styles['Heading3'], spaceAfter=2, spaceBefore=4, fontSize=10))
    styles.add(ParagraphStyle(name='Caption', parent=styles['Italic'], alignment=TA_CENTER, fontSize=7, spaceAfter=6, textColor=colors.dimgrey))
    
    Story = []

    # --- Title ---
    Story.append(Paragraph(TITLE, styles['Heading1']))
    Story.append(Paragraph(f"<b>Author:</b> {AUTHOR} | <b>Date:</b> October 2023", styles['Normal']))
    Story.append(Spacer(1, 8))

    # --- 1. Business Context ---
    Story.append(Paragraph("1. Business Objective", styles['SectionHeader']))
    text = """
    <b>Birhan Energies</b> aims to quantify the impact of geopolitical shocks (sanctions, conflicts, OPEC policies) on Brent Crude price stability. 
    By distinguishing transient noise from structural regime shifts using statistical change point detection, we provide clients—sovereign funds and 
    policymakers—with actionable triggers for risk hedging and strategic planning.
    """
    Story.append(Paragraph(text, styles['Justify']))

    # --- 2. Task 1: Foundation ---
    Story.append(Paragraph("2. Task 1: Methodology & Initial Findings", styles['SectionHeader']))
    
    Story.append(Paragraph("2.1 Analytical Workflow", styles['SubSectionHeader']))
    text = """
    We executed a rigorous pipeline: (1) <b>Ingestion:</b> Cleaned 10 years of Brent price data (2012-2022); (2) <b>Transformation:</b> Converted prices to stationary Log Returns to stabilize variance; 
    (3) <b>Enrichment:</b> Integrated a dataset of 15 geopolitical events as ground truth for validation.
    """
    Story.append(Paragraph(text, styles['Justify']))

    # 2.2 Event Data
    Story.append(Paragraph("2.2 Event Dataset (Sample of 15)", styles['SubSectionHeader']))
    event_data = load_events()
    # Use very compact table
    t = Table(event_data, colWidths=[60, 350])
    t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
                           ('TEXTCOLOR', (0,0), (-1,0), colors.black),
                           ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                           ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                           ('FONTSIZE', (0,0), (-1,-1), 7),
                           ('BOTTOMPADDING', (0,0), (-1,0), 1),
                           ('GRID', (0,0), (-1,-1), 0.25, colors.grey)]))
    Story.append(t)
    Story.append(Spacer(1, 6))

    # 2.3 EDA
    Story.append(Paragraph("2.3 Exploratory Data Analysis (EDA)", styles['SubSectionHeader']))
    text = """
    Initial analysis confirms structural complexity. Raw prices are <b>non-stationary</b> (ADF p=0.199), exhibiting distinct regimes (Fig 1). 
    Log Returns are stationary (p<0.001) but show extreme <b>Volatility Clustering</b> (Fig 2) and high Kurtosis (>100), confirming "fat-tail" risks 
    typical of energy markets.
    """
    Story.append(Paragraph(text, styles['Justify']))

    # Images side-by-side logic roughly simulated by small sequential images
    add_image(Story, "fig_brent_prices_2012_2022.png", "Fig 1: Brent Crude Prices (2012-2022).", styles, height=130)
    add_image(Story, "volatility_clustering.png", "Fig 2: Volatility Clustering in Returns.", styles, height=130)

    # 2.4 Assumptions (CRITICAL)
    Story.append(Paragraph("2.4 Critical Assumptions & Limitations", styles['SubSectionHeader']))
    text = """
    <b>Critical Distinction:</b> While our models detect statistical associations between events and price breaks, <b>correlation does not imply causation.</b> 
    A change point near a sanctions date suggests a relationship, but cannot isolate it from confounding factors (e.g., global demand shifts, USD value). 
    We assume market efficiency is imperfect, allowing for lags. Furthermore, we assume Brent is a valid proxy for global oil sentiment.
    """
    Story.append(Paragraph(text, styles['Justify']))

    # --- 3. Roadmap ---
    Story.append(Paragraph("3. Strategic Roadmap (Tasks 2 & 3)", styles['SectionHeader']))
    
    text = """
    <b>Task 2: Bayesian Modeling (In Progress):</b> We are deploying a PyMC model to estimate probability distributions for change points ($\tau$). 
    Rather than a single date, this approach quantifies the <i>uncertainty</i> of when a regime shift occurred (see Fig 3 prototype).
    <br/><b>Task 3: Dashboard Delivery:</b> The final product will be a React/Flask dashboard allowing stakeholders to interactively visualize these risk regimes against event timelines.
    """
    Story.append(Paragraph(text, styles['Justify']))

    add_image(Story, "fig_changepoint_on_prices.png", "Fig 3: [Prototype] Expected Bayesian Change Point Output.", styles, height=140)

    doc.build(Story)
    print(f"Report generated: {REPORT_FILENAME}")

if __name__ == "__main__":
    create_report()
